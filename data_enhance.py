# coding:utf8
import numpy as np
import os
import cv2
import glob
import shutil
import random
import xlsxwriter

from del_directory import delete_file

# 批量重命名文件
# 批量裁剪图片
# 数据扩增

w = 224
h = 224




def write_excel(data):
    workbook = xlsxwriter.Workbook(r'./label_number.xlsx')
    worksheet = workbook.add_worksheet('sheet2')
    worksheet.write(0, 0, 'Oldname')
    worksheet.write(0, 1, 'Newname')
    for k, i in zip(range(len(data)), data.keys()):
        j = data[i]
        worksheet.write(k + 1, 0, i)
        worksheet.write(k + 1, 1, j)
    workbook.close()


# 移动
def move(filename):
    save_path_img = r'./dele111'
    os.makedirs(save_path_img, exist_ok=True)
    shutil.move(filename, save_path_img)


# 裁剪
def resize(path):
    cate = [path + x for x in os.listdir(path) if os.path.isdir(path + x)]
    print('读取图像开始')
    print(cate)
    class_dict_id_number = {}
    num = []
    count = 0
    ids = []
    for idx, folder in enumerate(cate):
        folder1 = folder.split('/')
        id = folder1[4]
        print(id, folder)
        p = 'D:/me/animal/part4/' + id
        ids.append(id)
        if not os.path.exists(p):
            os.makedirs(p)
        for im in glob.glob(folder + '/*.jpg'):
            try:
                img = cv2.imread(im)
                img = cv2.resize(img, (w, h))
                im = im.split('\\')
                im = im[1]
                cv2.imwrite(p + '/' + im, img)
                count += 1
            except:
                print(im)
                # move(im)
        num.append(count)
        count = 0

    for i, j in zip(ids, num):
        class_dict_id_number[i] = j
    print(class_dict_id_number)
    write_excel(class_dict_id_number)


# 翻转
def flip(pic):
    img = []
    h_pic = cv2.flip(pic, 1)  # 水平翻转
    v_pic = cv2.flip(pic, 0)  # 垂直翻转
    hv_pic = cv2.flip(pic, -1)  # 水平垂直翻转
    img.append(h_pic)
    img.append(v_pic)
    img.append(hv_pic)
    return img


# 旋转
def rotate(pic):
    scale = 1.0
    # pic = cv2.resize(pic,(400,400))
    rows, cols = pic.shape[:2]
    img = []
    angle = [45, 90, 135, 180, 225, 275, 320]
    center = (cols / 2, rows / 2)  # 取图像的中点
    for a in angle:
        M = cv2.getRotationMatrix2D(center, a, scale)  # 获得图像绕着某一点的旋转矩阵
        pic = cv2.warpAffine(pic, M, (cols, rows), borderValue=(255, 255, 255))
        img.append(pic)
        # cv2.warpAffine()的第二个参数是变换矩阵,第三个参数是输出图像的大小
    return img


# 噪声
def noise(pic):
    for i in range(1500):
        pic[random.randint(0, pic.shape[0] - 1)][random.randint(0, pic.shape[1] - 1)][:] = 255
    return pic
    # random.randint(a, b)
    # 用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b


# 高斯模糊
def gussian(pic):
    img = []
    temp = cv2.GaussianBlur(pic, (9, 9), 1.5)
    dst = cv2.blur(pic, (11, 11), (-1, -1))
    # cv2.GaussianBlur(图像，卷积核，标准差）
    img.append(temp)
    img.append(dst)
    return img


# 光照
def light(pic):
    img = []
    contrast = 1  # 对比度
    brightness = 100  # 亮度
    pic_turn1 = cv2.addWeighted(pic, contrast, pic, 0, brightness)
    pic_turn2 = cv2.addWeighted(pic, 1.5, pic, 0, 50)
    img.append(pic_turn1)
    img.append(pic_turn2)
    # cv2.addWeighted(对象,对比度,对象,对比度)
    '''cv2.addWeighted()实现的是图像透明度的改变与图像的叠加'''
    return img


# 仿射
def fangshe(pic):
    rows, cols = pic.shape[:2]

    point1 = np.float32([[50, 50], [300, 50], [50, 200]])
    point2 = np.float32([[10, 100], [300, 50], [100, 250]])

    M = cv2.getAffineTransform(point1, point2)
    dst = cv2.warpAffine(pic, M, (cols, rows), borderValue=(255, 255, 255))
    # 对图像进行变换（三点得到一个变换矩阵）
    # 我们知道三点确定一个平面，我们也可以通过确定三个点的关系来得到转换矩阵
    # 然后再通过warpAffine来进行变换
    return dst


# 平移
def pingyi(img):
    rows, cols = img.shape[:2]
    M = np.array([[1, 0, -100], [0, 1, -50]], dtype=np.float32)
    img_change = cv2.warpAffine(img, M, (cols, rows))
    img_change = cv2.resize(img_change, (224, 224))
    return img_change


if __name__ == '__main__':
    path_re = "E:/taidi/DataEnhance/bmp2jpg/"


    print('读取图像开始')
    # print(cate)
    cate = ['E:/taidi/DataEnhance/bmp2jpg/']
    img_all = []
    for idx, folder in enumerate(cate):
        folder1 = folder.split('/')
        id = folder1[3]
        print(id, folder)
        p = path_re + id + '/'
        for im in glob.glob(folder + '/*.jpg'):
            try:
                img = cv2.imread(im)
                # img = cv2.resize(img, (224, 224))
                noi = noise(img)  # 噪声
                fli_h = flip(img)[0]  # 水平翻转
                fli_v = flip(img)[1]  # 垂直翻转
                fli_hv = flip(img)[2]  # 水平垂直翻转
                rot = rotate(img)  # 旋转
                guss = gussian(img)  # 模糊
                li = light(img)  # 光线
                fan = fangshe(img)  # 仿射
                result = {'img': img,
                          'noi': noi,
                          'fli_h': fli_h, 'fli_v': fli_v, 'fli_hv': fli_hv,
                          'rot_45': rot[0], 'rot_90': rot[1], 'rot_135': rot[2], 'rot_180': rot[3],
                          'rot_225': rot[4], 'rot_275': rot[5], 'rot_320': rot[6],
                          'guss_1': guss[0], 'guss_2': guss[1],
                          'li_0': li[0], 'li_1': li[1],
                          'fan': fan}
                im = im.split('\\')
                im = im[1].split('.')[0]
                des = 'E:/taidi/DataEnhance/train/' + im + '/'
                if not os.path.exists(des):
                    os.makedirs(des)
                for i, key in zip(range(len(result)), result):
                    imge = cv2.resize(result[key], (224, 224))
                    path = des + key + '.jpg'
                    temp = des + im + '~' + key + '.jpg'
                    cv2.imwrite(temp, imge)
            except:
                print(im)
            img_all = []

