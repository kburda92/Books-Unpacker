from tkinter import  *
from tkinter import filedialog
from Config import Config
from os import *

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.source_folder = StringVar()
        self.dest_folder = StringVar()
        self.__load_paths()
        self.__create_widgets()
        master.protocol('WM_DELETE_WINDOW', self.__save_and_exit)

    def __create_widgets(self):
        entries = (("Source Folder", self.source_folder), ("Destination Folder", self.dest_folder))
        row = 0
        self.grid()
        for entry in entries:
            text = Label(self, text = entry[0])
            text.grid(row=row, column=0, padx=5, pady=5)

            folder = Entry(self, width = 30, textvariable = entry[1])
            folder.grid(row=row, column=1, padx=5, pady=5)

            button = Button(self, text="...", command=lambda value = entry[1]: self.__set_folder(value))
            button.grid(row=row, column=2, padx=5, pady=5)
            row += 1

        self._search_button = Button(self, text="Search for books", command= self.__search_for_books)
        self._search_button.grid(row=0, column=3, rowspan=2, padx=5, pady=5)

        self.found_dirs = Listbox(self)
        self.found_dirs.grid(row=3, column=1, sticky=E+W, padx=5, pady=5)
        scrollbar = Scrollbar(self)
        scrollbar.grid(row=3,column=1,sticky=N+S+E+W, padx=5, pady=5)
        self.found_dirs.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.found_dirs.yview)

        self.found_files = Listbox(self)
        self.found_files.grid(row=3, column=2, columnspan=2, sticky=W+E, padx=5, pady=5)
        # self.found_files.config(yscrollcommand=scrollbar.set)

    def __load_paths(self):
        self.config = Config()
        self.source_folder.set(self.config.source_path)
        self.dest_folder.set(self.config.dest_path)

    def __set_folder(self, path):
        dir = filedialog.askdirectory()
        if dir:
             path.set(dir)

    def __search_for_books(self):
        i=0
        directories = [d for d in listdir(self.source_folder.get()) if path.isdir(path.join(self.source_folder.get(),d))]
        for dir in list(directories):
            self.found_dirs.insert(i, dir)
            i+=1
        self._search_button.configure(state='disabled')

    def __save_and_exit(self):
        self.config.source_path = self.source_folder.get()
        self.config.dest_path = self.dest_folder.get()
        self.config.save()
        self.quit()


root = Tk()
app = Application(master=root)
app.mainloop()