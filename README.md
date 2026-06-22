# PO Translator

Script em Python para traduzir automaticamente arquivos `.po`, preservando placeholders utilizados por aplicações PHP e WordPress.

## Funcionalidades

* Tradução automática utilizando Google Translate.
* Tradução em lote para reduzir o número de requisições.
* Preservação de placeholders como `%s`, `%1$s`, `%%`, `{name}` e `\n`.
* Tradução individual como fallback caso um lote falhe.
* Geração de um novo arquivo `.po` traduzido.

## Tecnologias

* Python
* polib
* deep-translator

## Instalação

Clone o repositório e instale as dependências:

```bash
pip install -r requirements.txt
```

## Como utilizar

Edite os nomes dos arquivos de entrada e saída no script e execute:

```bash
python po_translator.py
```

O arquivo traduzido será salvo automaticamente.
