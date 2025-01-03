from tkinter import *

root=Tk()
root.geometry('300x150')
Label(root,text='Ice Cream and Drinks').pack(side=TOP)

frame=Frame(root)
frame.pack()

frame2=Frame(root)
frame2.pack(side=BOTTOM)

b1=Button(frame,text='Ice Cream',fg='red')
b1.pack(side=LEFT)

b2=Button(frame,text='Fortnite themed Ice Cream',fg='red')
b2.pack(side=LEFT)

b3=Button(frame,text='Jeugdjournaal Super Ijsje',fg='red')
b3.pack(side=LEFT)


b4=Button(frame2,text='Bepsi',fg='blue')
b4.pack(side=BOTTOM)

b5=Button(frame2,text='choch-golah',fg='blue')
b5.pack(side=BOTTOM)

b6=Button(frame2,text='Fanta',fg='blue')
b6.pack(side=BOTTOM)







































root.mainloop()


