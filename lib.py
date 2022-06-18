def insertString(str, char, position):
    length = len(str)
    if (position > length or position < 0):
         return str
    return str[:position] + char + str[position:]

def getString(pixelList, fwd=True):
    ASCII_CHARS = " .-~*+#"
    ASCII_REV = "#+*~-. "
    ASCII_LIST = ASCII_CHARS if fwd else ASCII_REV
    return "".join([ASCII_LIST[((pixel*len(ASCII_LIST)) // 255)%len(ASCII_LIST)] for pixel in pixelList])
    

def resizeImage(image, resizeDim):
    imgRatio =  image.height/image.width if image.width > image.height else image.width / image.height
    imgScaleSize = (resizeDim*2, int(resizeDim // imgRatio)) if  image.width > image.height else (int(resizeDim // imgRatio), resizeDim)

    image = image.resize(imgScaleSize)
    return image

def getAsciiImage(image):
    image = resizeImage(image, 200)
    image = image.convert('L')
    imgData = image.getdata()
    asciiImage = getString(imgData)
    count = 0
    for i in range(0, image.height*image.width, image.width):
        asciiImage = insertString(asciiImage, '\n', i+count)
        count = count + 1
    return asciiImage.strip()
