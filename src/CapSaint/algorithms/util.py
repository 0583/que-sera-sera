from enum import IntEnum


class BottleCapType(IntEnum):
    INVALID = 0
    POS = 1
    NEG = 2
    STANDING = 3


class Rect:
    def __init__(self, xx, yy, hh, ww):
        self.x = xx
        self.y = yy
        self.h = hh
        self.w = ww

    def __str__(self):
        return "xywh = (%d, %d, %d, %d)" % (self.x, self.y, self.w, self.h)


class Block:
    def __init__(self):
        self.rect = None
        self.img = None


class Tag:
    def __init__(self):
        self.rect = None
        self.color = None
        self.type = None
