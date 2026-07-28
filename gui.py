import customtkinter as ctk
from tkinter import filedialog
import subprocess

GRID_PADDING = {
    "padx": 10,
    "pady": 10,
}

LANGUAGE_CODES = {
    "English": "en",
    "Brazilian Portuguese": "pt-BR",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese (Simplified)": "zh-CN",
    "Russian": "ru",
    "Polish": "pl",
    "Turkish": "tr",
}

def browse_file():
    filename = filedialog.askopenfilename()

    if filename:
        file_entry.delete(0, ctk.END)
        file_entry.insert(0, filename)

def translate():
    file_path = file_entry.get()
    language = LANGUAGE_CODES[language_menu.get()]
    batch_size = 50

    subprocess.run(
        [
            "python",
            "po_translator.py",
            file_path,
            language,
            str(batch_size),
        ]
    )

app = ctk.CTk()

app.title("PO Translator")
app.geometry("700x450")
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(4, weight=1)


title_label = ctk.CTkLabel(
    app,
    text="PO Translator"
)


file_label = ctk.CTkLabel(
    app,
    text="File:"
)

file_entry = ctk.CTkEntry(
    app,
    width=350,
)

browse_button = ctk.CTkButton(
    app,
    text="Browse",
    command=browse_file,
)


language_label = ctk.CTkLabel(
    app,
    text="Language"
)

language_menu = ctk.CTkOptionMenu(
    app,
    values=list(LANGUAGE_CODES.keys())
)


advanced_button = ctk.CTkButton(
    app,
    text="Advanced Settings"
)


translate_button = ctk.CTkButton(
    app,
    text="Translate",
    command=translate
)

cancel_button = ctk.CTkButton(
    app,
    text="Cancel",
    command=app.destroy
)


title_label.grid(
    row=0,
    column=1,
    **GRID_PADDING,
)

file_label.grid(
    row=1,
    column=0,
    sticky="w",
    **GRID_PADDING,
)

file_entry.grid(
    row=1,
    column=1,
    sticky="ew",
    **GRID_PADDING,
)

browse_button.grid(
    row=1,
    column=2,
    **GRID_PADDING,
)

language_label.grid(
    row=2,
    column=0,
    sticky="w",
    **GRID_PADDING,
)

language_menu.set("English")
language_menu.grid(
    row=2,
    column=2,
    **GRID_PADDING,
)

advanced_button.grid(
    row=3,
    column=1,
    **GRID_PADDING,
)

cancel_button.grid(
    row=5,
    column=1,
    sticky="e",
    **GRID_PADDING,
)

translate_button.grid(
    row=5,
    column=2,
    sticky="e",
    **GRID_PADDING,
)


app.mainloop()