import os
from tkinter import Tk,filedialog,messagebox

Tk().withdraw()
folder=filedialog.askdirectory(title='Select a folder to change extensions')

walk = os.walk(folder)

messagebox.askquestion(title='Continue?',message='All jpg files inside will be changed to img files.\nContinue?')

for path,folders,files in walk:
    for file in files:
        root,ext = os.path.splitext(file)
        if ext == '.jpg':
            os.rename(os.path.join(path,file),os.path.join(path,root+'.img'))
        else:
            continue
        
