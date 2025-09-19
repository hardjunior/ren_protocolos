# Renomeador Automático de PDFs

Este projeto é um script Python que lê todos os ficheiros PDF na pasta onde é executado, extrai informações específicas do conteúdo, e renomeia os PDFs com base nesses dados. Caso os dados não sejam encontrados, o ficheiro é renomeado para `não_localizado.pdf` (ou com sufixo numérico para evitar sobrescrita).

---

## Funcionalidades

- Lê o conteúdo de todos os PDFs na pasta atual
- Extrai duas informações específicas antes e depois da linha que contém `Coords:`
- Renomeia os ficheiros no formato: `<dado1>_<dado2>.pdf`
- Se os dados não forem encontrados, renomeia como `não_localizado.pdf`, adicionando sufixos `(1)`, `(2)`, ... para evitar conflitos
- Garante nomes válidos para Windows removendo caracteres inválidos
- Fácil execução via script Python ou ficheiro executável `.exe`

---

## Requisitos

- Python 3.6+  
- Biblioteca PyMuPDF (fitz) para ler PDFs  

Instala com:

```bash
pip install PyMuPDF
