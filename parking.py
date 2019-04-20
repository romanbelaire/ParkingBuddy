#AUTHOR: ROMAN BELAIRE
#COMPUTER VISION TO RECOGNIZE CARS IN A PARKING LOT
import cv2


camera = cv2.VideoCapture(1)
car_cascade = cv2.CascadeClassifier('cas1.xml')

def getImage():
    #camera.open()
    rec, Image = camera.read()
    #camera.release()
    return Image


def detectCars(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars, numCars = car_cascade.detectMultiScale2(gray, minNeighbors = 1, minSize = (30, 30), maxSize = (60, 60))
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    print(len(cars))
    cv2.imshow(str(numCars), img)
    cv2.waitKey(0)

image = cv2.imread('dataset/parking2.jpg')
#image = getImage()
detectCars(image)
