from tkinter import *

root = Tk()
root.geometry("300x270")
root.title("Calculator 2.0")

def type_value(value):
	display.insert(END,value)

def clear_display():
	display.delete(0,END)

def check_type():
	from_display = display.get()
	for x in from_display:
		try:
			if x == "+":
				a,b = from_display.split("+")
				total = int(a)+int(b)
				clear_display()
				type_value(total)
			if x == "-":
				a,b = from_display.split("-")
				total = int(a)-int(b)
				clear_display()
				type_value(total)
			if x == "*":
				a,b = from_display.split("*")
				total = int(a)*int(b)
				clear_display()
				type_value(total)
			if x == "/":
				#Doesnt return decimals
				a,b = from_display.split("/")
				total = int(a)/int(b)
				clear_display()
				type_value(int(total))

		except:
			clear_display()
			type_value("You broke it... :(")

display = Entry(root, font=("Calibri",20))

btn_0 = Button(root, text="0", command=lambda: type_value("0"))
btn_1 = Button(root, text="1", command=lambda: type_value("1"))
btn_2 = Button(root, text="2", command=lambda: type_value("2"))
btn_3 = Button(root, text="3", command=lambda: type_value("3"))
btn_4 = Button(root, text="4", command=lambda: type_value("4"))
btn_5 = Button(root, text="5", command=lambda: type_value("5"))
btn_6 = Button(root, text="6", command=lambda: type_value("6"))
btn_7 = Button(root, text="7", command=lambda: type_value("7"))
btn_8 = Button(root, text="8", command=lambda: type_value("8"))
btn_9 = Button(root, text="9", command=lambda: type_value("9"))

btn_c = Button(root, text="Clear", command=clear_display)
btn_sum = Button(root, text="+", command=lambda: type_value("+"))
btn_sub = Button(root, text="-", command=lambda: type_value("-"))
btn_mul = Button(root, text="*", command=lambda: type_value("*"))
btn_div = Button(root, text="/", command=lambda: type_value("/"))

btn_result = Button(root, text="=", command=check_type)


display.place(x=20, y=20, width=260, height=50)

btn_1.place(x=20,y=100, width=50, height=50)
btn_2.place(x=70,y=100, width=50, height=50)
btn_3.place(x=120,y=100, width=50, height=50)
btn_4.place(x=20,y=150, width=50, height=50)
btn_6.place(x=70,y=150, width=50, height=50)
btn_7.place(x=120,y=150, width=50, height=50)
btn_8.place(x=20,y=200, width=50, height=50)
btn_9.place(x=70,y=200, width=50, height=50)
btn_0.place(x=120,y=200, width=50, height=50)

btn_c.place(x=185,y=100, width=100, height=25)
btn_sum.place(x=185,y=125, width=50, height=50)
btn_sub.place(x=235,y=125, width=50, height=50)
btn_mul.place(x=185,y=175, width=50, height=50)
btn_div.place(x=235,y=175, width=50, height=50)
btn_result.place(x=185,y=225, width=100, height=25)

root.mainloop()
