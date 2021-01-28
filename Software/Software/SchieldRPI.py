from tkinter import *
from tkinter.font import Font
import os
from os import popen

cmd=popen("vcgencmd measure_temp")
window = Tk()
window.title("ShieldRPI IDE")
window.geometry('120x360')

def funcDI0():
    lblDO0.configure(bg="red") 
    
os.system("gpio mode 7 in")
os.system("gpio mode 0 in")
os.system("gpio mode 2 in")
os.system("gpio mode 3 in")
os.system("gpio mode 1 in")

os.system("gpio mode 21 out")
os.system("gpio mode 22 out")
os.system("gpio mode 23 out")
os.system("gpio mode 24 out")
os.system("gpio mode 25 out")

os.system("gpio mode 27 out")
os.system("gpio mode 28 out")
os.system("gpio mode 29 out")



def script():
    os.system("python bash_code.py")
def ADC():
    os.system("python ADC.py")    
def d1():
    os.system("gpio toggle 21")
def d2():
    os.system("gpio toggle 22")
def d3():
    os.system("gpio toggle 23")
def d4():
    os.system("gpio toggle 24")
def d5():
    os.system("gpio toggle 25")

Label(window, text =cmd.read(), width="10", font=Font(family='Helvetica', size=12, underline =1, weight='bold')).grid(column = 0,row = 0,padx = 5,pady = 5)  
Label(window, text ="Digital Input", width="10", font=Font(family='Helvetica', size=10,underline =1, weight='normal')).grid(column = 0,row = 1,padx = 5,pady = 5)  
btnDI0 = Button(window, text="DI0", command=d1, width="10", font=Font(family='Helvetica', size=10,underline =0, weight='normal')).grid(column = 0,row = 2,padx = 5,pady = 5)   
btnDI1 = Button(window, text="DI1", command=d2, width="10", font=Font(family='Helvetica', size=10,underline =0, weight='normal')).grid(column = 0,row = 3,padx = 5,pady = 5)  
btnDI2 = Button(window, text="DI2", command=d3, width="10", font=Font(family='Helvetica', size=10,underline =0, weight='normal')).grid(column = 0,row = 4,padx = 5,pady = 5)    
btnDI3 = Button(window, text="DI3", command=d4, width="10", font=Font(family='Helvetica', size=10,underline =0, weight='normal')).grid(column = 0,row = 5,padx = 5,pady = 5)    
btnDI4 = Button(window, text="DI4", command=d5, width="10", font=Font(family='Helvetica', size=10,underline =0, weight='normal')).grid(column = 0,row = 6,padx = 5,pady = 5)   
Button(window, text="Lancer Script", command=script, width="10", font=Font(family='Helvetica', size=10,underline =0, weight='normal')).grid(column = 0,row = 8,padx = 5,pady = 5)  

Button(window, text="Lancer ADC", command=ADC, width="10", font=Font(family='Helvetica', size=10,underline =0, weight='normal')).grid(column = 0,row = 9,padx = 5,pady = 5) 



   

window.mainloop()