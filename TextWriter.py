# HERDA A CLASSE TEXTEDITOR
import tkinter as tk
from TextEditor import TextEditor

class TextWriter(TextEditor):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.config(wrap="none")

        self.scroll_x = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.xview)
        self.scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.scroll_y = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.yview)
        self.scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.config(xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

    def xview(self, *args):
        self.scroll_x.set(*args)
        self.text_editor.xview(*args)

    def yview(self, *args):
        self.scroll_y.set(*args)
        self.text_editor.yview(*args)
