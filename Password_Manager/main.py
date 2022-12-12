import json
from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip

LETTERS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
FONT = ("Arial", 12, "bold")
FONT_E = ("Arial", 12)
FONT_B = ("Arial", 10)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, END)
    l = [choice(LETTERS) for _ in range(randint(8, 10))]
    s = [choice(SYMBOLS) for _ in range(randint(2, 4))]
    n = [choice(NUMBERS) for _ in range(randint(2, 4))]
    password = l+s+n
    shuffle(password)
    password = "".join(password)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty.")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = new_data
        else:
            data.update(new_data)

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()


# ---------------------------- SEARCH ------------------------------- #

def find_password():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave the field empty")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            messagebox.showerror(title="Error", message="No Data File Found")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
            else:
                messagebox.showinfo(title="Oops", message="No details for this website exists")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

img = PhotoImage(file="./logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# LABELS

website_label = Label(text="Website:", font=FONT)
website_label.grid(row=1, column=0, padx=12, pady=5)

email_username_label = Label(text="Email/Username:", font=FONT)
email_username_label.grid(row=2, column=0, padx=12, pady=5)

password_label = Label(text="Password:", font=FONT)
password_label.grid(row=3, column=0, padx=12, pady=5)

# ENTRIES

website_entry = Entry(width=24, font=FONT_E)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_username_entry = Entry(width=38, font=FONT_E)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "karan@gmail.com")

password_entry = Entry(width=24, font=FONT_E)
password_entry.grid(row=3, column=1)

# BUTTONS

generate_button = Button(text="Generate Password", font=FONT_B, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=42, font=FONT_B, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

search_button = Button(text="Search", font=FONT_B, width=14, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
