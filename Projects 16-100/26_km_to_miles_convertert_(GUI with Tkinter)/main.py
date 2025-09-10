from tkinter import *

# Button functions
def on_click():
    user_text = user_input_box.get()
    my_label.config(text=user_text)
    my_label.grid(column=0, row=0)

window = Tk() #inizializzo l'oggetto window

# Screen setup
window.title("My first GUI program") # Titolo della finestra
window.minsize(width=500, height= 300) # Grandezza della finestra
window.config(padx= 100, pady= 200, bg= "pink")

# Label setup
my_label = Label(font= ("Arial", 18))
my_label.config(text="Write something in the box below")
my_label.grid(column= 0, row= 0)
my_label.config(padx=10, pady= 10)

# Input setup
user_input_box = Entry(width= 30)
user_input_box.insert(END, string="Some text to begin with.") # Writing some text into the text box
user_input_box.grid(column= 4, row= 4)

# Button setup
button = Button(text="Click me", command= on_click, font= ("Arial", 12), bg="light blue")
button.grid(column= 2, row= 2)

# Button 1 setup
button1 = Button(text="second", font= ("Arial", 12), bg="light green")
button1.grid(column=3, row= 0)


window.mainloop()