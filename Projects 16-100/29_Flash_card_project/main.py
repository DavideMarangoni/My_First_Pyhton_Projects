from tkinter import *
from PIL import Image, ImageTk
import random as rd

# --------------------------------- CONSTANTS --------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 18, "italic")
WORD_FONT = ("Arial", 32, "bold")

# --------------- word list setup --------------- #

word_file_path = r"C:\Users\david\OneDrive\Desktop\PYTHON\Udemy\My_First_Pyhton_Projects\Projects 16-100\29_Flash_card_project\data\english_word.csv"
with open(file= word_file_path) as file:
    rows = file.readlines()
    rows_replace = [part.replace("\n", "") for part in rows[1:]]
    word_list = [part.split(",") for part in rows_replace]

# --------------------------------- FUNCTIONS SETUP --------------------------------- #

# --------------- random word --------------- #

def random_word():
    i = rd.randint(1,5000)
    return word_list[i][0]

# --------------------------------- GUI SETUP --------------------------------- #

win = Tk()
win.title("Flash Card")
win.config(bg= BACKGROUND_COLOR, padx= 30, pady= 30)

# --------------- Canvas setup --------------- #

# Card_front setup
original_card_front_img = Image.open(r"C:\Users\david\OneDrive\Desktop\PYTHON\Udemy\My_First_Pyhton_Projects\Projects 16-100\29_Flash_card_project\images\card_front.png")
resize_card_front_img = original_card_front_img.resize((400, 263))
tk_card_front_img = ImageTk.PhotoImage(resize_card_front_img)
canvas = Canvas(width= 500, height=300, highlightthickness=0, bg= BACKGROUND_COLOR)
canvas.create_image(250, 150, image = tk_card_front_img)
language_text = canvas.create_text(250, 70, text= "english", fill= "black", font= LANGUAGE_FONT)
word_text = canvas.create_text(250, 150, text= random_word(), fill= "black", font= WORD_FONT)
canvas.grid(column=1, row= 1, columnspan= 2)

# Card_back setup
# TODO - programming the card_back

# --------------- Button setup --------------- #

# x button setup
original_x_button_path = Image.open(r"C:\Users\david\OneDrive\Desktop\PYTHON\Udemy\My_First_Pyhton_Projects\Projects 16-100\29_Flash_card_project\images\wrong.png")
resize_x_button_img = original_x_button_path.resize((70, 70))
tk_x_button_img = ImageTk.PhotoImage(resize_x_button_img)
x_button = Button(image= tk_x_button_img, highlightthickness= 0)
x_button.grid(column = 1, row= 2)

# v_button setup
original_v_button_path = Image.open(r"C:\Users\david\OneDrive\Desktop\PYTHON\Udemy\My_First_Pyhton_Projects\Projects 16-100\29_Flash_card_project\images\right.png")
resize_v_button_img = original_v_button_path.resize((70, 70))
tk_v_button_img = ImageTk.PhotoImage(resize_v_button_img)
v_button = Button(image= tk_v_button_img, highlightthickness= 0)
v_button.grid(column= 2, row= 2)




win.mainloop()