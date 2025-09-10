from tkinter import *
from tkinter import messagebox
import random as rd
from PIL import Image, ImageTk
import pyperclip
import json
# ---------------------------- CONSTANTS ------------------------------- #

PASSWORD_ELEMENTS = {
    "letters": ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    "numbers": ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    "symbols": ['!', '#', '$', '%', '&', '(', ')', '*', '+']
}

# ---------------------------- SEARCH WEBSITE ------------------------------- #

def search_website():

    website = website_entry.get()
    if not website:
        messagebox.showinfo(title= "Ops", message= "Website box can't be empty")
    else:
        with open("password_saved.json", mode= "r") as file:
            data = json.load(file)
        try:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title = website, message= f"Email: {email}\n"
                                                          f"Password: {password}")
        except KeyError:
            messagebox.showinfo(title= "Ops", message= "The website you wrote doesn't exist ")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def random_pass():
    
    global PASSWORD_ELEMENTS
    password_gen = []
    password_join = ""

    password_entry.delete(0, "end")

    for i in range(rd.randint(16,20)):

        key = rd.choice(list(PASSWORD_ELEMENTS.keys()))
        new_value = rd.choice(PASSWORD_ELEMENTS[key])
        password_gen.append(new_value)

    password_join = "".join(password_gen)
    password_entry.insert(0, string=password_join)
    pyperclip.copy(password_join)

    messagebox.showinfo(title= "copied", message= "The password has been copy")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title= "Error", message= "There can't be empty boxes, please check")
    else:

        is_ok = messagebox.askokcancel(title= "Password Manager", message= f""f"Username: {email}\n"
                                                                           f"Password: {password}\n\n"
                                                                           f"Do you want to proceed?")

        if is_ok:

            try:
                with open("password_saved.json", mode= "r") as file:
                    # reading old data
                    data = json.load(file)

            except FileNotFoundError:
                with open("password_saved.json", mode = "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                # updating old data with new data
                data.update(new_data)

                # saving new data
                with open("password_saved.json", mode= "w") as file:
                    json.dump(data, file, indent= 4)

            finally:
                messagebox.showinfo(title="Notification", message="The credentials has been saved")
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #

# window setup
window = Tk()
window.title("Password manager")
window.config(pady=70, padx=70, bg= "white")

# image setup
original_image = Image.open("logo.png")
resize_image = original_image.resize((200, 189))
tk_img = ImageTk.PhotoImage(resize_image)

# canvas setup
canvas = Canvas(width=200, height=200, bg= "white", highlightthickness=0)
canvas.create_image(100, 100, image= tk_img)
canvas.grid(column= 2, row= 1)

# Text Label Setup
website_text = Label(text= "Website:", bg= "white", fg= "black")
website_text.grid(column= 1, row= 2)

email_username_text = Label(text= "Email/Username:", bg= "white", fg= "black")
email_username_text.grid(column= 1, row= 3)

password_text = Label(text= "Password:", bg= "white", fg= "black")
password_text.grid(column= 1, row= 4)

# Entry Label setup

website_entry = Entry(width= 32, bg= "white")
website_entry.focus()
website_entry.grid(column= 2, row= 2)

username_entry = Entry(width= 45, bg= "white")
username_entry.insert(0,"davide.marangoni18@gmail.com")
username_entry.grid(column= 2, row= 3, columnspan= 2)

password_entry = Entry(width= 32, bg= "white")
password_entry.grid(column= 2, row= 4)

# Button Setup

pass_gen_button = Button(text= "Generate", bg= "white", fg= "black", borderwidth= 1, relief= "sunken", width= 9, command= random_pass)
pass_gen_button.grid(column = 3, row= 4)

search_button = Button(text= "Search", bg= "white", fg= "black", borderwidth= 1, relief= "sunken", width= 9, command= search_website)
search_button.grid(column = 3, row= 2)

add_button = Button(text= "Add", bg= "white", fg= "black", borderwidth= 1, width= 38, relief= "sunken", command= save, pady= 3)
add_button.grid(column = 2, row= 5, columnspan= 2)

window.mainloop()
