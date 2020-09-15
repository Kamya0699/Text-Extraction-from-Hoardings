from tkinter import *
from PIL import ImageTk, Image
import webbrowser
import os

import grayscale

class ProcessWindow:
    def __init__(self):
        self.win=Tk()
        self.canvas=Canvas(self.win, width=600, height=500, bg="white")
        self.canvas.pack(expand=YES, fill=BOTH)
        width=self.win.winfo_screenwidth()
        height=self.win.winfo_screenheight()
        x=int(width/2-1000/2)
        y=int(height/2-750/2)
        strl="1000x750+" + str(x) + "+" + str(y)
        self.win.geometry(strl)

        self.win.resizable(width=FALSE, height=FALSE)
        self.win.title("WELCOME | Process Window | ADMINISTRATOR")


    def add_frame(self):
        self.frame=Frame(self.win, height=800, width=1950)
        self.frame.place(x=0, y=0)
        x, y =0, 0
        self.img = ImageTk.PhotoImage(Image.open("hh3.png"))
        self.label=Label(self.frame, image=self.img)
        self.label.place(x=x+0, y=y+0)
        self.button = Button(self.frame, text="Select the image", font=('helvetica', 20, 'underline italic'),
                             fg='brown', command=lambda: os.system('start "" "{}"'.format("D:\college work\minor\dataset")))
        self.button.place(x=x + 650, y=y + 350)
        self.button=Button(self.frame, text="Gray+Canny",font=('helvetica', 20, 'underline italic'), fg='brown', command=self.canny1)
        self.button.place(x=x+650, y=y+250)

        self.win.mainloop()

    def canny1(self):
        self.win.destroy()
        x=grayscale.cannywindow()
        x.canny()

if __name__=="__main__":
   x=ProcessWindow()
   x.add_frame()




