import cv2
import numpy as np


def nop():
    pass


def mouse(event, x, y, flags, param):
    global drawing, clone, mask, size
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(clone, (x, y), size, (0, 0, 0), -1)
            cv2.circle(mask, (x, y), size, (255, 255, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


cv2.namedWindow('image', cv2.WINDOW_NORMAL)
img = cv2.imread('../old.jpg')
drawing = False
clone = img.copy()
mask = np.zeros(img.shape[:2], dtype=np.uint8)
cv2.setMouseCallback('image', mouse)
cv2.createTrackbar('size', 'image', 5, 20, nop)

while True:
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    dst = cv2.inpaint(img, mask, 1, cv2.INPAINT_TELEA)  # fix old image
    cv2.imshow('image', np.hstack([clone, dst]))
    size = cv2.getTrackbarPos('size', 'image')

cv2.destroyAllWindows()
