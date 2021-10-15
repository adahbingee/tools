import cv2 as cv

webcam0 = cv.VideoCapture(0)
webcam1 = cv.VideoCapture(1)

# set webcam resolution
sizeX = 1280
sizeY = 720
webcam0.set(cv.CAP_PROP_FRAME_WIDTH,  sizeX)
webcam0.set(cv.CAP_PROP_FRAME_HEIGHT, sizeY)
webcam1.set(cv.CAP_PROP_FRAME_WIDTH,  sizeX)
webcam1.set(cv.CAP_PROP_FRAME_HEIGHT, sizeY)

isImgSizeSet = False

while True:
    ret0, frame0 = webcam0.read()
    ret1, frame1 = webcam1.read()

    if ret0 == True:
        cv.imshow('frame0', frame0)
    if ret1 == True:
        cv.imshow('frame1', frame1)

    key = cv.waitKey(1)

    if key & 0xFF == ord('q'):
        break