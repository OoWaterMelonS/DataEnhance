import tensorflow as tf
import matplotlib.pyplot as plt

# 读取图片
img = tf.gfile.FastGFile("", 'rb').read()
# print(img)

# 建立会话
with tf.Session() as sess:
    # 解码图像
    img = tf.image.decode_jpeg(img)
    # 编码图像
    img_encode = tf.image.encode_jpeg(img)
    with tf.io.gfile.GFile("", 'wb') as file:
        file.write(img_encode.eval())
        plt.imshow(img.eval())
        plt.show()