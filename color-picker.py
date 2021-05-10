import cv2 as cv
import numpy as np
from cv2 import *

WIN_NAME      = 'img'                                   # window title
WIN_SIZE_X    = 800                                     # window image width
WIN_SIZE_Y    = 800                                     # window image height
NORM_SIZE     = 500                                     # normalized image width and height
BLK_SIZE_X    = 40                                      # normalized image block width
BLK_SIZE_Y    = 70                                      # normalized image block height
BLK_MARGIN_X  = 44                                      # normalized image block horizontal margin
BLK_MARGIN_Y  = 55                                      # normalized image block vertical   margin
BLK_OFFSET_X  = 20                                      # normalized image block horizontal offset
BLK_OFFSET_Y  = 25                                      # normalized image block vertical   offset
BLK_NUM_X     = 6                                       # color block horizontal number
BLK_NUM_Y     = 4                                       # color block vertical   number
img           = np.zeros( (1, 1, 3), dtype=np.uint8 )   # the actual image
imgS          = np.zeros( (1, 1, 3), dtype=np.uint8 )   # normalize displayed image
homoPoints    = []                                      # normalized [0, 1] points in [y, x] format

def onMouse(event, x, y, flags, param):
    global img, imgS, homoPoints, WIN_NAME

    imgSub = imgS[y-50:y+50, x-50:x+50, :]
    imgSub = resize(imgSub, (imgSub.shape[0]*2, imgSub.shape[1]*2), interpolation = INTER_NEAREST)
    subC   = (int(imgSub.shape[0]/2),  int(imgSub.shape[1]/2))
    drawMarker(imgSub, subC, (0, 255, 0), MARKER_CROSS)
    imshow('subImage', imgSub)

    if event == EVENT_LBUTTONDOWN:
        rect = getWindowImageRect(WIN_NAME)
        winSizeX = rect[2]
        winSizeY = rect[3]
        drawMarker(imgS, (x,y), (0, 255, 0), MARKER_CROSS)
        homoPoints.append([x/winSizeX, y/winSizeY])
        imshow(WIN_NAME, imgS)

        print(rect)
        print('{},{}'.format(x, y))
        print(homoPoints)

    if event == EVENT_RBUTTONDOWN:
        homoPoints = []
        imgS = resize(img, (WIN_SIZE_X, WIN_SIZE_Y))
        imshow(WIN_NAME, imgS)

def main():
    global img, imgS
    img      = imread('client.png')
    imgSizeY = img.shape[0]
    imgSizeX = img.shape[1]

    imgS = resize(img, (WIN_SIZE_X, WIN_SIZE_Y))
    imshow(WIN_NAME, imgS)
    setMouseCallback(WIN_NAME, onMouse)
    waitKey()

    if len(homoPoints) == 4:
        # remove mouse callback
        setMouseCallback(WIN_NAME, lambda *args : None)
        print('compute homography')
        srcPoints = np.float32(homoPoints) * np.float32([imgSizeX, imgSizeY])
        dstPoints = np.float32([[0, 0], [1, 0], [1, 1], [0, 1]]) * NORM_SIZE
        M         = getPerspectiveTransform(srcPoints, dstPoints)
        imgWarp   = warpPerspective(img, M, (NORM_SIZE, NORM_SIZE))

        for y in range(BLK_NUM_Y):
            iy0 = BLK_OFFSET_Y + y*(BLK_SIZE_Y + BLK_MARGIN_Y)
            iy1 = iy0 + BLK_SIZE_Y
            for x in range(BLK_NUM_X):
                ix0 = BLK_OFFSET_X + x*(BLK_SIZE_X + BLK_MARGIN_X)
                ix1 = ix0 + BLK_SIZE_X
                rectangle(imgWarp, (ix0, iy0), (ix1, iy1), (0, 255, 0))
                avg = mean(imgWarp[iy0:iy1, ix0:ix1])[:3]

                # put text
                avgR = np.round(avg)
                putText(imgWarp, 'B:{}'.format(int(avgR[0])), (ix0, iy0+00+BLK_OFFSET_Y), FONT_HERSHEY_PLAIN, 0.8, (0, 255, 0), 1, LINE_AA)
                putText(imgWarp, 'G:{}'.format(int(avgR[1])), (ix0, iy0+12+BLK_OFFSET_Y), FONT_HERSHEY_PLAIN, 0.8, (0, 255, 0), 1, LINE_AA)
                putText(imgWarp, 'R:{}'.format(int(avgR[2])), (ix0, iy0+24+BLK_OFFSET_Y), FONT_HERSHEY_PLAIN, 0.8, (0, 255, 0), 1, LINE_AA)
                print(avg)

        imshow('imgWarp', imgWarp)
        waitKey()
    else:
        print('4 points for homography')

if __name__ == "__main__":
    main()