import cv2 as cv

capture = cv.imread(r"C:\Users\ashis\OneDrive\Desktop\projects\opencv\imgs\Screenshot 2025-09-14 183212.png")

def changeRes(width, height): #used for live videos only 
    capture.set(3,width)
    capture.set(4,height)

def resize(frame,scale = 0.75): #robust used for imgs, videos and live videos as well
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def displayVid(capture):
    while True:
        isTrue, frame = capture.read()
        cv.imshow('video',frame)


cv.imshow('image',resize(capture))
cv.imshow('image',capture)
cv.waitKey(0)