from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    user = user_entry.get()
    passwords = password_entry.get()

    if len(website) == 0 or len(passwords) == 0:
        messagebox.showinfo(title="Oops", message="There are blank fields!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {user} "
                                                              f"\nPassword: {passwords} \nIs it ok to save?")
        if is_ok:
            with open("Day29data.txt", "a") as data_file:
                data_file.write(f"{website} | {user} | {passwords}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="Day29Logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_label = Label()
website_label.config(text="Website:")
website_label.grid(row=1, column=0)
user_label = Label()
user_label.config(text="Email/Username:")
user_label.grid(row=2, column=0)
password_label = Label()
password_label.config(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry()
website_entry.config(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
user_entry = Entry()
user_entry.config(width=35)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, "test.com")
password_entry = Entry()
password_entry.config(width=21)
password_entry.grid(row=3, column=1)

password_button = Button()
password_button.config(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)
add_button = Button()
add_button.config(text="Add", width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
