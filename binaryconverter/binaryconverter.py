from tkinter import * 
#exit function
def click():
    entered_text = textentry.get()
    output.delete(0.0, END)
    binary = "".join(format(ord(x), "08b") for x in entered_text)
    output.insert(END, binary)
def close_window():
    window.destroy()
#window config
window = Tk()
window.title("Binary converter")
window.iconbitmap("binary.ico")
window.configure(background = "white", padx = "5", pady = "5")
window.resizable(0, 0)
#label
Label(window, text = "Enter anything you'd like to convert to binary notation.", bg="white", fg="black", font="none 12",).grid(row = 0, column = 0, sticky = W)
#text entry
textentry = Entry(window, width = 60, bg = "white", fg = "black")
textentry.grid(row = 1, column = 0, sticky = W)
#enter button
Label(window, text = "\n", bg="white", fg="black", font = "none 12").grid(row = 2, column = 0, sticky = W)
Button(window, text = "Enter", width = 6, command = click).grid(row = 2, column = 0, sticky = W)
#another label                      
Label(window, text = "Here is your text converted to binary notation. If necessary, use your scrollwheel to read the full text.", bg="white", fg="black", font = "none 12").grid(row = 3, column = 0, sticky = W)
#text box
output = Text(window, width = 75, height = 5, wrap = WORD, background = "white")
output.grid(row = 4, column = 0, columnspan = 2, sticky = W)
#exit
Label(window, text = "\n", bg="white", fg="black", font = "none 12").grid(row = 6, column = 0, sticky = W)
Button(window, text = "Exit", width = 6, command = close_window).grid(row = 6, column = 0, sticky = W)
window.mainloop()
