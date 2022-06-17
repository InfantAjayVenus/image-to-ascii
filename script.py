import random
import requests
from PIL import Image
from os import listdir
import io

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

def getRandomImage():    
    response = requests.get("https://api.unsplash.com/photos/random?client_id=Q9L4l0YmQTwxj_FtySLRgxv22HzGWTbJ-nSgthX9ATY").json()
    imageURL = response['urls']['raw']
    imageResponse = requests.get(imageURL)
    return Image.open(io.BytesIO(imageResponse.content))



def test():
    filesList = listdir('./test_images')
    targetFile = random.choice(filesList)
    print(targetFile)
    image = Image.open('./test_images/{}'.format(targetFile))
    asciiImageString = getAsciiImage(image)
    targetFile = targetFile.split('.')[0]
    with open('./output/ascii-{}.txt'.format(targetFile), 'w') as f:
            f.write(asciiImageString)


test()