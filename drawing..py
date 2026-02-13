import cv2 as cv
import numpy as np 

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#painting an image 
blank[0:,0:100] = 0,255,0 #first range changed the colour along the entire height, second range changed colour for the width
#drawing a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2) #for colouring thatr region we can put thickness = cv.FILLED or =-1
#similarly for a circle itd be .circle(img,center,radius,colour,thickness)


#to write a text on an image 
cv.putText(blank,'Hello',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=2)
cv.imshow('Green',blank)
cv.waitKey(0)