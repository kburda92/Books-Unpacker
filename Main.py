from tkinter import  *
from tkinter import filedialog
from Config import Config

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.source_folder = StringVar()
        self.dest_folder = StringVar()
        self.__load_paths()
        self.__create_widgets()
        master.protocol('WM_DELETE_WINDOW', self.__save_and_exit)

    def __create_widgets(self):
        widgets = (("Source Folder", self.source_folder), ("Destination Folder", self.dest_folder))
        row = 0
        self.grid()
        for widget in widgets:
            text = Label(self, text=widget[0])
            text.grid(row=row, column=0, padx=5, pady=5)

            folder = Entry(self, width = 30, textvariable = widget[1])
            folder.grid(row=row, column=1, columnspan=3, padx=5, pady=5)

            button = Button(self, text="...", command=lambda value = widget[1]: self.__set_folder(value))
            button.grid(row=row, column=4, padx=5, pady=5)
            row += 1

    def __load_paths(self):
        self.config = Config()
        self.source_folder.set(self.config.source_path)
        self.dest_folder.set(self.config.dest_path)

    def __set_folder(self, path):
        path.set(filedialog.askdirectory())

    def __save_and_exit(self):
        self.config.source_path = self.source_folder.get()
        self.config.dest_path = self.dest_folder.get()
        self.config.save()
        self.quit()


root = Tk()
app = Application(master=root)
app.mainloop()