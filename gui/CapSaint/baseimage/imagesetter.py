__global_img = None

def isOk():
    global __global_img

    if __global_img == None:
        return False
    return True

def displayIt():
    global __global_img

    print("called displayIt.")
    if isOk():
        print("it's ok, so we're going to show %s" % __global_img)
        __global_img.show()
    print("not ok, not going to show anything")

def getImageObject():
    global __global_img

    print("called getImageObject, will return %s" % __global_img)
    return __global_img

def setImageObject(obj):
    global __global_img

    print("called setImageObject, will set __global_img to %s" % obj)
    __global_img = obj

def clearImageObject():
    global __global_img
    
    print("called clearImageObject.")
    __global_img = None
