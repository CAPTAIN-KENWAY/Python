from tkinter import *


def m_to_km():
    miles = float(input.get())
    km = miles*1.609
    km = round(km, 2)
    label3.config(text=f"{km}")


window = Tk()
window.geometry("350x200")
window.resizable(0, 0)
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)

input = Entry(highlightthickness=2, font=("Arial", 14), width=8)
input.config(highlightbackground="lightblue", highlightcolor="lightblue")
input.grid(row=0, column=1, padx=10, pady=10)

label1 = Label(text="Miles", font=("Arial", 14))
label1.grid(row=0, column=2, padx=10, pady=10)

label2 = Label(text="is equal to", font=("Arial", 14))
label2.grid(row=1, column=0, padx=10, pady=10)

label3 = Label(text="0", font=("Arial", 14))
label3.grid(row=1, column=1, padx=10, pady=10)

label4 = Label(text="Km", font=("Arial", 14))
label4.grid(row=1, column=2, padx=10, pady=10)

button = Button(text="Calculate", font=("Arial", 14), command=m_to_km)
button.grid(row=2, column=1, padx=10, pady=10)

window.mainloop()
