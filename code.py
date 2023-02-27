from turtle import width
import cv2 as c
import numpy as np

img= c.imread("road.jpg")
gray=c.cvtColor(img,c.COLOR_BGR2GRAY)
edges=c.Canny(gray,50,150,apertureSize=3)
lines= c.HoughLines(edges,1,np.pi/180,200)

for line in lines:
    rho,theta = line[0]
    a=np.cos(theta)
    b=np.sin(theta)
    x0=a*rho
    y0=b*rho

    x1=int(x0+1000*(-b))
    y1=int(y0+1000*(a))

    x2=int(x0-1000*(-b))
    y2=int(y0-1000*(a))
    c.line(img,(x1,y1),(x2,y2),(0,0,255),2)

c.imshow("image",img)
c.imshow("canny",edges)
c.waitKey(0)

c.destroyAllWindows()
