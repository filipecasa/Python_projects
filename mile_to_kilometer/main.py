import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
# window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

label = tk.Label(text="is equal to")
label.grid(column=0, row=1)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1)

result_label = tk.Label(text=0)
result_label.grid(column=1, row=1)

def miles_to_km():
    new_text = input.get()
    result_label.config(text=round(float(new_text) * 1.609, 1))

button = tk.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

input = tk.Entry(width=5)
input.grid(column=1, row=0)

window.mainloop()