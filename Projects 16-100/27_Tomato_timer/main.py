from tkinter import *
from PIL import Image, ImageTk   # Pillow library
import pygame

pygame.init()             # inizializza tutti i moduli pygame
pygame.mixer.init()       # inizializza esplicitamente il mixer (facoltativo ma consigliato)

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#eFDAB9E"
RED = "#E50046"
GREEN = "#C6D870"
YELLOW = "#FFF0BD"
BLUE = "#3396D3"
ORANGE = "#FF9A00"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TOMATO_REPS = 1
CHECK_NUMBER = 0
timer = None
timer_passed = 0

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global TOMATO_REPS, CHECK_NUMBER
    window.after_cancel(timer)
    window.config(bg=YELLOW)
    timer_word.config(text="Timer", bg= YELLOW)
    canvas.itemconfig(timer_text, text="25:00")
    canvas.config(bg=YELLOW)
    check.config(text="", bg= YELLOW)
    TOMATO_REPS = 1
    CHECK_NUMBER = 0

# ---------------------------- TIMER BREAK ----------------------------------- #

def timer_break():

    global is_break

    is_break = True
    window.after_cancel(timer)
    timer_word.config(text= "Pause", bg=YELLOW)
    canvas.config(bg=YELLOW)
    check.config(bg=YELLOW)
    window.config(bg= YELLOW)

def timer_play():

    global timer_passed

    timer_word.config(text="Work", bg=BLUE)
    canvas.config(bg=BLUE)
    check.config(bg=BLUE)
    window.config(bg=BLUE)

    count_down(timer_passed)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global TOMATO_REPS, CHECK_NUMBER

    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if TOMATO_REPS % 2 != 0 and TOMATO_REPS != 1:
        symbol = "✔" * CHECK_NUMBER
        check.config(text= symbol)

    if TOMATO_REPS % 8 == 0 and TOMATO_REPS != 0:  # long break ogni 8 cicli
        timer_word.config(text="Break", bg= BLUE)
        window.config(bg=BLUE)
        canvas.config(bg=BLUE)
        check.config(bg=BLUE)
        count_down(long_break)

    elif TOMATO_REPS % 2 == 0:  # short break nei cicli pari
        timer_word.config(text="Break", bg= BLUE)
        window.config(bg=BLUE)
        canvas.config(bg=BLUE)
        check.config(bg=BLUE)
        count_down(short_break)

    else:  # work nei cicli dispari
        timer_word.config(text="Work", bg=GREEN)
        window.config(bg=GREEN)
        canvas.config(bg=GREEN)
        check.config(bg=GREEN)
        CHECK_NUMBER += 1
        count_down(work_time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

sveglia_sound = pygame.mixer.Sound("sveglia_sound.mp3")
def count_down(count):
    global TOMATO_REPS, timer_passed

    timer_passed = count

    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        sveglia_sound.play()
        TOMATO_REPS += 1
        window.after(1000, start_timer)

    return timer_passed


# ---------------------------- GUI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer App")
window.config(padx= 80, pady= 80, bg= YELLOW)

# Timer Word SETUP
timer_word = Label(text="Timer", fg= "green" , font= (FONT_NAME, 60, "bold"), bg= YELLOW)
timer_word.grid(column=4, row= 1)

# Tomato and Canvas SETUP
original_img = Image.open("tomato2.png") # import the original image
resize_image = original_img.resize((300, 300)) #resize the image
tk_img = ImageTk.PhotoImage(resize_image) # create a Tkinter compatible image
canvas = Canvas(width=310, height= 310, bg= YELLOW, highlightthickness= 0) #Creating the canva that contains image
canvas.create_image(0, 0, image=tk_img , anchor="nw")
timer_text = canvas.create_text(150, 170, text="25:00", font= (FONT_NAME, 37, "bold"), fill= "white")
canvas.grid(column=4, row= 2)

# check label SETUP
check = Label(font= (FONT_NAME, 12), fg= RED, bg= YELLOW)
check.place(x=20, y=460)

# start button setup
start_button = Button(text="Start", font= (FONT_NAME, 13, "bold"), fg= "white", bg= "green", command= start_timer)
start_button.grid(column= 1, row= 3)

# Reset button SETUP
reset_button = Button(text= "Reset", font= (FONT_NAME, 13, "bold"), fg="white", bg= "green", command= reset_timer)
reset_button.grid(column=7, row=3)

break_button = Button(text="⏸", font= (FONT_NAME, 13), bg= "green", fg= "white", command= timer_break)
break_button.place(x=170, y=408)

play_button = Button(text="▶", font= (FONT_NAME, 13), bg= "green", fg= "white", command= timer_play)
play_button.place(x=220, y=408)

window.mainloop()