import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor(tk.Text):
    def __init__(self, master, **kwargs):
        super(TextEditor, self).__init__(master, **kwargs)
        self.master = master
        self.filename = None

    def novo(self):
        self.delete("1.0", tk.END)
        self.filename = None

    def abrir(self):
        path = filedialog.askopenfilename()
        if path:
            with open(path, "r") as f:
                self.insert(tk.END, f.read())
            self.filename = path

    def salvar(self):
        if self.filename:
            with open(self.filename, "w") as f:
                f.write(self.get("1.0", tk.END))
        else:
            self.salvarcomo()

    def salvarcomo(self, path=None):
        if not path:
            path = filedialog.asksaveasfilename()
        if path:
            with open(path, "w") as f:
                f.write(self.get("1.0", tk.END))
            self.filename = path

    def sair(self):
        if not self.filename and not self.get("1.0", tk.END).strip():
            self.master.quit()
        elif self.filename and self.get("1.0", tk.END).strip() == open(self.filename, "r").read().strip():
            self.master.quit()
        else:
            if not self.filename:
                title = "Arquivo sem título"
            else:
                title = self.filename
            answer = tk.messagebox.askyesnocancel(title, "Deseja salvar as alterações em " + title + "?")
            if answer == tk.YES:
                self.salvar()
                self.master.quit()
            elif answer == tk.NO:
                self.master.quit()
