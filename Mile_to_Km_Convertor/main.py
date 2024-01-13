from tkinter import *
from tkinter import messagebox

def Button_clicked():
	try:
		value = float(input.get())
		if value < 0:
			messagebox.showerror("Invalid input", "Please enter a positive number")
		elif conversion_type.get() == "miles_to_km":
			converted = round(value * 1.60934, 3)
		else:
			converted = round(value / 1.60934, 3)
		messagebox.showinfo("Result", f"The converted value is {converted}")
	except ValueError:
		messagebox.showerror("Invalid input", "Please enter a valid number")
window = Tk()
window.title("Distance Convertor")
window.geometry('400x150')
window.config(padx=20, pady=20)

Label(text="Enter distance:").grid(column=0, row=1)
input = Entry(width=7)
input.insert(0, "0")  # default value
input.grid(column=1, row=1)

Label(text="Choose conversion type:").grid(column=0, row=2)
conversion_type = StringVar()
conversion_type.set("miles_to_km")  # default value
Radiobutton(text="Miles to Km", variable=conversion_type, value="miles_to_km").grid(column=1, row=2)
Radiobutton(text="Km to Miles", variable=conversion_type, value="km_to_miles").grid(column=2, row=2)

Button(text="Calculate", command=Button_clicked).grid(column=1, row=3)

window.mainloop()