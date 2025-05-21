# How to add this project to GitHub:
# 1. Open a terminal in this folder.
# 2. Run: git init
# 3. Run: git add .
# 4. Run: git commit -m "Initial commit"
# 5. (Optional) If you haven't already, create the repository on https://github.com
# 6. Run: git remote add origin https://github.com/saiteja001553/translator.git
# 7. Run: git branch -M main
# 8. Run: git push -u origin main

from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
import webbrowser
import os
import urllib.request

root = Tk()
root.title("Language Translator")
root.geometry("800x500")
root.resizable(False, False)
root.configure(bg="#e8eaf6")

# Overlay frame for content
overlay = Frame(root, bg="#ffffff", bd=0, highlightthickness=0)
overlay.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

# Translator
translator = Translator()
lang_dict = LANGUAGES

# ---------- Functions ----------
def translate_text():
    input_text = input_box.get("1.0", END).strip()
    dest_lang = lang_code_entry.get().strip()
    if input_text and dest_lang:
        try:
            translated = translator.translate(input_text, dest=dest_lang)
            output_box.delete("1.0", END)
            animate_output(translated.text)
        except Exception as e:
            output_box.delete("1.0", END)
            animate_output("Translation Error:\n" + str(e))
    else:
        output_box.delete("1.0", END)
        animate_output("Enter text and language code.")

def animate_output(text, idx=0):
    output_box.delete("1.0", END)
    def reveal(i=0):
        output_box.delete("1.0", END)
        output_box.insert(END, text[:i])
        if i < len(text):
            output_box.after(10, reveal, i+1)
    reveal()

def on_lang_select(event):
    if not lang_listbox.curselection():
        return
    selected = lang_listbox.get(lang_listbox.curselection())
    code = selected.split(' - ')[0]
    lang_code_entry.delete(0, END)
    lang_code_entry.insert(0, code)

def open_lang_link(event):
    webbrowser.open_new("https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages")

def open_unsplash(event):
    webbrowser.open_new("https://unsplash.com/photos/JIUjvqe2ZHg")

def open_github(event):
    webbrowser.open_new("https://github.com/ssut/py-googletrans")

# ---------- GUI Layout ----------

# Header with title only (no logo)
header = Frame(overlay, bg="#3949ab")
header.pack(fill=X, pady=(0, 10))
Label(header, text="Language Translator", bg="#3949ab", fg="white", font=("Arial", 18, "bold")).pack(side=LEFT, padx=15, pady=5)

# Info links
links_frame = Frame(overlay, bg="#ffffff")
links_frame.pack(fill=X, pady=(0, 5))
lang_link = Label(links_frame, text="Language Codes", fg="#1976d2", bg="#ffffff", cursor="hand2", font=("Arial", 10, "underline"))
lang_link.pack(side=LEFT, padx=10)
lang_link.bind("<Button-1>", open_lang_link)
unsplash_link = Label(links_frame, text="Background Photo", fg="#1976d2", bg="#ffffff", cursor="hand2", font=("Arial", 10, "underline"))
unsplash_link.pack(side=LEFT, padx=10)
unsplash_link.bind("<Button-1>", open_unsplash)
github_link = Label(links_frame, text="Project on GitHub", fg="#1976d2", bg="#ffffff", cursor="hand2", font=("Arial", 10, "underline"))
github_link.pack(side=LEFT, padx=10)
github_link.bind("<Button-1>", open_github)

main_frame = ttk.Frame(overlay, padding=10)
main_frame.pack(fill=BOTH, expand=True)

sidebar = Frame(main_frame, bg="#f5f5f5", width=200)
sidebar.pack(side=LEFT, fill=Y, padx=(0,10), pady=0)
sidebar.pack_propagate(False)
Label(sidebar, text="Languages", bg="#f5f5f5", fg="#3949ab", font=("Arial", 13, "bold")).pack(pady=(10,5))
lang_listbox = Listbox(sidebar, font=("Arial", 10), width=24, height=18, bg="#e3eafc", fg="#222")
for code, name in sorted(lang_dict.items()):
    lang_listbox.insert(END, f"{code} - {name.title()}")
lang_listbox.pack(pady=5, padx=5)
lang_listbox.bind('<<ListboxSelect>>', on_lang_select)

content_frame = ttk.Frame(main_frame)
content_frame.pack(side=LEFT, fill=BOTH, expand=True)

Label(content_frame, text="Enter text to translate:", bg="#ffffff", font=("Arial", 12)).pack(pady=(5,2), anchor=W)
input_box = Text(content_frame, height=5, width=50, font=("Arial", 11), bg="#f8fafc", fg="#222")
input_box.pack(pady=2)

Label(content_frame, text="Destination language code (e.g., te for Telugu):", bg="#ffffff", font=("Arial", 12)).pack(pady=(10,2), anchor=W)
lang_code_entry = ttk.Entry(content_frame, font=("Arial", 11), width=20)
lang_code_entry.pack(pady=2, anchor=W)

ttk.Button(content_frame, text="Translate", command=translate_text).pack(pady=12)

Label(content_frame, text="Translated text:", bg="#ffffff", font=("Arial", 12)).pack(pady=(10,2), anchor=W)
output_box = Text(content_frame, height=5, width=50, font=("Arial", 11), fg="#1b5e20", bg="#f8fafc")
output_box.pack(pady=2)

# Style
style = ttk.Style()
style.theme_use('clam')
style.configure('TFrame', background='#ffffff')
style.configure('TButton', font=('Arial', 12, 'bold'), background='#4CAF50', foreground='white')
style.map('TButton', background=[('active', '#388e3c')])

# Run app
root.mainloop()
