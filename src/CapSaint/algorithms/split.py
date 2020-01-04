import cv2
import numpy as np
from .util import Rect


def split(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    h, w = thresh.shape[0:2]
    mask = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, mask)
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    h, w = closed.shape[0:2]
    x = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,
                         cv2.CHAIN_APPROX_NONE)
    _, cnts, _b = x
    c = sorted(cnts, key=cv2.contourArea, reverse=True)
    img_list = []
    rect_list = []
    for k in range(len(c)):
        if cv2.contourArea(c[k]) < 10000:
            break
        rect = cv2.minAreaRect(c[k])
        box = np.int0(cv2.boxPoints(rect))
        Xs = [i[0] for i in box]
        Ys = [i[1] for i in box]
        x1 = min(Xs)
        x2 = max(Xs)
        y1 = min(Ys)
        y2 = max(Ys)
        hight = y2 - y1
        width = x2 - x1
        cropImg = image[y1:y1 + hight, x1:x1 + width].copy()
        img_list.append(cropImg)
        rect_list.append(Rect(y1, x1, hight, width))
    return img_list, rect_list
