from PIL import Image, ImageChops
import matplotlib.pyplot as plt
import glob


# shift
def shift(im):
    plt.figure()
    plt.subplot(1, 2, 1)
    img = Image.open(im)
    plt.imshow(img)
    img2 = ImageChops.offset(img, 200, 100)  # 水平位移：200，垂直位移：100
    plt.subplot(1, 2, 2)
    plt.imshow(img2)
    plt.show()
    # img = img.resize((224, 224), resample=Image.LANCZOS)
    save(img2, im, 'shift')
    return img2


# 遮挡
def paste(im):
    plt.figure()
    plt.subplot(1, 2, 1)
    img = Image.open(im)
    plt.imshow(img)
    img2 = img.crop((0, 0, 100, 100))  # 裁剪原图中一部分作为覆盖图片
    img.paste(img2, (150, 150, 150 + img2.size[0], 150 + img2.size[1]))  # 第二个参数是覆盖位置
    plt.subplot(1, 2, 2)
    plt.imshow(img)
    plt.show()
    save(img, im, 'paste')
    return img


# 剪切
def shear(im):
    plt.figure()
    plt.subplot(1, 2, 1)
    img = Image.open(im)
    plt.imshow(img)
    # image = cv2.resize(image,(224,224))
    cropped = img.crop((100, 100, 500, 500))  # 坐标从左上开始
    plt.subplot(1, 2, 2)
    plt.imshow(cropped)
    plt.show()
    save(cropped, im, 'shear')
    return cropped


def save(img, im, op):
    name = im.split("\\", )[1]
    dir = '/datadata/'
    name = dir + name.split(".")[0] + '_' + op + '.jpg'
    img.save(name)  # 写入图片


if __name__ == '__main__':
    cate = ['E:/taidi/DataEnhance/data/']
    for idx, folder in enumerate(cate):
        for im in glob.glob(folder + '/*.jpg'):
            img1 = shift(im)
            img2 = shear(im)
            img3 = paste(im)
