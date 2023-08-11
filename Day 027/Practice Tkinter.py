import tkinter

window = tkinter.Tk()
window.title("First tkinter program")
window.minsize(500, 500)

#Label

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

window.mainloop()
