# PO Translator

A Python command-line tool that automatically translates `.po` files while preserving placeholders commonly used in PHP and WordPress applications.

## Key Features

* Automatic source language detection.
* Batch translation using Google Translate.
* Preserves placeholders such as `%s`, `%1$s`, `%%`, `{name}` and `\n`.
* Falls back to individual translation if a batch fails.
* Automatically generates a new translated `.po` file without modifying the original.

## Built With

- Python
- polib
- deep-translator

## Requirements

- Python 3.10 or newer
- Internet connection (required for Google Translate)

## Installation

Clone the repository:

```bash
git clone https://github.com/HarumiRin/po-translator.git
cd po-translator
```

Create and activate a virtual environment (recommended):

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script with the required arguments:

```bash
python po_translator.py input.po target_language batch_size
```

### Arguments

| Argument | Description |
|----------|-------------|
| `input.po` | Input `.po` file to translate. |
| `target_language` | Target language code (`pt-br`, `en`, `es`, `fr`, etc). |
| `batch_size` | Number of entries translated per request. |

### Example

```bash
python po_translator.py messages.po pt 50
```

This command translates `messages.po` into Portuguese using batches of 50 entries and creates `messages_translated.po`.

## Future Improvements

* Progress bar during translation.
* Support for additional translation providers.
* Unit tests.

## Licence

This project is licensed under the MIT License.