import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    data_to_save = f"{website_entry} | {email_entry} | {password_entry}"
    with open("data.txt", "a") as data:
        data.write(data_to_save)
# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
locker_img = tk.PhotoImage(file="logo.png")

canvas.create_image(100, 110, image=locker_img)
canvas.grid(column=1, row=0)

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = tk.Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = tk.Entry(width=53)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = tk.Entry(width=53)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "your@email.com")
password_entry = tk.Entry(width=34)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = tk.Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)
add_button = tk.Button(text="Add", width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2)






window.mainloop()