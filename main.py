from os import listdir, path, getcwd
from sys import argv
from PIL import Image
import random
import argparse
from lib import getAsciiImage

def test():
    filesList = listdir('./test_images')
    targetFile = random.choice(filesList)
    print(targetFile)
    image = Image.open('./test_images/{}'.format(targetFile))
    asciiImageString = getAsciiImage(image)
    targetFile = targetFile.split('.')[0]
    with open('./output/ascii-{}.txt'.format(targetFile), 'w') as f:
            f.write(asciiImageString)
            
def getAsciiArt(imagePath):
    if not path.exists(imagePath):
        print("Given Path {} cannot be found!")
        return
    
    image = Image.open(imagePath)
    return getAsciiImage(image)
    
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A CLI that converts an Image into an ascii art.")
    parser.add_argument("-p", "--path",type=str, help="Path of the target image", default="./test_images/{}".format(random.choice(listdir('./test_images'))))
    parser.add_argument("-o", "--output",type=str, help="Path of the output text file")
    args = parser.parse_args()
    print(args.path)
    if not path.isfile(args.path):
        raise FileNotFoundError("Input File {} Not Found!".format(args.path))
    
    inputPath = args.path
    targetPath = args.output
    
    if not args.output:
        fileName = "{}.txt".format(path.basename(args.path).split('.')[0])
        targetPath = path.join(getcwd(), fileName)
    
    asciiImage = getAsciiArt(inputPath)
    
    print("Writing to File {}".format(targetPath))
    with open(targetPath, 'w') as f:
        f.write(asciiImage)
        print("Done!")