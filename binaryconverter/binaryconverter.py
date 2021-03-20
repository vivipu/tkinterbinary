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
window.configure(background = "#f7f5fb", padx = "5", pady = "5")
window.resizable(0, 0)
#label
Label(window, text = "Enter anything you'd like to convert to binary notation.", bg="#f7f5fb", fg="#0a0908", font="none 12",).grid(row = 0, column = 0, sticky = W)
#text entry
textentry = Entry(window, width = 60, bg = "#f7f5fb", fg = "#0a0908")
textentry.grid(row = 1, column = 0, sticky = W)
#enter button
Label(window, text = "\n", bg="#f7f5fb", fg="#0a0908", font = "none 12").grid(row = 2, column = 0, sticky = W)
Button(window, text = "Enter", width = 6, command = click, relief = "flat", background = "#457eac", foreground = "#f7f5fb", borderwidth = "0", activebackground = "#457eac", activeforeground = "#f7f5fb").grid(row = 2, column = 0, sticky = W)
#another label                      
Label(window, text = "Here is your text converted to binary notation. If necessary, use your scrollwheel to read the full text.", bg="#f7f5fb", fg="#0a0908", font = "none 12").grid(row = 3, column = 0, sticky = W)
#text box
output = Text(window, width = 75, height = 5, wrap = WORD, background = "#f7f5fb")
output.grid(row = 4, column = 0, columnspan = 2, sticky = W)
#exit
Label(window, text = "\n", bg="#f7f5fb", fg="#0a0908", font = "none 12").grid(row = 6, column = 0, sticky = W)
Button(window, text = "Exit", width = 6, command = close_window, relief = "flat", background = "#ec7357", foreground = "#f7f5fb", borderwidth = "0", activebackground = "#ec7357", activeforeground = "#f7f5fb").grid(row = 6, column = 0, sticky = W)
window.mainloop()
