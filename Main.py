import tkinter as tk
row = 0
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.create_open_file_widget("Source Folder")
        self.create_open_file_widget("Destination Folder")

    def create_open_file_widget(self, label_text):
        self.text = tk.Label(self, text=label_text)
        self.text.grid(row=row, column=0, padx=5, pady=5)

        self.folder = tk.Entry(self)
        self.folder.grid(row=row, column=1, columnspan=3, padx=5, pady=5)

        self.button = tk.Button(self, text="...")
        self.button.grid(row=row, column=4, padx=5, pady=5)

        global row
        row += 1


root = tk.Tk()
app = Application(master=root)
app.mainloop()