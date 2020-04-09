import time
from tkinter import *
from tkinter.font import Font
import random
class clock:
                
        def __init__(self):
                self.i=0
                self.colors = ['gold','hot pink','honeydew2',
                               'red','royalblue1','antiquewhite4',
                               'lawn green','bisque2',
                               'steelblue2','floral white',
                               'darkorange','azure2',
                               ]
                self.color = self.colors[self.i]
                self.root=Tk()
                self.root.resizable(False,False)
                self.root.title("Digital Clock")
                self.root.iconbitmap('clo.ico')

                self.fr = Frame(self.root, bd = 10,height =300,
                           width=1000,
                           bg ='black')
                
        def times(self):
                self.cur_t=time.strftime("%I:%M:%S %p")
                self.cur_d=time.strftime('%A')
                self.cur_D=time.strftime('%dth %B %Y')
                self.rD=Label(self.fr,
                         font=Font(family="AR DESTINE",size=40),
                         fg=self.color,bg="black",
                         text=self.cur_D)
                self.rt=Label(self.fr,
                         font=Font(family="AR DESTINE",size=70),
                         fg=self.color,bg="black",
                         text=self.cur_t)
                self.rd=Label(self.fr,
                         font=Font(family="AR DESTINE",size=40),
                         fg=self.color,bg="black",
                         text=self.cur_d)
                                
                self.rt.after(200,self.times)
                self.rD.grid(row=0,column=1)
                self.rt.grid(row=1,column=1)
                self.rd.grid(row=2,column=1)
                
        def color_change(self,event):
                
                self.i += 1
                if self.i > (len(self.colors)-1):
                        self.i=0
                self.color=self.colors[self.i]

obj=clock()

obj.fr.bind('<Button-1>',obj.color_change)


obj.fr.grid()
obj.times()

obj.root.mainloop()

