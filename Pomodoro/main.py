from math import floor
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    global check
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label1.config(text="Timer", fg=GREEN)
    label2.config(text="")
    reps = 0
    check = ""

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    work = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60
    if reps == 7:
        label1.config(text="Break", fg=RED)
        countdown(long_break)

    elif reps == 0 or reps % 2 == 0:
        reps += 1
        label1.config(text="Work", fg=GREEN)
        countdown(work)
    else:
        reps += 1
        label1.config(text="Break", fg=PINK)
        countdown(short_break)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_min = floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        global check
        if reps % 2 != 0:
            check += "✔"
            label2.config(text=check)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label1 = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
label1.grid(row=0, column=1)

img = PhotoImage(file="./tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 10), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 10), highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

label2 = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16))
label2.grid(row=3, column=1)

window.mainloop()
