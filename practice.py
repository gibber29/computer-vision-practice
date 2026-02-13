import cv2 as cv

capture = cv.imread(r"C:\Users\ashis\OneDrive\Desktop\projects\opencv\imgs\Screenshot 2025-09-14 183212.png")

def changeRes(width, height): #this only works for live videos 
    capture.set(3,width)
    capture.set(4,height)

    
def resize(frame,scale = 0.75): #robust method works for images, videos, and live videos
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def displayVid(capture):
    while True:
        isTrue, frame = capture.read()
        frame_resized = resize(frame)
        cv.imshow('video',frame_resized)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    capture.release()
    cv.destroyAllWindows()

displayVid(capture)

cv.imshow('image',resize(capture))
cv.imshow('image',capture)
cv.waitKey(0)