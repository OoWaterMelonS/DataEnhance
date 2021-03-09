import glob
import os

path = 'E:/taidi/DataEnhance/bmp2jpg/'
paths = glob.glob(os.path.join(path, '*.jpg'))
for path in paths:
    str = path.split('-')[1].split('.')[0]
    if str == '1':
    # if str == '2':
        os.remove(path)
