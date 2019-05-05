#AUTHOR: ROMAN BELAIRE
#COMPUTER VISION TO RECOGNIZE CARS IN A PARKING LOT
import cv2
import numpy as np
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt


camera = cv2.VideoCapture(0)
car_cascade = cv2.CascadeClassifier('cas1.xml')

def getImage():
    #camera.open()
    rec, Image = camera.read()
    #camera.release()
    return Image


def detectCars_cascade(img):
    #detects cars in image and returns rectangles as a list
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars, numCars = car_cascade.detectMultiScale2(gray, minNeighbors = 1, minSize = (30, 30), maxSize = (60, 60))
    rects = []
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        rect = []
        rect.append([x,y])
        rect.append([x+w, y])
        rect.append([x+w,y+h])
        rect.append([x, y+h])
        rect = np.array(rect)
        rects.append(rect)
    rects = np.array(rects)
    print(len(cars))
    #cv2.imshow(str(numCars), img)
    #cv2.waitKey(0)
    return rects, len(cars)


def getHeatMap(img, rects):
    exposure_frame = np.zeros((img.shape[0], img.shape[1]), dtype=np.float)#frame to hold "heat"

    #add rectangles to mask
    masking = np.zeros(exposure_frame.shape, dtype=np.float)
    for rect in rects:
        cv2.fillConvexPoly(masking, rect, (0.5), lineType=4)


    #cv2.imshow('', img)
    #cv2.waitKey(0)


    return img

def getData():
    image = getImage()
    rects, carNum = detectCars_cascade(image)
    img = getHeatMap(image, rects)
    return img, carNum

#image = cv2.imread('dataset/parking2.jpg')
#image = getImage()
#rects = detectCars_cascade(image)
#getHeatMap(image, rects)
