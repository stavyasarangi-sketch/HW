import tkinter as tk

def calculate_area():
    length_value = float(length_entry.get())
    width_value = float(width_entry.get())
    area_result = length_value * width_value
    result_label.config(text="Area: " + str(area_result) + " sq units")

window = tk.Tk()
window.title("Area Calculator")

length_label = tk.Label(window, text="Length:")
length_label.grid(row=0, column=0)

length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1)

width_label = tk.Label(window, text="Width:")
width_label.grid(row=1, column=0)

width_entry = tk.Entry(window)
width_entry.grid(row=1, column=1)

calculate_button = tk.Button(window, text="Calculate Area", background="orange", command=calculate_area)
calculate_button.grid(row=2, column=0)

result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0)

window.mainloop()
