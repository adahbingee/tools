import cv2 as cv
import threading

# set webcam resolution
sizeX = 1280
sizeY = 720

def openCam( idx ):
    webcam = cv.VideoCapture( idx )
    webcam.set(cv.CAP_PROP_FRAME_WIDTH,  sizeX)
    webcam.set(cv.CAP_PROP_FRAME_HEIGHT, sizeY)
    while True:
        ret, frame = webcam.read()

        if ret == True:
            cv.imshow('frame{}'.format(idx), frame)

        key = cv.waitKey(1)

        if key & 0xFF == ord('q'):
            break
    webcam.release()

def createCamThread( idx ):
    cam = threading.Thread( target = openCam, args=(idx,) )
    return cam

if __name__ == '__main__':
    threadPool = []
    threadPool.append( createCamThread( 0 ) )
    threadPool.append( createCamThread( 1 ) )

    for thread in threadPool:
        thread.start()

    for thread in threadPool:
        thread.join()