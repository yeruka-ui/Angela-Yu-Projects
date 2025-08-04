from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
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
    new_data = {website: {
        "email": email,
        "password": password
    }}

    if not website or not email or not password:
        messagebox.showwarning("Warning", "Please provide all the required information.")
    else:
        try:
            with open ("data.json", "r") as f:
                data = json.load(f) #Reading old data
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)  # Updating old data with new data

            with open("data.json", "w") as f:
                json.dump(data, f, indent=4) #Save the file in JSON
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

        messagebox.showinfo("CloseBox", "Your details have been saved.")

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showwarning("Warning: No Information", "No details for this website exists.")
    else:
        if website in data:
            email_find = data[website]["email"]
            password_find = data[website]["password"]
            messagebox.showinfo("Information", f"Website: {email_find} \nPassword: {password_find}")
        else:
            messagebox.showwarning("Warning: No account", f"The details for that {website} does not exist.")
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)

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
website_entry = Entry(width= 29)
website_entry.grid(column = 1, row = 1)
website_entry.focus()

# Email Entry:
email_entry = Entry(width= 44)
email_entry.grid(column = 1, row = 2, columnspan = 2)
email_entry.insert(0,"laurenkailey05@gmail.com")

# Password Entry:
password_entry = Entry(width= 29)
password_entry.grid(column = 1, row = 3)

# Generate Button
password_generate = Button(text= "Generate", width=11, command= generate_password)
password_generate.grid(column = 2, row = 3, sticky="w")

# Add Button
add_button = Button(text= "Add", width=40, command = save_information)
add_button.grid(column = 1, row = 4, columnspan = 2)

# Generate Button
search_button = Button(text= "Search", width=11, command= find_password)
search_button.grid(column = 2, row = 1, sticky="w")


window.mainloop()