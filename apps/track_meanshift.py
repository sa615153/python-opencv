# -*- coding: utf-8 -*-
# 本例中存在的问题是——目标消失一段时间重现后，矩形框不在能聚焦到目标上
# 猜测具体过程是这样，目标消失，矩形框仍在找最大像素和，这个时候，屏幕上没有目标，所以是在毫无意义的图片上
# 寻找最大像素和，很可能被小数据中的极大值吸引，偏离原来正确位置，而且偏离得很远，即使目标重现——新的有效
# 直方图反向投影图出现，但由于偏离太远，矩形框内的质心位置已经失去了指示作用，所以矩形框不再回被质心导航到
# 正确的目标位置
'''如果问题出在这儿，那么应该得靠识别来解决，来重新定位
   即使问题不出在这，这也可能会是导致问题的潜在因素'''

'''经过逐帧检测，发现问题不是由目标消失直接造成，因为目标重现后，矩形框还能捕获目标，但是后又突然偏离'''

# r = 432
# c = 190
# w = 20
# h = 26
r = 438
c = 198
w = 8
h = 14

import numpy as np
import cv2
cap = cv2.VideoCapture('../a.mp4')
# take first frame of the video
ret,frame = cap.read()
# setup initial location of window
# r - row    c - col   h - hight(行数) w - width(列数)
r,h,c,w = 438,14,198,8  # simply hardcoded the values
track_window = (c,r,w,h)
# set up the ROI for tracking
roi = frame[r:r+h, c:c+w]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
while(1):
    ret ,frame = cap.read()
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)  # 目标信息介入追踪阶段  # para2 —— channel
        # apply meanshift to get the new location
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        # Draw it on image
        x,y,w,h = track_window
        img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
        cv2.imshow('img2',img2)
        k = cv2.waitKey(0) & 0xff
        if k == 27:
            break
        elif k == ord('q'):
            continue
        elif k == ord('s'):
            cv2.imwrite(chr(k)+".jpg",img2)

    else:
        break
cv2.destroyAllWindows()
cap.release()