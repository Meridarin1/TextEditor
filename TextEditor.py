from tkinter import *
from tkinter import ttk
import tkinter.filedialog
import tkinter.messagebox


class TextEditor:

    def __init__(self, root):

        self.root = root
        root.title("Text Editor")

        #------Adding Text Area-----------------------------------
        self.text_area = Text(root)
        self.text_area.pack(side='left', fill='both', expand=True)

        # ------Adding Menu---------------------------------------
        the_menu = Menu(root)

        # ------Adding File Menu----------------------------------
        file_menu = Menu(the_menu, tearoff=0)
        file_menu.add_command(label='Open', command=self.open_file)
        file_menu.add_command(label='Save', command=self.save_file)
        file_menu.add_command(label='Quit', command=self.quit_app)
        the_menu.add_cascade(label="File", menu=file_menu)

        # ------Adding Scrollbar-----------------------------------
        scrollbar = Scrollbar(root)
        scrollbar.config(command=self.text_area.yview)
        scrollbar.pack(side='right', fill='y')

        root.config(menu=the_menu)

    def quit_app(self):
        self.root.quit()

    def open_file(self):

        file = tkinter.filedialog.askopenfilename(parent=self.root, initialdir='C:/Users/Public')

        if file:
            self.text_area.delete(1.0, END)

            try:
                with open(file) as f:
                    self.text_area.insert(1.0, f.read())

            except:
                tkinter.messagebox.showwarning("File Error", "Can't open file")

    def save_file(self):
        file = tkinter.filedialog.asksaveasfile(mode='w')

        if file is not None:
            data = self.text_area.get('1.0', END + '-1c')
            file.write(data)
            file.close()


