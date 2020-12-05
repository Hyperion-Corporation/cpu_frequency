#!/usr/bin/python3

import subprocess
from tkinter import *

def architecture():
	output = subprocess.check_output('lscpu')
	output = str(output.split()[1])
	output = output.split("'")[1]
	lbl.configure(text=output)

def processor_vendor():
	output = subprocess.check_output('lscpu')
	output = str(output.split()[39])
	output = output.split("'")[1]
	lbl.configure(text=output)

def processor_model():
	output = subprocess.check_output('lscpu')
	output = output.split()
	vendor = output[47]
	model = output[48]
	code = output[49]
	vendor = str(vendor)
	model = str(model)
	code = str(code)
	vendor = vendor.split("'")[1]
	model = model.split("'")[1]
	code = code.split("'")[1]
	final = vendor, model, code
	lbl.configure(text=final)

def cpu_max_mhz():
	output = subprocess.check_output('lscpu')
	output = output.split()[61]
	output = str(output)
	output = output.split("'")[1]
	output = output, "MHz"
	lbl.configure(text=output)

# Window settings

window = Tk()
window.title("CPU Information")
window.geometry("300x150")

# Text label

lbl = Label(window, text="")
lbl.grid(column=0, row=0)

# Buttons

btn = Button(window, text="Architecture", command=architecture)
btn.grid(column=1, row=0)

btn2 = Button(window, text="Processor Vendor", command=processor_vendor)
btn2.grid(column=1, row=1)

btn3 = Button(window, text="Processor Model", command=processor_model)
btn3.grid(column=1, row=2)

btn4 = Button(window, text="CPU Max frequency", command=cpu_max_mhz)
btn4.grid(column=1, row=3)

window.mainloop()
