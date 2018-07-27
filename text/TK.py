# -*- coding: utf-8 -*-
# author：Super.Shen

import tkinter

import tkinter.messagebox

top1=tkinter.Tk()

def hello():
    tkinter.messagebox.showinfo("Hello Python", "Hello Runoob")

def text():
    tkinter.messagebox.showinfo("Hello Python", "Hello super")

def run():
    for i in range(10):
        print(i)

# B = tkinter.Button(top, text="点我", command=helloCallBack)
tkinter.Button(top1, text="点我", command=hello).pack()
tkinter.Button(top1, text="再点我", command=text).pack()
tkinter.Button(top1, text="第三次", command=run).pack()

top1.mainloop()