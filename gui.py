import customtkinter as ctk

app = ctk.CTk()

app.title("PO Translator")
app.geometry("700x450")


title_label = ctk.CTkLabel(
    app,
    text = "PO Translator"
)


file_label = ctk.CTkLabel(
    app,
    text = "File:"
)

file_entry = ctk.CTkEntry(
    app,
)

browse_button = ctk.CTkButton(
    app,
    text = "Browse"
)


language_label = ctk.CTkLabel(
    app,
    text = "Language"
)

option_menu = ctk.CTkOptionMenu(
    app,    
)


advanced_button = ctk.CTkButton(
    app,
    text = "Advanced Settings"
)


translate_button = ctk.CTkButton(
    app,
    text = "Translate"
)

cancel_button = ctk.CTkButton(
    app,
    text = "Cancel"
)


title_label.pack()

file_label.pack()
file_entry.pack()
browse_button.pack()

language_label.pack()
option_menu.pack()

advanced_button.pack()

translate_button.pack()
cancel_button.pack()


app.mainloop()