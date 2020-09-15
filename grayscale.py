import cv2
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import mser
from matplotlib import pyplot as plt # Conversion of image to grayscale

class cannywindow():
   def __init__(self):
      self.win = Tk()
      # making the window screen
      self.canvas = Canvas(self.win, width=600, height=400, bg="white")
      self.canvas.pack(expand=YES, fill=BOTH)

      # bringing the screen in the centre
      width = self.win.winfo_screenwidth()
      height = self.win.winfo_screenheight()
      x = int(width / 2 - 1200 / 2)
      y = int(height / 2 - 750 / 2)
      strl = "1200x750+" + str(x) + "+" + str(y)
      self.win.geometry(strl)
      self.win.configure(bg="Black")
      # disable resize of the window

      self.win.resizable(width=False, height=False)

      # change the title of the window
      self.win.title("WELCOME | Canny | ADMINISTRATOR")

   def canny(self):
      self.frame = Frame(self.win, height=800, width=1950)
      self.frame.place(x=0, y=0)
      x, y = 0, 0

      #  place the photo in the frame
      self.img = ImageTk.PhotoImage(Image.open("billboard.jpg"))
      self.label = Label(self.frame, image=self.img)
      self.label.place(x=x + 0, y=y + 0)

      self.label = Label(self.frame, text="GrayScale+Canny")
      self.label.config(font=("Verdana", 40, 'bold'), fg='darkBlue')
      self.label.place(x=130, y=y + 10)

      self.button = Button(self.frame, text="Go to MSER", font=('helvetica', 30, 'underline bold italic'),
                           bg='dark blue', fg='white', command=self.mser1)
      self.button.place(x=x + 500, y=y + 600)
      self.win.mainloop()


      self.img = cv2.imread("hh3.png",0) #use of canny algorithm function for edge detection
      self.canny = cv2.Canny(self.img,100,200)
      self.titles = ("image","canny")
      self.images = (self.img , self.canny)
      for i in range(2):
          plt.subplot(1 ,2,i+1), plt.imshow(self.images[i], 'gray')
          plt.title(self.titles[i])
          plt.xticks([]),plt.yticks([])
          plt.show() #cv2.imshow("Grey image",img)
      cv2.waitKey(0)
      cv2.destroyAllWindows()

   def mser1(self):
      self.win.destroy()
      x = mser.mserWindow()
      x.mser()

if __name__=="__main__":
   x=cannywindow()
   x.canny()