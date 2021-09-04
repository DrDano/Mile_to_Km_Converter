from tkinter import *


# Button Action
def action():
    conversion = int(1.609) * user_input.get()
    return conversion


# Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)

user_input = Entry(width=10)
print(user_input.get())
user_input.grid(column=1, row=0)

button_text = action

# Labels
label = Label(text="is equal to", font=("Arial", 12, "normal"))
label.grid(column=0, row=1)
label.config(padx=20)

# Labels
label2 = Label(text="Km", font=("Arial", 12, "normal"))
label2.grid(column=2, row=1)
label2.config(padx=20)

# Labels
label3 = Label(text="Miles", font=("Arial", 12, "normal"))
label3.grid(column=2, row=0)

# Labels
label4 = Label(text=button_text, font=("Arial", 12, "normal"))
label4.grid(column=1, row=1)

# Button
button = Button(text="Calculate", command=action)
button.grid(column=1, row=2)


window.mainloop()

