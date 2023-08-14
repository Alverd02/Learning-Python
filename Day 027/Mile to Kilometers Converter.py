from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=25, pady=25)

miles_input = Entry(width=8)
miles_input.grid(column=1, row=0)

kilometer_output = Label(text="0")
kilometer_output.grid(column=1, row=1)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

Km = Label(text="Km")
Km.grid(column=2, row=1)


def converter():
    km = float(miles_input.get()) * 1.609344
    kilometer_output["text"] = f"{round(km,2)}"


calculate = Button(text="Calculate", command=converter)
calculate.grid(column=1, row=2)

window.mainloop()
