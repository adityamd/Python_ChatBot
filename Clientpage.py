from tkinter import *
from threading import *
import socket,sys
i=1
s=socket.socket()
host=socket.gethostname();
port=1900
s.connect((host,port))
def send_message():
                global i
                message=mes_enter.get()
                M1=Message(box,text=message,width=len(message)**3+5,bg='white',border=2)
                M1.place(x=370-(len(message)*5),y=26*i)
                message=message.encode()
                s.send(message)
                i+=1
                print("Message Sent")
class rec_message(Thread):
        def run(self):
                global i
                while 1:
                        inc_mess=s.recv(1024)
                        inc_mess=inc_mess.decode()
                        rec_mes=Message(box,text=inc_mess,width=len(inc_mess)**3+5,bg='white',border=2)
                        rec_mes.place(x=5,y=26*i)
                        i+=1
rec=rec_message()
rec.start()
box=Tk()
box.geometry('400x400')
mes_enter=Entry(box,width=57)
send=Button(box,text="Send",command=send_message)
#recieve=Button(box,text="Recieve",command=rec_message)
#recieve.place(x=5,y=5)
mes_enter.place(x=5,y=355)
send.place(x=355,y=350)
box.mainloop()
