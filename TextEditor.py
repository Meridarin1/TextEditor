from tkinter import *
from tkinter import ttk
import tkinter.filedialog
import tkinter.messagebox
from PIL import Image, ImageTk


class TextEditor:

    def __init__(self, root):

        self.root = root
        root.title("Text Editor")

        #------Adding Text Area-----------------------------------
        text_area_frame = Frame(root)
        self.text_area = Text(text_area_frame)
        self.text_area.pack(side='left', fill='both', expand=True)

        '''DELETED traditional Menu
        # ------Adding Menu---------------------------------------
        the_menu = Menu(root)

        # ------Adding File Menu----------------------------------
        file_menu = Menu(the_menu, tearoff=0)
        file_menu.add_command(label='Open', command=self.open_file)
        file_menu.add_command(label='Save', command=self.save_file)
        file_menu.add_command(label='Quit', command=self.quit_app)
        the_menu.add_cascade(label="File", menu=file_menu)
        '''
        # ------Adding Scrollbar-----------------------------------
        scrollbar = Scrollbar(root)
        scrollbar.config(command=self.text_area.yview)
        scrollbar.pack(side='right', fill='y')

        #-------Adding IconBar-------------------------------------
        size = [24, 24]
        toolbar = Frame(root, relief=RAISED)

        open_img = Image.open("open.png")
        save_img = Image.open("save.png")
        exit_img = Image.open("exit.png")

        open_img.thumbnail(size)
        save_img.thumbnail(size)
        exit_img.thumbnail(size)

        open_icon = ImageTk.PhotoImage(open_img)
        save_icon = ImageTk.PhotoImage(save_img)
        exit_icon = ImageTk.PhotoImage(exit_img)

        open_button = Button(toolbar, image=open_icon, command=self.open_file)
        save_button = Button(toolbar, image=save_icon, command=self.save_file)
        exit_button = Button(toolbar, image=exit_icon, command=self.quit_app)

        open_button.image = open_icon
        save_button.image = save_icon
        exit_button.image = exit_icon

        open_button.pack(side=LEFT, padx=2, pady=2)
        save_button.pack(side=LEFT, padx=2, pady=2)
        exit_button.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)
        text_area_frame.pack(side=BOTTOM)
        #root.config(menu=the_menu)

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


