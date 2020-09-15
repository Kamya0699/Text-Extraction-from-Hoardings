from tkinter import *
from PIL import ImageTk, Image
import h2
class WelcomeWindow:

    def __init__(self):
        self.win=Tk()
         # making the window screen
        self.canvas = Canvas(self.win, width=600, height=400, bg="white")
        self.canvas.pack(expand=YES, fill=BOTH)

        #bringing the screen in the centre
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 1200 / 2)
        y = int(height / 2 - 750 / 2)
        strl = "1200x750+" + str(x) + "+" + str(y)
        self.win.geometry(strl)

       # disable resize of the window

        self.win.resizable(width=False, height=False)

        # change the title of the window
        self.win.title("WELCOME | Text Extraction from hoardings | ADMINISTRATOR")

    def add_frame(self):
        # create an inner frame
        self.frame = Frame(self.win, height=800, width=1950)
        self.frame.place(x=0, y=0)
        x, y = 0, 0

    #  place the photo in the frame
        self.img = ImageTk.PhotoImage(Image.open("billboard.jpg"))
        self.label = Label(self.frame, image=self.img)
        self.label.place(x=x+0, y=y + 0)

        self.label = Label(self.frame, text="Text extraction from Hoardings")
        self.label.config(font=("Verdana", 40, 'bold'),fg='darkBlue')
        self.label.place(x=130, y=y + 10)

        self.button=Button(self.frame,text="Let's Begin",font=('helvetica',30,'underline bold italic'),bg='dark blue',fg='white', command=self.login)
        self.button.place(x=x+500, y=y+600)
        self.win.mainloop()
    # open a new window on pressing button
    def login(self):
        print("working")

        #destroy the current window frame
        self.win.destroy()
        # open the new login window
        log=h2.ProcessWindow()
        log.add_frame()


if __name__ == "__main__":
    x=WelcomeWindow()
    x.add_frame()