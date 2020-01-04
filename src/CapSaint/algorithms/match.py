import cv2
from matplotlib import pyplot as plt


def match(img1, img2):
    sift = cv2.xfeatures2d.SIFT_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    # BFMatcher with default params
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    # Apply ratio test
    coord_list1 = []
    coord_list2 = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            coord_list1.append(kp1[m.queryIdx].pt)
            coord_list2.append(kp2[m.trainIdx].pt)

    return coord_list1, coord_list2
