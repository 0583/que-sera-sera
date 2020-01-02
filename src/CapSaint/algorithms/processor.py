from .dhash import DHash
from .retouch import Retouch
from .split import split
from .util import BottleCapType, Tag
import os
import cv2


class Identify:
    def __init__(self):
        self.__init_config()
        self.__init_load()

    def __init_config(self):
        # path config
        self.path_list = [
            '../../standard/positive', '../../standard/negative',
            '../../standard/standing'
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
        return ((size[0] > 1.5 * size[1]) | (size[1] > 1.5 * size[0]))

    def __fix_coordinate(self, rect, rect_local):
        rect.x = rect.x + rect_local.x
        rect.y = rect.y + rect_local.y
        rect.w = rect_local.w
        rect.h = rect_local.h
        return rect

    def judge(self, img_test, rect):
        tag = Tag()

        img_retouched, rect_local = Retouch.retouch(img_test)
        size = img_retouched.shape
        avg_score = [0, 0, 0]

        for i in range(3):
            avg_score[i] = self.__compare(img_retouched,
                                          self.standard_img_list[i])
            print(avg_score[i])

        print(size)
        if self.__size_evaluation(size):
            idx = 2
        else:
            max_score = max(avg_score[:2])
            idx = avg_score.index(max_score)

        tag.rect = self.__fix_coordinate(rect, rect_local)
        tag.type = self.switcher[idx]
        return tag

    def judge_list(self, img_test_list, rect_list):
        tags = []
        for img_test, rect in zip(img_test_list, rect_list):
            tag = self.judge(img_test, rect)
            tags.append(tag)
        return tags

    def process(self, img_scene):
        img_list, rect_list = split(img_scene)
        return self.judge_list(img_list, rect_list)
