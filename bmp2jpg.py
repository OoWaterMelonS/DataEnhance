# coding:utf-8
import os
from PIL import Image


# bmp 转换为jpg
def bmpToJpg(file_path, out_path):
    for fileName in os.listdir(file_path):
        print(fileName)
        newFileName = fileName[0:fileName.find(".")] + ".jpg"
        print(newFileName)
        im = Image.open(file_path + "\\" + fileName)
        im.save(out_path + "\\" + newFileName)


def main():
    file_path = 'origin_data'
    out_path = 'bmp2jpg/'
    bmpToJpg(file_path, out_path)


if __name__ == '__main__':
    main()
