import tkinter as tk

def clear_fields():
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)

window = tk.Tk()
window.title("Data Entry")

first_name_label = tk.Label(window, text="First Name:")
first_name_label.grid(row=0, column=0)

first_name_entry = tk.Entry(window)
first_name_entry.grid(row=0, column=1)

last_name_label = tk.Label(window, text="Last Name:")
last_name_label.grid(row=1, column=0)

last_name_entry = tk.Entry(window)
last_name_entry.grid(row=1, column=1)

submit_button = tk.Button(window, text="Submit")
submit_button.grid(row=2, column=0)

clear_button = tk.Button(window, text="Clear", background="red", command=clear_fields)
clear_button.grid(row=2, column=1)

window.mainloop()
