# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib_1 import pyplot as plt


# 直方图均衡化经常用来使所有的图片具有相同的亮度条件的参考工具

img = cv2.imread('../../hist_equa.png',0)

#flatten() 将数组变成一维
hist,bins = np.histogram(img.flatten(),256,[0,256])

# 计算累积分布图
cdf = hist.cumsum()

# 注意归一化的方法
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')  # 按绘图语句顺序指示线条信息
plt.show()


# print cdf
'''
[    0     0     0     0     0     0     0     0     0     0     0     0
     0     0     0     0     0     0     0     0     0     0     0     0
     0     0     0     0     0     0     0     0     0     0     0     0
     0     0     0     0     0     0     0     0     0     0     0     0
     0     0     0     0     0     0     0     0     0     0     0     0
     0     0     0     0     0     0     0     0     0     0     0     0
     0     0     0     0     0     0     0     0     0     0     0     0
     0     0     0     0     0     0     0     0     0     0     0     0
     0     0     0     0     1     1     1     1     1     1     2     2
     5     5     8    13    15    21    27    44    61    82   114   159
   231   319   443   595   811  1066  1343  1687  2090  2589  3271  4128
  5295  6683  8273 10198 12461 14973 17553 19864 22003 24043 25810 27582
 29200 30804 32371 33908 35500 36968 38515 39971 41428 42863 44170 45371
 46512 47545 48415 49290 50131 50902 51626 52245 52858 53432 53897 54326
 54725 55090 55412 55702 55964 56207 56439 56632 56812 56990 57141 57290
 57438 57549 57672 57774 57894 58015 58129 58252 58388 58512 58645 58771
 58902 59027 59155 59253 59356 59462 59564 59661 59729 59800 59845 59889
 59918 59938 59954 59966 59973 59979 59980 59984 59986 59990 59993 59994
 59994 59995 59995 59998 59998 59998 59999 60000 60000 60000 60000 60000
 60000 60000 60000 60000 60000 60000 60000 60000 60000 60000 60000 60000
 60000 60000 60000 60000 60000 60000 60000 60000 60000 60000 60000 60000
 60000 60000 60000 60000]'''


# 构建 Numpy 掩模数组， cdf 为原数组，当数组元素为 0 时，掩盖（计算时被忽略）。
cdf_m = np.ma.masked_equal(cdf,0)
# print cdf_m
'''
[-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 1L 1L 1L 1L 1L 1L 2L 2L 5L 5L 8L 13L 15L 21L 27L 44L 61L 82L 114L 159L
 231L 319L 443L 595L 811L 1066L 1343L 1687L 2090L 2589L 3271L 4128L 5295L
 6683L 8273L 10198L 12461L 14973L 17553L 19864L 22003L 24043L 25810L 27582L
 29200L 30804L 32371L 33908L 35500L 36968L 38515L 39971L 41428L 42863L
 44170L 45371L 46512L 47545L 48415L 49290L 50131L 50902L 51626L 52245L
 52858L 53432L 53897L 54326L 54725L 55090L 55412L 55702L 55964L 56207L
 56439L 56632L 56812L 56990L 57141L 57290L 57438L 57549L 57672L 57774L
 57894L 58015L 58129L 58252L 58388L 58512L 58645L 58771L 58902L 59027L
 59155L 59253L 59356L 59462L 59564L 59661L 59729L 59800L 59845L 59889L
 59918L 59938L 59954L 59966L 59973L 59979L 59980L 59984L 59986L 59990L
 59993L 59994L 59994L 59995L 59995L 59998L 59998L 59998L 59999L 60000L
 60000L 60000L 60000L 60000L 60000L 60000L 60000L 60000L 60000L 60000L
 60000L 60000L 60000L 60000L 60000L 60000L 60000L 60000L 60000L 60000L
 60000L 60000L 60000L 60000L 60000L 60000L 60000L 60000L 60000L 60000L
 60000L 60000L]'''


cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
# print cdf_m
'''
[-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 0L 0L 0L 0L 0L 0L 0L 0L 0L 0L 0L 0L 0L 0L 0L 0L 0L 0L 0L 0L 0L 1L 1L 2L 3L
 4L 5L 7L 8L 10L 13L 17L 22L 28L 35L 43L 52L 63L 74L 84L 93L 102L 109L 117L
 124L 130L 137L 144L 150L 157L 163L 169L 176L 182L 187L 192L 197L 202L 205L
 209L 213L 216L 219L 222L 224L 227L 229L 230L 232L 234L 235L 236L 237L 238L
 239L 240L 241L 242L 242L 243L 244L 244L 245L 245L 246L 246L 247L 247L 248L
 248L 249L 249L 250L 250L 251L 251L 252L 252L 253L 253L 253L 254L 254L 254L
 254L 254L 254L 254L 254L 254L 254L 254L 254L 254L 254L 254L 254L 254L 254L
 254L 254L 254L 254L 255L 255L 255L 255L 255L 255L 255L 255L 255L 255L 255L
 255L 255L 255L 255L 255L 255L 255L 255L 255L 255L 255L 255L 255L 255L 255L
 255L 255L 255L 255L 255L 255L 255L]'''

# 对被掩盖的元素赋值，这里赋值为 0
cdf = np.ma.filled(cdf_m,0).astype('uint8')
# print cdf
'''
[  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0   0   0   0   0   1   1   2   3   4
   5   7   8  10  13  17  22  28  35  43  52  63  74  84  93 102 109 117
 124 130 137 144 150 157 163 169 176 182 187 192 197 202 205 209 213 216
 219 222 224 227 229 230 232 234 235 236 237 238 239 240 241 242 242 243
 244 244 245 245 246 246 247 247 248 248 249 249 250 250 251 251 252 252
 253 253 253 254 254 254 254 254 254 254 254 254 254 254 254 254 254 254
 254 254 254 254 254 254 254 255 255 255 255 255 255 255 255 255 255 255
 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255
 255 255 255 255]'''


# 现在就获得了一个表，我们可以通过查表得知与输入像素对应的输出像素
# 的值。我们只需要把这种变换应用到图像上就可以了。
img2 = cdf[img]


# -----------------------
# opencv
# -----------------------

img = cv2.imread('../../hist_equa.png',0)
equ = cv2.equalizeHist(img)  # 就这一句
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imwrite('res.png',res)
cv2.imshow('res',res)
cv2.waitKey(0)
