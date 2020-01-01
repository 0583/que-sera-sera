from .dhash import DHash
from .retouch import Retouch
import os
from PIL import Image
from enum import IntEnum
import cv2


class BottleCapType(IntEnum):
    INVALID = 0
    POS = 1
    NEG = 2
    STANDING = 3


class Identify:
    def __init__(self):
        self.__init_config()
        self.__init_load()

    def __init_config(self):
        # path config
        self.path_list = [
            '../standard/positive', '../standard/negative',
            '../standard/standing'
        ]
        self.standard_img_list = [[], [], []]
        self.switcher = {
            0: BottleCapType.POS,
            1: BottleCapType.NEG,
            2: BottleCapType.STANDING,
            3: BottleCapType.INVALID
        }
        self.threshold = 0.8

    def __init_load(self):
        owd = os.getcwd()
        for idx, path in enumerate(self.path_list):
            filename_list = os.listdir(path)
            os.chdir(path)
            for filename in filename_list:
                # self.standard_img_list[idx].append(Image.open(filename))
                self.standard_img_list[idx].append(cv2.imread(filename))
            os.chdir(owd)

    def __diff(self, img_l, img_r):
        distance = DHash.hamming_distance(img_l, img_r)
        return 1 - distance * 1. / (32 * 32 / 4)

    def __compare(self, img_test, img_list):
        score = 0
        for img in img_list:
            score += self.__diff(img_test, img)
        return score / len(img_list)

    def __size_evaluation(self, size):
        return ((size[0] > 2 * size[1]) | (size[1] > 2 * size[0]))

    def judge(self, img_test):
        img_retouched = Retouch.retouch(img_test)
        size = img_retouched.shape

        if self.__size_evaluation(size):
            idx = 2
        else:
            avg_score = [0, 0, 0]
            for i in range(3):
                avg_score[i] = self.__compare(Retouch.retouch(img_test),
                                              self.standard_img_list[i])
                print(avg_score[i])
            max_score = max(avg_score[:2])
            idx = avg_score.index(max_score)

        return self.switcher[idx]

    def judge_list(self, img_test_list):
        type_list = []
        for img_test in img_test_list:
            type_list.append(self.judge(img_test))
        return type_list
