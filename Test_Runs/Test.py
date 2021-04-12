# importing all files  from tkinter
from tkinter import *
from tkinter import ttk
import json

# import only asksaveasfile from filedialog
# which is used to save file in any extension
from tkinter.filedialog import asksaveasfile

root = Tk()
root.geometry('200x150')


# function to call when user press
# the save button, a filedialog will
# open and ask to save file
def save():
    files = [('JSON Files', '*.json'),
             ('All Files', '*.*')]
    file = asksaveasfile(filetypes=files, defaultextension=files)
    json_obj = json.dumps(dict, indent=4)
    if file is None:
        return
    file.write(json_obj)
    file.close()


btn = ttk.Button(root, text='Save', command=save)
btn.pack(side=TOP, pady=20)

mainloop()