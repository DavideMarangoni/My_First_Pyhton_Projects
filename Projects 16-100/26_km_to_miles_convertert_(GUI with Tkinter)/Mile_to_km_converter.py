from tkinter import *

#converter function
def converter():
    km = float(miles_input_box.get())
    miles = (km / 1.609).__round__(2)
    convert_label.config(text=miles)
    convert_label.grid(column=2, row=2)


# Screen setup
window = Tk()
window.title("Km to miles converter") # Titolo della finestra
window.minsize(width=250, height= 150) # Grandezza della finestra
window.config(padx= 20, pady= 20, bg= "white")

# Input Box setup
miles_input_box = Entry(width= 10)
miles_input_box.insert(END, string="0") # Writing some text into the text box
miles_input_box.config(font= ("Arial", 12))
miles_input_box.grid(column= 2, row= 0)

# Miles Label setup
miles_write = Label(font= ("Arial", 12))
miles_write.config(text="miles", bg= "white")
miles_write.grid(column=3, row=0)

# is_equal_to setup
is_equal_to = Label(font= ("Arial", 12))
is_equal_to.config(text="is equal to", bg= "white")
is_equal_to.grid(column=1, row=2)

# Converter label setup
convert_label = Label(font= ("Arial", 12), bg= "white", fg= "black")
convert_label.config(text="0")
convert_label.grid(column=2, row=2)

# "km" Label setup
km_write = Label(font= ("Arial", 12))
km_write.config(text="km", bg= "white")
km_write.grid(column=3, row=2)

# Button setup
button = Button(text="Calculate", command= converter, font=("Arial", 12), border=3 , bg= "white")
button.grid(column= 2, row= 3)

window.mainloop()
