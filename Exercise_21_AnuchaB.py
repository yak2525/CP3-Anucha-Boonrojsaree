from tkinter import *
import math


def leftClickButton(event):
    result = float(textBoxWeight.get()) / math.pow(float(textBoxHight.get()) / 100, 2)
    if result > 30 :
        ans = "อ้วนมาก"
    elif result > 25 :
        ans = "อ้วน"
    elif result > 23 :
        ans = "น้ำหนักเกิน"
    elif result > 18.6 :
        ans = "น้ำหนักปกติเหมาะสม"
    else:
        ans = "ผอมเกินไป"
    labelResult.configure(text =ans)

MainWindow = Tk()
labelHight = Label(MainWindow, text="ส่วนสูง (cm)")
labelHight.grid(row=0, column=0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row=0, column=1)
labelWeight = Label(MainWindow, text="น้ำหนัก (kg)")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1, column=1)
calculateButton = Button(MainWindow, text="คำนวณ")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2, column=0)
labelResult = Label(MainWindow, text="ผลลัพธ์")
labelResult.grid(row=2, column=1)
MainWindow.mainloop()