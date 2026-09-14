import customtkinter as ctk
from tkinter import filedialog, messagebox
import subprocess
from pathlib import Path
import threading

GRID_PADDING = {
    "padx": 10,
    "pady": 10,
}

LANGUAGE_CODES = {
    "English": "en",
    "Brazilian Portuguese": "portuguese",
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

batch_size = 50


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")


def browse_file():
    filename = filedialog.askopenfilename()

    if filename:
        file_entry.delete(0, ctk.END)
        file_entry.insert(0, filename)

def open_advanced_settings():
    settings_window = ctk.CTkToplevel(app)

    settings_window.transient(app)
    settings_window.grab_set()

    settings_window.title("Advanced Settings")
    center_window(settings_window, 400, 200)


    batch_label = ctk.CTkLabel(
        settings_window,
        text="Batch size:"
    )

    batch_entry = ctk.CTkEntry(
        settings_window,
        width=100
    )

    batch_entry.insert(0, str(batch_size))

    def save_settings():
        global batch_size

        try:
            new_batch_size = int(batch_entry.get())
        except ValueError:
            messagebox.showerror(
                "Invalid batch size",
                "Batch size must be a number."
            )
            return

        if new_batch_size <= 0:
            messagebox.showerror(
                "Invalid batch size",
                "Batch size must be greater than 0."
            )
            return

        batch_size = new_batch_size

        batch_size_label.configure(
            text=f"Batch size: {batch_size}"
        )

        settings_window.destroy()

    save_button = ctk.CTkButton(
        settings_window,
        text="Save",
        command=save_settings
    )


    batch_label.grid(
        row=0,
        column=0,
        **GRID_PADDING
    )

    batch_entry.grid(
        row=0,
        column=1,
        **GRID_PADDING
    )

    save_button.grid(
        row=1,
        column=1,
        **GRID_PADDING
    )


def run_translation(file_path, language, batch_size):
    result = subprocess.run(
        [
            "python",
            "po_translator.py",
            file_path,
            language,
            str(batch_size)
        ]
    )

    if result.returncode == 0:
        app.after(
            0,
            lambda: status_label.configure(text="Translation completed!")
        )

        app.after(
            0,
            lambda: translate_button.configure(state="normal")
        )

    else:
        app.after(
            0,
            lambda: status_label.configure(text="Translation failed.")
        )

        app.after(
            0,
            lambda: translate_button.configure(state="normal")
        )

def translate():
    file_path = file_entry.get()
    language = LANGUAGE_CODES[language_menu.get()]

    path = Path(file_path)

    if (not path.exists()
        or not path.is_file()
        or path.suffix != ".po"):

        messagebox.showerror(
            "Invalid file",
            "Please select a valid .po file."
        )
        return


    status_label.configure(text="Translating...")
    translate_button.configure(state="disabled")

    threading.Thread(
        target=run_translation,
        args=(file_path, language, batch_size),
        daemon=True
    ).start()


app = ctk.CTk()

app.title("PO Translator")
center_window(app, 700, 450)

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
    text="Advanced Settings",
    command=open_advanced_settings
)

batch_size_label = ctk.CTkLabel(
    app,
    text=f"Batch size: {batch_size}"
)

status_label = ctk.CTkLabel(
    app,
    text="Ready"
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

batch_size_label.grid(
    row=3,
    column=2,
    sticky="w",
    **GRID_PADDING,
)

status_label.grid(
    row=4,
    column=1,
    sticky="w",
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