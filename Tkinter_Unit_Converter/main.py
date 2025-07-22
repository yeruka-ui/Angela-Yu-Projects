from tkinter import *

window = Tk()

window.title("Miles to Km Converter")
window.minsize(200, 100)
window.config(padx = 20, pady = 20)

def click_button():
    entered_txt = float(miles_input.get())
    output_label.config(text = entered_txt * 1.60934)

def clear(event):
    if miles_input.get() == "0":
        miles_input.delete(0, END)

# Entry
miles_input = Entry(width= 10)
miles_input.insert(0, "0")
miles_input.grid(column = 1, row = 0)
miles_input.bind("<FocusIn>", clear)

#Miles Label
my_label = Label(text = f"Miles")
my_label.grid(column = 2, row = 0)

#Equal to Label
equal_to_label = Label(text =f"is equal to")
equal_to_label.grid(column = 0, row = 1)

#Conversion Label
output_label = Label(text = f"0")
output_label.grid(column = 1, row = 1)

#Km Label
km_label = Label(text = f"Km")
km_label.grid(column = 2, row = 1)

# Calculate Button Widget
button = Button(text = "Calculate", command = click_button)
button.grid(column = 1, row = 2)


window.mainloop()