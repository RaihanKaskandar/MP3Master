from tkinter import *
from tkinter import filedialog

def initFileExplorer():
    window = Tk()
    window.title('File Explorer')
    window.geometry("500x300")
    window.config(background = "White")

    label_file_explorer = Label(window,
                            text = "File Explorer using Tkinter",
                            width = 60, height = 4,
                            fg = "blue")

    button_explore = Button(window,
                        text = "Browse Files",
                        command = browseFiles)
    
    button_folder = Button(window,
                        text = "Browse Folder",
                        command = openDirectory)

    button_exit = Button(window,
                     text = "Exit",
                     command = exit)

    label_file_explorer.grid(column = 1, row = 1)
    button_explore.grid(column = 1, row = 2)
    button_folder.grid(column = 1, row = 3)
    button_exit.grid(column = 1, row = 4)

    window.mainloop()


def browseFiles():                                                   
    filenames = filedialog.askopenfilenames(initialdir = "/mnt/c/Users/Raihan/Music",
                                          title = "Select MP3 File(s)",
                                          filetypes = (("MP3 File",
                                                        "*.mp3*"),
                                                       ("all files",
                                                        "*.*")))

    print("Opening file(s): ")
    for x in filenames:
        print("     " + x)


def openDirectory():
    directory = filedialog.askdirectory(initialdir = "/mnt/c/Users/Raihan/Music", title = "Select Folder")
    print("Opening Directory: \n    " + directory)