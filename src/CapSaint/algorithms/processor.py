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

    def __center_rbg(self, img):
        x = int(len(img) / 2)
        y = int(len(img[0]) / 2)
        return img[x][y]

    def __balance_determine(self, coord_list1, coord_list2, size):
        arg = 0.85

        counter = Counter(coord_list2).most_common(3)
        coords_commmon = []
        cnts_common = 0
        for i in range(3):
            coords_commmon.append(counter[i][0])
            cnts_common = cnts_common + counter[i][1]

        for idx in range(2):
            cnt = 0
            for coord1, coord2 in zip(coord_list1, coord_list2):
                if (coord2 in coords_commmon):
                    continue
                if (coord1[idx] > size[idx] / 2):
                    cnt = cnt + 1
            length = len(coord_list1) - cnts_common
            if ((cnt > length * arg) | (cnt < length * (1 - arg))):
                return 0
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
        elif not self.__balance_determine(coord_list1, coord_list2, img.shape):
            cap_type = 1

        return cap_type

    def judge(self, img_test, rect):
        tag = Tag()

        img_retouched, rect_local = Retouch.retouch(img_test)
        rgb = self.__center_rbg(img_retouched)
        size = img_retouched.shape

        if self.__size_evaluation(size):
            idx = 2
        else:
            idx = self.__match_determine(img_retouched)

        tag.rect = self.__fix_coordinate(rect, rect_local)
        tag.type = self.switcher[idx]
        tag.color = rgb
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
