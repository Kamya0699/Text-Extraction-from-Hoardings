import cv2
from tkinter import*
import numpy as np
class mserWindow():


 def mser(self):
#Create MSER object
      self.mser = cv2.MSER_create()
#Your image path i-e receipt path
      self.img = cv2.imread('hh3.png')
#Convert to grayscale
      self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
      self.vis = self.img.copy()
#detect regions in gray scale image

      self.regions, _ = self.mser.detectRegions(self.gray)
      self.hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in self.regions]
      cv2.polylines(self.vis, self.hulls, 1, (0, 255, 0))
      cv2.imshow('img', self.vis)
      cv2.waitKey(0)
      self.mask = np.zeros((self.img.shape[0], self.img.shape[1], 1), dtype=np.uint8)
      for contour in self.hulls:
          cv2.drawContours(self.mask, [contour], -1, (255, 255, 255), -1)
#this is used to find only text regions, remaining are ignored
      text_only = cv2.bitwise_and(self.img, self.img, mask=self.mask)
      cv2.imshow("text only", text_only)
      cv2.waitKey(0)

 # def tess(self):
 #     self.win.destroy()
 #     x=tesseract()
 #     x.tesseract()

if __name__=="__main__":
 x=mserWindow()
 x.mser()