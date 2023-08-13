from tkinter import *

window = Tk()
window.title("First tkinter program")
window.minsize(500, 500)

# Label

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New text"
my_label.config(text="Click the button")

# Button
def button_clicked():
    my_label.config(text=input.get())


button = Button(text="Click here", command=button_clicked)
button.pack()

# Entry

input = Entry(width=10)
input.pack()


window.mainloop()
