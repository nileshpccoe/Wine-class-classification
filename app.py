# Wine quality categorization system

from tkinter import *
import tkinter.messagebox
import numpy as np

from sklearn.externals import joblib  
classifier = joblib.load('wine.model')
scaler = joblib.load('scaler.model')

top = Tk()
top.title('Wine Quality Categorization System')
top.geometry("500x500")
top.resizable(0, 0) 

window_height = 500
window_width = 900

screen_width = top.winfo_screenwidth()
screen_height = top.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

top.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

def check():
	global a, m, f, c, p
	new = np.array([[a.get(), m.get(), f.get(), c.get(), p.get()]])
	print (new)
	y_pred = classifier.predict(scaler.transform(new))
	if y_pred[0] == 1:
		tkinter.messagebox.showinfo('Result','This is Quality 1 Wine')
	elif y_pred[0] == 2:
		tkinter.messagebox.showinfo('Result','This is Quality 2 Wine')
	elif y_pred[0] == 3:
		tkinter.messagebox.showinfo('Result','This is Quality 3 Wine')	

a = DoubleVar()
m = DoubleVar()
f = DoubleVar()
c = DoubleVar()
p = DoubleVar()

Label(top, text="WINE QUALITY DETECTION SYSTEM", font=('Ubuntu', 25)).place(x=120,y=30)
Label(top, text="Alcalinity of ash:", font=('courier', 16)).place(x=20,y=100)
Entry(top, textvariable=a, font=('courier', 16)).place(x=280,y=100)
Label(top, text="Magnesium:", font=('courier', 16)).place(x=20,y=150)
Entry(top, textvariable=m, font=('courier', 16)).place(x=280,y=150)
Label(top, text="Flavanoids:", font=('courier', 16)).place(x=20,y=200)
Entry(top, textvariable=f, font=('courier', 16)).place(x=280,y=200)
Label(top, text="Color Intensity", font=('courier', 16)).place(x=20,y=250)
Entry(top, textvariable=c, font=('courier', 16)).place(x=280,y=250)
Label(top, text="Proline", font=('courier', 16)).place(x=20,y=300)
Entry(top, textvariable=p, font=('courier', 16)).place(x=280,y=300)
Button(top, text="--Check--", font=('courier', 16, 'bold'), command=check).place(x=250,y=400)

from PIL import ImageTk, Image
img = ImageTk.PhotoImage(Image.open("wine.png"))
Label(top, image = img).place(x=550,y=100)
 
top.mainloop()
