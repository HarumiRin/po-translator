import polib
from deep_translator import GoogleTranslator
import time
import re
import sys

SOURCE_LANGUAGE = "auto"

# Regex for WordPress/PHP placeholders
PLACEHOLDER_PATTERN = r'(%%|%\d*\$?[a-zA-Z]|{\w+}|\\n)'

def protect_placeholders(text):
    placeholders = re.findall(PLACEHOLDER_PATTERN, text)
    protected_text = text
    for i, ph in enumerate(placeholders):
        protected_text = protected_text.replace(ph, f"__PH{i}__")
    return protected_text, placeholders

def restore_placeholders(text, placeholders):
    restored_text = text
    for i, ph in enumerate(placeholders):
        restored_text = restored_text.replace(f"__PH{i}__", ph)
    return restored_text

def get_cli_args():
    if len(sys.argv) < 4:
        print("Usage: python po_translator.py input.po language batch_size")
        sys.exit(1)
    
    input_file = sys.argv[1]
    target_language = sys.argv[2].strip().lower()
    batch_size = int(sys.argv[3])

    output_file = input_file.replace(".po", "_translated.po")

    if batch_size <= 0:
        print("Batch size must be greater than 0")
        sys.exit(1)
    
    return input_file, output_file, target_language, batch_size

"""
def get_user_input():
    # Arquivos
    input_file = input("Input .po file: ")

    output_file = input_file.replace(".po", "_translated.po")

    target_language = input("Target language (en, fr, es...): ").strip().lower()

    while True:
        try:
            batch_size = int(input("Batch size (recommended: 50): "))
                
            if batch_size <= 0:
                print("Batch size must be greater than zero.")
                continue
            break
            
        except ValueError:
            print("Please enter a valid number.")
        
    return input_file, output_file, target_language, batch_size
"""

def main():
    input_file, output_file, target_language, batch_size = get_cli_args()

    # Load .po file
    po = polib.pofile(input_file)

    # Create translator instance
    translator = GoogleTranslator(
        source=SOURCE_LANGUAGE,
        target=target_language
        )

    # Filter untranslated entries
    entries = [e for e in po if e.msgid.strip() and not e.msgstr.strip()]

    total = len(entries)
    translated_count = 0

    for i in range(0, len(entries), batch_size):

        batch = entries[i:i+batch_size]

        protected_texts = []
        placeholder_groups = []

        for entry in batch:

            # Skip entries containing only placeholders
            if re.fullmatch(r'(%%|%\d*\$?[a-zA-Z])+', entry.msgid):
                entry.msgstr = entry.msgid
                continue

            protected_text, placeholders = protect_placeholders(entry.msgid)

            protected_texts.append(protected_text)
            placeholder_groups.append(placeholders)

        try:

            translations = translator.translate_batch(protected_texts)

            for entry, translation, placeholders in zip(batch, translations, placeholder_groups, strict=True):

                if not translation:
                    translation = entry.msgid

                translation = restore_placeholders(translation, placeholders)

                entry.msgstr = translation

                translated_count += 1
                print(f"[{translated_count}/{total}] Translated:", entry.msgid)

        except Exception as e:

            print(f"Batch translation failed: {e}")
            print("Trying individual translation...")

            for entry in batch:

                try:

                    protected_text, placeholders = protect_placeholders(entry.msgid)

                    translation = translator.translate(protected_text)

                    if not translation:
                        translation = entry.msgid

                    translation = restore_placeholders(translation, placeholders)

                    entry.msgstr = translation

                    translated_count += 1
                    print(f"[{translated_count}/{total}] Translated individually:", entry.msgid)

                except Exception:

                    print("Translation failed:", entry.msgid)
                    entry.msgstr = entry.msgid

        time.sleep(0.5)

    # Ensure msgstr is never None before saving
    for entry in po:
        if entry.msgstr is None:
            entry.msgstr = ""

    po.save(output_file)

    print("Translation completed!")

    
if __name__ == "__main__":
    main()