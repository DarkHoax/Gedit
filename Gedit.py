import tkinter as tk
from tkinter import filedialog, messagebox
from TextEditor import TextEditor
from TextWriter import TextWriter

class Gedit():
    def __int__(self, master):
        self.master = master
        self.text_editor = TextEditor(self.master)

        self.menu_bar = tk.Menu(self.master)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add(label="Novo", command=self.novo)
        self.file_menu.add(label="Abrir", command=self.abrir)
        self.file_menu.add(label="Salvar", command=self.salvar)
        self.file_menu.add(label="Salvar como", command=self.salvarcomo)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Sair", command=self.master.sair)
        self.menu_bar.add_cascade(label="Arquivo", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Inserir Texto", command=self.inserir_texto)
        self.menu_bar.add_cascade(label="Editar", menu=self.edit_menu)

    def novo(self):
        self.text_editor.novo()

    def abrir(self):
        self.text_editor.abrir()

    def salvar(self):
        self.text_editor.salvar()

    def salvarcomo(self):
        path = filedialog.asksaveasfilename()
        if path:
            self.text_editor.salvarcomo(path)

    def sair(self):
        if not self.text_editor.salvar():
            answer = tk.messagebox.askyesnocancel("Gedit", "Deseja salvar as alterações?")
            if answer == tk.YES:
                self.salvar()
                self.master.quit()
            elif answer == tk.NO:
                self.master.quit()
            else:
                return
        else:
            self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Editor de Textos")
    gedit = Gedit()
    root.config()
    writer = TextWriter(root)
    writer.pack(fill=tk.BOTH, expand=True)
    root.mainloop()