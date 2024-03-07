from tkinter import *
from tkinter import ttk
import numpy as np
import time

win=Tk()

text1=Text(win,cursor='xterm',insertbackground='yellow')
text1.place(x=50,y=50)

text1.insert(INSERT,'Our product development philosophy \n')
text1.insert(END, ' is built on the idea of introducing \n')
text1.insert(END,'meaningful innovations  that deliver \n')
text1.insert(END, ' on real needs. Often, this takes the \n')
text1.insert(END, '  form of building from our existing \n')
text1.insert(END,' brands to deliver new solutions.')

text1.tag_add('big', '1.0', 'end')
text1.tag_config('big', font=("Arial bold",15))

arr1=[3.0,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,3.10,3.11,3.12,3.13,3.14,3.15,3.16,3.17,3.18,3.19,3.20,3.21,3.22]
arr2=[3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,3.10,3.11,3.12,3.13,3.14,3.15,3.16,3.17,3.18,3.19,3.20,3.21,3.22,3.23]
def call1():
    for i in range (0,22):
        
        start_value1=arr1[i]
        end_value1=arr2[i]
        
        text1.tag_add('highlight',start_value1,end_value1)
        text1.tag_config('highlight',background='yellow')
        time.sleep(0.35)
        text1.update()
        
call1()
win.mainloop()
