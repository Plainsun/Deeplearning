# -*- coding: cp936 -*-

from tkinter import *

text_class = ''

def get_text():
    def go():
        global text_class
        text_class = entry.get()
        win.destroy()

    win = Tk(className='input label')
    win.geometry('230x100')  # ������x ������*

    label = Label(win)
    label['text'] = 'input label: '
    label.pack()  # ���ص�����

    entry = Entry(win)
    entry.pack()

    Button(win, text='ok', command=go).pack()
    # a = go()

    win.mainloop()


