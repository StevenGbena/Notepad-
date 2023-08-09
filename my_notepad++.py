

#skip to content
#Using Gmail with screen readers
#Conversations
#0.38 GB of 15 GB used
#Terms · Privacy · Programme Policies
#Last account activity: 23 minutes ago
#Details
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext


keywords = ["def", "for","while","if","else","False","None","True","and","as","assert","async","await","break","class","continue","del","elif","except","finally","from","global","import","in","is","lambda","nonlocal","not","or","pass","raise","return","try","while","with","yield"]
keyword_color = "blue"
comment_color = "green"
coat_color = "red"

def highlight_syntax(event=None):
    text=editor.get("1.0", tk.END)
    editor.tag_remove("keyword", "1.0", tk.END)
    editor.tag_remove("comment", "1.0", tk.END)
    editor.tag_remove("coat", "1.0", tk.END)

    for keyword in keywords:
        start = "1.0"
        while True:
            index = editor.search(keyword, start, stopindex=tk.END)
            if not index:
                break
            end= f"{index}+{len(keyword)}c"
            editor.tag_add("keyword", index, end)
            start = end
    
    editor.tag_config("keyword", foreground=keyword_color)

    lines = text.split("\n")
    for i, line in enumerate(lines):
        start = f"{i+1}.0"
        if line.strip().startswith("#"):
            end= f"{i+1}.{len(line)}"
            editor.tag_add("comment", start, end)
            editor.tag_config("comment", foreground=comment_color)
        elif line.strip().startswith("''"):
            end = f"{i+1}.{len(line)}"
            editor.tag_add("coat", start, end)
            editor.tag_config("coat", foreground=coat_color)

root = tk.Tk()
root.title("Notepad++")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=file_menu)

def new_file():
    global current_file
    if editor.get("1.0", "end-1c"):
        result = tk.messagebox.askyesnocancel("Save", "Do you want to save the changes?")
        if result:
            save_file()
        elif result is None:
            return
    editor.delete("1.0", "end")
    current_file = None

file_menu.add_command(label="New", command=new_file)

def open_file():
    global current_file
    new_file
    file = filedialog.askopenfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file:
        editor.insert("1.0", file.read())
        current_file = file.name
        file.close()

file_menu.add_command(label="Open", command=open_file)

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w") as file:
            file.write(editor.get("1.0", "end"))
    else:
        save_file_as()

file_menu.add_command(label="Save", command=save_file)

def save_file_as():
    global current_file
    file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file:
        file.write(editor.get("1.0", "end"))
        current_file = file.name
        file.close()

file_menu.add_command(label="Save As", command=save_file_as)

edit_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: editor.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda:editor.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: editor.event_generate("<<Paste>>"))

search_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="Search", menu=search_menu)
search_menu.add_command(label="Find", command=None)
search_menu.add_command(label="Replace", command=None)

view_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Toggle Line Numbers", command=None)

encoding_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="Encoding", menu=encoding_menu)
encoding_menu.add_command(label="UTF-8", command=None)
encoding_menu.add_command(label="ASCII", command=None)

language_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="Language", menu=language_menu)
language_menu.add_command(label="Python",command=None)
language_menu.add_command(label="C++", command=None)

settings_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="Settings", menu=settings_menu)

tools_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="Tools", menu=tools_menu)

macro_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="Macro", menu=macro_menu)

run_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="Run", menu=run_menu)

plugins_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="Plugins", menu=plugins_menu)

windows_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="Windows", menu=windows_menu)

editor = scrolledtext.ScrolledText(root, wrap=tk.WORD)
editor.pack(fill="both", expand=True)

editor.tag_configure("keyword", foreground="red")
editor.tag_configure("comment", foreground="green")
editor.bind("<KeyRelease>", highlight_syntax)

current_file = None

root.mainloop()
#notepad_plus+.py
#Displaying notepad_plus+.py.