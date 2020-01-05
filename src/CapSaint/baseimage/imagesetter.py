import logging

__global_imgs = []


def isEmpty():
    global __global_imgs
    return len(__global_imgs) == 0


def getCount():
    global __global_imgs
    return len(__global_imgs)


def getImageAt(id):
    global __global_imgs
    assert(type(id) == int)

    if id < 0 or id >= getCount():
        logging.error("failed to get image id %d" % id)
        return

    return __global_imgs[id]


def setImageAt(id, image):
    global __global_imgs
    assert(type(id) == int)

    if id < 0 or id >= getCount():
        logging.error("failed to get image id %d" % id)
        return

    __global_imgs[id] = image


def appendImage(obj):
    global __global_imgs

    logging.info("called setImageObject, will add %s to __global_imgs" % obj)
    __global_imgs.append(obj)


def removeImageAt(id):
    global __global_imgs

    __global_imgs.pop(id)


def clearImageObject():
    global __global_imgs

    print("called clearImageObject.")
    __global_imgs.clear()
