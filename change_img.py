import sys
import os
import cv2

width = 64
height = 64

output_dir = './output_img'
input_dir = './input_img'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

index = 1
for path,dirnames,filenames in os.walk(input_dir):
    for filename in filenames:
        if filename.endswith('.JPG'):
            print('正在处理第 %s 张图片' % index)
            img_path = path + '/' + filename
            img = cv2.imread(img_path)
            new_img = cv2.resize(img, (width, height))
            cv2.imwrite(output_dir + '/' + str(index) + '.png', new_img)
            index += 1
            key = cv2.waitKey(30) & 0xff
            if key == 27:
                sys.exit(0)






