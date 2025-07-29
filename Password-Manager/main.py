from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = (([choice(letters) for char in range(randint(8, 10))] +
                     [choice(symbols) for char in range(randint(2, 4))]) +
                     [choice(numbers) for char in range(randint(2, 4))])

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_information():
    website =   website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website or not email or not password:
        messagebox.showwarning("Warning", "Please provide all the required information.")
    else:
        is_ok = messagebox.askokcancel(title= website, message= f"These are the details entered: \nE-mail: {email} \nPassword: {password} \n"
                                                        f"Is the information provided correct?")
        if is_ok:
            with open ("data.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo("CloseBox", "Your details have been saved.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx= 40, pady= 40)

canvas = Canvas(width= 200, height= 200, highlightthickness= 0)
canvas_image = PhotoImage(file= "logo.png")
canvas.create_image(100, 100, image = canvas_image)
canvas.grid(column = 1, row = 0)

# Website Label:
website_label = Label(text = "Website: ")
website_label.grid(column = 0, row = 1, )

# Email/Username Label:
user_label = Label(text = "Email/Username: ")
user_label.grid(column = 0, row = 2)

# Password Label:
password_label = Label(text = "Password: ")
password_label.grid(column = 0, row = 3)

# Website Entry:
website_entry = Entry(width= 48)
website_entry.grid(column = 1, row = 1, columnspan = 2)
website_entry.focus()

# Email Entry:
email_entry = Entry(width= 48)
email_entry.grid(column = 1, row = 2, columnspan = 2)
email_entry.insert(0,"laurenkailey05@gmail.com")

# Password Entry:
password_entry = Entry(width= 29)
password_entry.grid(column = 1, row = 3)

# Generate Button
password_generate = Button(text= "Generate Password", width=15, command= generate_password)
password_generate.grid(column = 2, row = 3, sticky="w")

# Add Button
add_button = Button(text= "Add", width=40, command = save_information)
add_button.grid(column = 1, row = 4, columnspan = 2)


window.mainloop()