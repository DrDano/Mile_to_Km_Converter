from tkinter import *

#Buttons
def action():
   print("I got clicked")


# Creating a new window and configurations
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=80, pady=200)

# Labels
label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
label.config(text="New Text")
label.grid(column=0, row=0)
label.config(padx=50, pady=50)

# calls action() when pressed
button = Button(text="Click Me", command=action)
button.grid(column=1, row=1)

# Button 2
button2 = Button(text="Click Me", command=action)
button2.grid(column=3, row=0)

# Entries
user_input = Entry(width=10)
print(user_input.get())
user_input.grid(column=4, row=4)

mainloop()
