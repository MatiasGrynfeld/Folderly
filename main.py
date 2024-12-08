import tkinter as tk
from tkinter import ttk
# Window config
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

# Frames

titleFrame = ttk.Frame(app, width=window_width)
appFrame = ttk.Frame(app, width=window_width, height=window_height-titleFrame.winfo_height())

# Widgets

title = ttk.Label(titleFrame, text="Folderly", font=("Arial", 20), background='red', anchor='center', justify='center')
label = ttk.Label(appFrame, text="Hello World", font=("Arial", 20), background='blue', anchor='center', justify='center')

# Object placement

titleFrame.pack(side="top", fill="both")
appFrame.pack(side="top", expand=True, fill="both")
title.pack(side="top", fill="both")
label.pack(side="top", expand=True, fill="both")
# Start App
app.mainloop()