# -*- coding: utf-8 -*-
# img.ravel() 将图像转成一维数组，这里没有中括号。
'''
计算比值： R = M/I 。反向投影 R，也就是根据 R 这个”调色板“创建一
副新的图像，其中的每一个像素代表这个点就是目标的概率。例如 B (x, y) =
R [h (x, y) , s (x, y)]，其中 h 为点（x， y）处的 hue 值， s 为点（x， y）处的
saturation 值。最后加入再一个条件 B (x, y) = min [B (x, y) , 1]。

h,s,v = cv2.split(hsvt)
B = R[h.ravel(),s.ravel()]
B = np.minimum(B,1)
B = B.reshape(hsvt.shape[:2])
'''