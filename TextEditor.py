from tkinter import *
from tkinter import filedialog

filepath = None

def openFile():
    global filepath
    filepath = filedialog.askopenfilename(initialdir="C:\\Users",
                                          title="Open text file",
                                          filetypes= (("text files","*.txt"),
                                          ("all files","*.*")))
    
    file = open(filepath, 'r')
    content = str(file.read())
    text.insert(1.0, chars=content)
    file.close()

def saveAsFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0,END))
    file.write(filetext)
    file.close()

def saveFile():
    if filepath is None:
        saveAsFile()
    else:
        file = open(filepath, 'w')
        file.write(str(text.get(1.0, END)))
        file.close()



window = Tk()
window.title("Manan's Notepad")
window.geometry("600x420")
window.config(bg="brown")

open_btn = Button(window,
                  text="Open File",
                  command=openFile,
                  bd=6,)

save_btn = Button(window,
                  text="Save",
                  command=saveFile,
                  bd=6)

save_as_btn = Button(window,
                  text="Save As",
                  command=saveAsFile,
                  bd=6)

text = Text(window,
            bg="light yellow",
            font=("Arial",12),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="black")

open_btn.grid(row=0, column=0, padx=5, pady=5)
save_btn.grid(row=0, column=1, padx=5, pady=5)
save_as_btn.grid(row=0, column=2, padx=5, pady=5)
text.grid(row=1, column=0, columnspan=4, sticky="nsew")

# Configure row and column weights to make the Text widget expand
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(3, weight=1)

window.mainloop()