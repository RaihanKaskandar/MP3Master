from tkinter import *
from tkinter import filedialog

__mp3_files = []

def init_file_explorer():
    window = Tk()
    window.title('File Explorer')
    window.geometry("500x300")
    window.config(background = "White")

    label_file_explorer = Label(window,
                    text = "If the files have been selected, close this window",
                    width = 60, height = 4,
                    fg = "blue")

    button_explore = Button(window,
                        text = "Browse Files",
                        command = browse_files)
    
    button_folder = Button(window,
                        text = "Browse Folder",
                        command = open_directory)

    label_file_explorer.grid(column = 1, row = 1)
    button_explore.grid(column = 1, row = 2)
    button_folder.grid(column = 1, row = 3)

    window.mainloop()


def browse_files():
    filenames = filedialog.askopenfilenames(initialdir = "/mnt/c/Users/Raihan/Downloads/#Download Shit/temp",
                                          title = "Select MP3 File(s)",
                                          filetypes = (("MP3 File", "*.mp3*"),
                                                       ("all files", "*.*")))

    for x in filenames:
        __mp3_files.append(x)

def open_directory():
    directory = filedialog.askdirectory(initialdir = "/mnt/c/Users/Raihan/Downloads/#Download Shit/temp", title = "Select Folder")
    print("Opening Directory: \n    " + directory)

def set_mp3_files():
    init_file_explorer()

def get_mp3_files():
    set_mp3_files()
    return __mp3_files