import pywhatkit
from tkinter import *

root=Tk()
root.title("WHATSAPP MESSAGE SENDER")
root.geometry('650x471')
root.configure(background='springgreen')

Label(root, text="!-----COMMUNICATE WITH OTHERS THROUGH US-----!", font='san-serif 14 bold',bg="springgreen",fg="magenta").grid(row=0,column=0)
Label(root, text="ENTER THE MOBILE NUMBER WITH[+91]:", font='san-serif 15 bold',bg="springgreen").grid(row=2,column=0)
number = Entry(root, width=70)
number.grid(row=3,column=0)
Label(root, text="ENTER THE MESSAGE:", font='san-serif 15 bold',bg="springgreen").grid(row=4,column=0)
message = Entry(root, width=70)
message.grid(row=5,column=0)
Label(root, text="ENTER THE SENDING HOUR IN THE 24HR'S FORMAT ", font='san-serif 15 bold',bg="springgreen").grid(row=6,column=0)
hour = Entry(root, width=70)
hour.grid(row=7,column=0)
Label(root, text="ENTER THE SENDING MINUTE IN THE THE FORMAT OF (00-59) ", font='san-serif 15 bold',bg="springgreen").grid(row=8,column=0)
minute = Entry(root, width=70)
minute.grid(row=9,column=0)

Button(root, text='SEND', font='san-serif 16 bold', bg='red', padx=2,command="sendwhatmsg").grid(row=10,column=0)

n=number.get()
msg=message.get()
h=hour.get() 
m=minute.get()

def sendwhatmsg():
    pywhatkit.sendwhatmsg(n,msg,h,m)
                      
root.mainloop()
                      