from tkinter import  *
from tkinter import filedialog
from Config import Config
from os import *
from collections import defaultdict
from Book import Book

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.source_folder = StringVar()
        self.dest_folder = StringVar()
        self.checkbuttons = {}
        self.format_vars = {}
        self.books = []
        self.__load_paths()
        self.__create_widgets()
        master.protocol('WM_DELETE_WINDOW', self.__save_and_exit)

    def __create_widgets(self):
        self.grid()
        entries = (("Source Folder", self.source_folder), ("Destination Folder", self.dest_folder))
        row = 0
        for entry in entries:
            text = Label(self, text = entry[0])
            text.grid(row=row, column=0, padx=5, pady=5)

            folder = Entry(self, width = 30, textvariable = entry[1])
            folder.grid(row=row, column=1, padx=5, pady=5)

            button = Button(self, text="...", command=lambda value = entry[1]: self.__set_folder(value))
            button.grid(row=row, column=2, padx=5, pady=5)
            row += 1

        self._search_button = Button(self, text="Search for books", command=self.__search_for_books)
        self._search_button.grid(row=0, column=3, rowspan=2, padx=5, pady=5)

        self.found_books = Listbox(self)
        self.found_books.bind('<<ListboxSelect>>', self.__search_for_formats)
        self.found_books.grid(row=3, column=0, columnspan=2, rowspan=10, sticky=E+W, padx=5, pady=5)
        scrollbar = Scrollbar(self)
        scrollbar.grid(row=3,column=1,rowspan=10,sticky=N+S+E+W, padx=5, pady=5)
        self.found_books.config(yscrollcommand=scrollbar.set, state='disabled')
        scrollbar.config(command=self.found_books.yview)

        selected_formats_Label = Label(self, text="Found Formats:")
        selected_formats_Label.grid(row=3, column=2, columnspan = 3, padx=5, pady=5,sticky=N+W)
        check_buttons = ("pdf", "mobi", "epub")
        row=4
        for check_button in check_buttons:
            self.format_vars[check_button] = IntVar()
            self.checkbuttons[check_button] = Checkbutton(self, text=check_button, variable=self.format_vars[check_button])
            self.checkbuttons[check_button].grid(row=row, column=2, padx=5, pady=5,sticky=N+W)
            self.checkbuttons[check_button]['state'] ='disabled'
            row+=1

    def __load_paths(self):
        self.config = Config()
        self.source_folder.set(self.config.source_path)
        self.dest_folder.set(self.config.dest_path)

    def __set_folder(self, path):
        dir = filedialog.askdirectory()
        if dir:
             path.set(dir)

    def __search_for_books(self):
        books = [path.join(root, filename) for root, dirnames, filenames in walk(self.source_folder.get())
                 for filename in filenames if filename.endswith('.pdf') or filename.endswith('.mobi') or filename.endswith('.epub')]

        for book in list(books):
            self.books.append(Book(book))

        if len(self.books):
            self.found_books['state'] = 'normal'

        for book in self.books:
            if book.name not in self.found_books.get(0, 'end'):
                self.found_books.insert('end', book.name)

        self._search_button['state'] = 'disabled'

    def __search_for_formats(self, event):
        for button in self.checkbuttons.values():
            button['state'] = 'disabled'

        for format_var in self.format_vars.values():
            format_var.set(0)

        selection = event.widget.curselection()
        value = event.widget.get(selection[0])
        formats = [n for n in self.books if n.name == value]
        for format in formats:
            print(format.ext)
            self.checkbuttons[format.ext]['state'] = 'normal'
            self.format_vars[format.ext].set(1)

    def __save_and_exit(self):
        self.config.source_path = self.source_folder.get()
        self.config.dest_path = self.dest_folder.get()
        self.config.save()
        self.quit()


root = Tk()
app = Application(master=root)
app.mainloop()