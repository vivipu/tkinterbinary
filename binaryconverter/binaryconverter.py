from tkinter import * 
#exit function
def bindeci(binval):
    return int(binval, 2)
def click():
    numbers = "0123456789"
    entered_text = textentry.get()
    nums = 0
    bincount = 0
    out = ""
    for x in entered_text:
        if x in numbers:
            nums += 1
        if x == "0" or x == "1":
            bincount += 1
    output.delete(0.0, END)
    if nums != len(entered_text):
        out = "".join(format(ord(x), "08b") for x in entered_text)
    elif len(entered_text) == bincount:
        out = ''.join(chr(int(entered_text[i*8:i*8+8],2)) for i in range(len(entered_text)//8))
        test = "".join(format(ord(x), "08b") for x in out).replace("0b","")
        if not out or entered_text != test:
            arr = list(entered_text)
            out = int("".join([str(x) for x in arr]), 2)
    elif nums == len(entered_text) and nums != bincount:
        out = bin(int(entered_text)).replace("0b","")
    output.insert(END, out)
def close_window():
    window.destroy()
#window config
window = Tk()
window.title("Binary converter")
window.iconbitmap("binary.ico")
window.configure(bg = "#f7f5fb", padx = "5", pady = "5")
window.resizable(0, 0)
#labels
Label(window, text = "Enter anything you'd like to convert to or from binary notation.", bg="#f7f5fb", fg="#0a0908", font="none 12",).grid(row = 0, column = 0, sticky = W)
Label(window, text = "Integers are converted as integers, rather than in their string form.", bg="#f7f5fb", fg="#0a0908", font="none 12",).grid(row = 1, column = 0, sticky = W)
#text entry
textentry = Entry(window, width = 75, bg = "#f7f5fb", fg = "#0a0908")
textentry.grid(row = 2, column = 0, sticky = W)
#enter button
Label(window, text = "\n", bg="#f7f5fb", fg="#0a0908", font = "none 12").grid(row = 3, column = 0, sticky = W)
Button(window, text = "Convert", width = 8, command = click, relief = "flat", bg = "#457eac", fg = "#f7f5fb", borderwidth = "0", activebackground = "#457eac", activeforeground = "#f7f5fb").grid(row = 3, column = 0, sticky = W)
#another label                      
Label(window, text = "Here is your text converted to or from binary notation. Use your scrollwheel to read the full text.", bg="#f7f5fb", fg="#0a0908", font = "none 11").grid(row = 4, column = 0, sticky = W)
#text box
output = Text(window, width = 75, height = 5, wrap = WORD, bg = "#f7f5fb")
output.grid(row = 5, column = 0, columnspan = 2, sticky = W)
#exit
Label(window, text = "\n", bg="#f7f5fb", fg="#0a0908", font = "none 12").grid(row = 7, column = 0, sticky = W)
Button(window, text = "Quit", width = 8, command = close_window, relief = "flat", bg = "#ec7357", fg = "#f7f5fb", borderwidth = "0", activebackground = "#ec7357", activeforeground = "#f7f5fb").grid(row = 7, column = 0, sticky = W)
window.mainloop()