from .retouch import Retouch
from .split import split
from .util import BottleCapType, Tag
from .match import match
import os
import cv2
from collections import Counter


class Identify:
    def __init__(self):
        self.__init_config()
        self.__init_load()

    def __init_config(self):
        # path config
        self.path = '../../standard'
        self.standard_img_list = []
        self.switcher = {
            0: BottleCapType.POS,
            1: BottleCapType.NEG,
            2: BottleCapType.STANDING,
            3: BottleCapType.INVALID
        }
        self.threshold = 0.8

    def __init_load(self):
        owd = os.getcwd()
        filename_list = os.listdir(self.path)
        os.chdir(self.path)
        for filename in filename_list:
            self.standard_img_list.append(cv2.imread(filename))
        os.chdir(owd)

    def __size_evaluation(self, size):
        return ((size[0] > 1.2 * size[1]) | (size[1] > 1.2 * size[0]))

    def __fix_coordinate(self, rect, rect_local):
        rect.x = rect.x + rect_local.x
        rect.y = rect.y + rect_local.y
        rect.w = rect_local.w
        rect.h = rect_local.h
        return rect

    def __balance_determine(self, coord_list1, coord_list2, size):
        arg = 0.85

        most_cnts = Counter(coord_list2).most_common(1)
        if (most_cnts[0][1] > len(coord_list2) / 2):
            return 0

        print(len(coord_list1))
        print(len(coord_list2))
        for idx in range(2):
            cnt = 0
            for coord in coord_list1:
                if (coord[idx] > size[idx] / 2):
                    cnt = cnt + 1
            print(cnt)
            if ((cnt > len(coord_list1) * arg) | (cnt < len(coord_list1) *
                                                  (1 - arg))):
                return 0
        print("balance")
        return 1

    def __match_determine(self, img):
        cap_type = 0
        coord_list1 = []
        coord_list2 = []
        for standard_img in self.standard_img_list:
            coord_list1_tmp, coord_list2_tmp = match(img, standard_img)
            if (len(coord_list1_tmp) > len(coord_list1)):
                coord_list1 = coord_list1_tmp
                coord_list2 = coord_list2_tmp

        if (len(coord_list1) < 10):
            cap_type = 1

        if not self.__balance_determine(coord_list1, coord_list2, img.shape):
            cap_type = 1

        return cap_type

    def judge(self, img_test, rect):
        tag = Tag()

        img_retouched, rect_local = Retouch.retouch(img_test)
        size = img_retouched.shape

        if self.__size_evaluation(size):
            idx = 2
        else:
            idx = self.__match_determine(img_retouched)

        tag.rect = self.__fix_coordinate(rect, rect_local)
        tag.type = self.switcher[idx]
        print(tag.type)
        return tag, img_retouched

    def judge_list(self, img_test_list, rect_list):
        tags = []
        imgs = []
        for img_test, rect in zip(img_test_list, rect_list):
            tag, img = self.judge(img_test, rect)
            tags.append(tag)
            imgs.append(img)
        # display
        cwd = os.getcwd()
        os.chdir('../../result/retouched')
        for idx, img in enumerate(imgs):
            cv2.imwrite("{}.png".format(idx), img)
        os.chdir(cwd)
        return tags

    def process(self, img_scene):
        img_list, rect_list = split(img_scene)
        return self.judge_list(img_list, rect_list)
