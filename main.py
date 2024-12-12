import tkinter as tk
from tkinter import ttk

# ?Window config

app = tk.Tk()
app.resizable(False, False)
app.title("Folderly")
window_width = 1000
window_height = 800

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

app.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
app.iconbitmap('./Assets/icon.ico')

# ?General

    # *Title

titleFrame = ttk.Frame(app, width=window_width)
title = ttk.Label(titleFrame, text="Folderly", font=("Arial", 20), background='red', anchor='center', justify='center')
titleFrame.pack(side="top", fill="both")
title.pack(side="top", fill="both")

    # *Subframes

appFrame = ttk.Frame(app, width=window_width, height=window_height-titleFrame.winfo_height())
left = ttk.Frame(appFrame)
right = ttk.Frame(appFrame)
appFrame.pack(side="top", expand=True, fill="both")
left.pack(side="left", expand=True, fill="both")
right.pack(side="right", expand=True, fill="both")

# ?Left

    # *Open Folder

def open_folder():
    pass

folder_button = ttk.Button(left, text="Select Folder", command=open_folder, width=20)
folder_button.pack(side="top")

    # *Open Exceptions

def open_exceptions():
    pass

exception_button = ttk.Button(left, text="Select Exceptions", command=open_exceptions, width=20)
exception_button.pack(side="top")
    
    # *Caracteristics Frame

caracteristicsFrame = ttk.Frame(left, border=1, relief="solid")
caracteristicsFrame.pack(side="top", expand=True, fill="both")
lbl = ttk.Label(caracteristicsFrame, text="Caracteristics", font=("Arial", 20), background='blue', anchor='center', justify='center')
lbl.pack(side="top", expand=True, fill="both")

# ?Right

    # *Download Button

def download():
    pass

download_button = ttk.Button(right, text="Download", command=download, width=20)
download_button.pack(side="top")

    # *Scheme Frame

schemeFrame = ttk.Frame(right, border=1, relief="solid")
schemeFrame.pack(side="top", expand=True, fill="both")
lbl2 = ttk.Label(schemeFrame, text="Scheme", font=("Arial", 20), background='green', anchor='center', justify='center')
lbl2.pack(side="top", expand=True, fill="both")

# ?Start App

app.mainloop()