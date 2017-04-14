from tkinter import  *
from tkinter import filedialog

row = 0

def set_folder(path):
    path.set(filedialog.askdirectory()[-20:])

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        source_folder = StringVar()
        self.create_open_file_widget("Source Folder", source_folder)
        dest_folder = StringVar()
        self.create_open_file_widget("Destination Folder", dest_folder)

    def create_open_file_widget(self, label_text, string):
        text = Label(self, text=label_text)
        text.grid(row=row, column=0, padx=5, pady=5)

        folder = Entry(self, width = 30, textvariable = string)
        folder.grid(row=row, column=1, columnspan=3, padx=5, pady=5)

        button = Button(self, text="...", command=lambda: set_folder(string))
        button.grid(row=row, column=4, padx=5, pady=5)

        global row
        row += 1


root = Tk()
app = Application(master=root)
app.mainloop()