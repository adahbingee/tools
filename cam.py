import cv2 as cv

cap = cv.VideoCapture(2)
if not cap.isOpened():
    print('Cannot open camera')
    exit()

# ret = cap.set(cv.CAP_PROP_AUTO_EXPOSURE, 0)
# ret = cap.set(cv.CAP_PROP_EXPOSURE, 40)
ret =  cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
ret &= cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
# ret &= cap.set(cv.CAP_PROP_FPS, 25)
print(ret)

while(True):
    ret, frame = cap.read()

    if not ret:
        print('Can\'t receive frame (stream end?). Exiting ...')
        break

    frame = cv.flip(frame, 1)

    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()