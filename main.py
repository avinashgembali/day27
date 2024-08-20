import tkinter


def button_clicked():
    print("button was clicked")
    label["text"] = "button got clicked!"
    print(inp.get())


window = tkinter.Tk()
window.title("my first GUI program.")
window.minsize(width=500, height=300)
window.config(padx=200, pady=200)

label = tkinter.Label(text="I am a label", font=("Courier", 24, "bold"))
label.grid(column=0, row=0)


label["font"] = ("Arial", 24, "italic")
# label.config(font=("Arial", 24, "italic")) another way of updating

button = tkinter.Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)


new_button = tkinter.Button(text="new button!")
new_button.grid(column=2, row=0)

inp = tkinter.Entry(width=10)
inp.grid(column=3, row=2)

window.mainloop()

# unlimited positional arguments (*args)
# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total
#
#
# print(add(1, 2, 3, 4))

# keyword arguments (*kwargs)
# class Bike:
#
#     def __init__(self, **kw):
#         self.company = kw.get("company")
#         self.cost = kw.get("cost")
#
#
# obj = Bike(company="ktm")
# print(obj.cost)
