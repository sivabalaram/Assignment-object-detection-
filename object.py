import numpy as  np
import cv2

img1=cv2.imread('human.jpeg')
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2=cv2.imread('fog.jpg')
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
img33=cv2.imread('hat.jpg')
img33=cv2.cvtColor(img33,cv2.COLOR_BGR2RGB)
import matplotlib.pyplot as plt
plt.imshow(img1)
x1_offset=100
y2_offset=90
x1_end=300
y2_end=500
roi=img1[y2_offset:y2_end,x1_offset:x1_end]
plt.imshow(roi)
plt.imshow(img2)
plt.imshow(img33)
xx1_offset=50
yy2_offset=30
xx1_end=550
yy2_end=230
rroi=img33[yy2_offset:yy2_end,xx1_offset:xx1_end]
plt.imshow(rroi)
rroi =cv2.resize(rroi,(150,150))
plt.imshow(rroi)
large_img = img2
small_img = roi
x_offset=600
y_offset=300
large_img[y_offset:y_offset+small_img.shape[0], x_offset:x_offset+small_img.shape[1]] = small_img
plt.imshow(large_img)
llarge_img = large_img
ssmall_img = rroi
xxxx_offset=600
yyyy_offset=210


llarge_img[yyyy_offset:yyyy_offset+ssmall_img.shape[0], xxxx_offset:xxxx_offset+ssmall_img.shape[1]] = ssmall_img
plt.imshow(large_img)