import tkinter as tk
import time
import keyboard
import sys
import os
root =tk.Tk() 
TimeS=False
countword=0
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def wpm(word,timeing):
    print("time",timeing)
    print("word",word)
    value=(str(round((word/5)/(timeing/60)))+" WPS")
    gwpm=tk.Label(root, text=value,font = "Helvetica 14 bold" )
    gwpm.pack()
    B = tk.Button(root, text ="Reset",activeforeground = "blue",activebackground = "pink",pady=10,padx=20, command = restart_program)
    B.pack()
    
def pressed(keyevent):
    global TimeS,timeing,start,stop,countword
    if((keyevent.keycode==8)):
        countword=countword-1    
    elif (keyevent.keycode!=8):
        countword=countword+1
    print(countword)
    if(keyevent.char=="\r"):

        stop=time.time()
        timeing=round(stop-start)
        countword=countword-1
        wpm(countword,timeing)
    if not TimeS:
        start = time.time()
        print("time start",start)
        TimeS=True

    type_word = txt.get()
    print(type_word)
root.geometry('600x400')
var = tk.StringVar()
label =tk.Label( root, textvariable=var,font = "Helvetica 14 bold" )

var.set("Lorem Ipsum is simply dummy text of the printing\n and typesetting industry.Lorem Ipsum has been\nthe industry's standard dummy text ever since the 1500s, \nwhen an unknown printer took\na galley of type and scrambled it to make a\ntype specimen book.")
label.pack()
txt =tk.Entry(root,width=50,justify='center',font = "Helvetica 14 bold")
txt.pack()
txt.bind('<KeyRelease>', pressed)

root.mainloop()