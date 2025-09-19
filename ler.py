import fitz  # PyMuPDF
import os
import re

def extrair_texto_pdf(caminho_pdf):
    texto = ""
    with fitz.open(caminho_pdf) as doc:
        for pagina in doc:
            texto += pagina.get_text()
    return texto

def extrair_dados_para_nome(texto):
    linhas = texto.splitlines()
    for i, linha in enumerate(linhas):
        if "Coords:" in linha and i > 0 and i + 2 < len(linhas):
            anterior = linhas[i - 1].strip()
            depois2 = linhas[i + 2].strip()
            return anterior, depois2
    return None, None

def limpar_nome_ficheiro(texto):
    # Remove caracteres inválidos para nomes de ficheiros no Windows
    return re.sub(r'[<>:"/\\|?*]', '', texto)

def gerar_nome_nao_localizado(pasta):
    base = "não_localizado"
    contador = 1
    nome = f"{base}.pdf"
    caminho = os.path.join(pasta, nome)
    while os.path.exists(caminho):
        nome = f"{base} ({contador}).pdf"
        caminho = os.path.join(pasta, nome)
        contador += 1
    return nome

def renomear_pdf(caminho_pdf):
    texto = extrair_texto_pdf(caminho_pdf)
    dado1, dado2 = extrair_dados_para_nome(texto)

    diretorio = os.path.dirname(caminho_pdf)

    if all([dado1, dado2]):
        dado1 = limpar_nome_ficheiro(dado1)
        dado2 = limpar_nome_ficheiro(dado2)
        novo_nome = f"{dado1}_{dado2}.pdf"
    else:
        novo_nome = gerar_nome_nao_localizado(diretorio)

    novo_caminho = os.path.join(diretorio, novo_nome)

    try:
        os.rename(caminho_pdf, novo_caminho)
        print(f"✔ Renomeado: {os.path.basename(caminho_pdf)} → {novo_nome}")
    except Exception as e:
        print(f"❌ Erro ao renomear {os.path.basename(caminho_pdf)}: {e}")

def processar_pasta_pdf():
    pasta_atual = "."
    for nome_ficheiro in os.listdir(pasta_atual):
        if nome_ficheiro.lower().endswith(".pdf"):
            caminho_pdf = os.path.join(pasta_atual, nome_ficheiro)
            renomear_pdf(caminho_pdf)

# === Executar ===
processar_pasta_pdf()
