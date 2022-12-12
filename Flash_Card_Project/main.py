from tkinter import *
import pandas
from random import choice
BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
data_list = data.to_dict(orient="records")


def flip_card():
    canvas.itemconfig(flash_image, image=card_back)
    canvas.itemconfig(flash_language, text="English", fill="white")
    canvas.itemconfig(flash_word, text=current_card["English"], fill="white")


def change_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(data_list)
    word = current_card["French"]
    canvas.itemconfig(flash_image, image=card_front)
    canvas.itemconfig(flash_word, text=word, fill="black")
    canvas.itemconfig(flash_language, text="French", fill="black")
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    data_list.remove(current_card)
    df = pandas.DataFrame(data_list)
    df.to_csv("./data/words_to_learn.csv", index=False)
    change_word()


# UI SETUP
window = Tk()
window.title("flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# FLASH CARD
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_image = canvas.create_image(400, 263, image=card_front)
flash_language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
flash_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# BUTTONS
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0,
                      borderwidth=0, command=change_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0,
                      borderwidth=0, command=is_known)
right_button.grid(row=1, column=1)


change_word()
window.mainloop()
