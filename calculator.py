import tkinter
from tkinter import font
root=tkinter.Tk()
root.geometry('400x300')
f1=font.Font(family='Arial',size=4)
operators = ['+', '-', '*', '/']
def ev(w):	
    current = entry.get()
    
    if w in operators:
        if current == "":
            return
        if current[-1] in operators:
            return
    entry.insert(tkinter.END, w)
def clear():
	entry.delete(0,tkinter.END)
def cal():
	expression = entry.get()
	try:
	       result = eval(expression) 
	       entry.delete(0, tkinter.END)
	       entry.insert(tkinter.END, str(result))
	       lb.insert(tkinter.END,str(result))
	except:
            entry.delete(0, tkinter.END)
def history(x):
	n=lb.selection_get()
	entry.delete(0, tkinter.END)
	entry.insert(tkinter.END, n)
lb=tkinter.Listbox(root)
lb.pack()
entry=tkinter.Entry(root,font=f1)
entry.pack()
frm=tkinter.Frame(root)
b1=tkinter.Button(frm,text='+',font=f1,command=lambda v='+':ev(v))
b1.grid(row=0,column=0)
b2=tkinter.Button(frm,text='-',font=f1,command=lambda v='-':ev(v))
b2.grid(row=1,column=0)
b3=tkinter.Button(frm,text='*',font=f1,command=lambda v='*':ev(v))
b3.grid(row=2,column=0)
b4=tkinter.Button(frm,text='/',font=f1,command=lambda v='/':ev(v))
b4.grid(row=3,column=0)
b5=tkinter.Button(frm,text='1',font=f1,command=lambda v='1':ev(v))
b5.grid(row=0,column=1)
b6=tkinter.Button(frm,text='4',font=f1,command=lambda v='4':ev(v))
b6.grid(row=1,column=1)
b7=tkinter.Button(frm,text='7',font=f1,command=lambda v='7':ev(v))
b7.grid(row=2,column=1)
b8=tkinter.Button(frm,text='c',font=f1,command=clear)
b8.grid(row=3,column=1)
b9=tkinter.Button(frm,text='2',font=f1,command=lambda v='2':ev(v))
b9.grid(row=0,column=2)
b10=tkinter.Button(frm,text='5',font=f1,command=lambda v='5':ev(v))
b10.grid(row=1,column=2)
b11=tkinter.Button(frm,text='8',font=f1,command=lambda v='8':ev(v))
b11.grid(row=2,column=2)
b12=tkinter.Button(frm,text='0',font=f1,command=lambda v='0':ev(v))
b12.grid(row=3,column=2)
b13=tkinter.Button(frm,text='3',font=f1,command=lambda v='3':ev(v))
b13.grid(row=0,column=3)
b14=tkinter.Button(frm,text='6',font=f1,command=lambda v='6':ev(v))
b14.grid(row=1,column=3)
b15=tkinter.Button(frm,text='9',font=f1,command=lambda v='9':ev(v))
b15.grid(row=2,column=3)
b16=tkinter.Button(frm,text='=',font=f1,command=cal)
b16.grid(row=3,column=3)
frm.pack(side=tkinter.BOTTOM)
lb.bind('<<ListboxSelect>>',history)
root.mainloop()