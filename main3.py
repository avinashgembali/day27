from tkinter import *


def calc_miles_to_km():
    num = float(miles_inp.get())
    answer = int(num * 1.60934)
    km_label["text"] = f"          {answer}     km"


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=50)
window.config(padx=50, pady=50)

label = Label(text="is equal to")
label.grid(column=0, row=2)

miles_inp = Entry(width=10)
miles_label = Label(text="Miles")
miles_label.grid(column=4, row=1)
miles_inp.grid(column=3, row=1)

km_label = Label(text="          0     km")
km_label.grid(column=3, row=2)

cal_button = Button(text="calculate", command=calc_miles_to_km)
cal_button.grid(column=3, row=3)

window.mainloop()

