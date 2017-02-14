# -*- coding: utf-8 -*-
import cv2
import numpy as np

b,g,r = 0,0,0
drawing = False

def nothing(x):
    pass

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,b,g,r
    # 当按下左键是返回起始位置坐标
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y
    # 当鼠标左键按下并移动是绘制图形。 event 可以查看移动， flag 查看是否按下
    elif event==cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_FLAG_LBUTTON:
        if drawing==True:

            # 绘制圆圈，小圆点连在一起就成了线， 3 代表了笔画的粗细
            cv2.circle(img,(x,y),3,(b,g,r),-1)
            # 下面注释掉的代码是起始点为圆心，起点到终点为半径的
            # r=int(np.sqrt((x-ix)**2+(y-iy)**2))
            # cv2.circle(img,(x,y),r,(0,0,255),-1)
            # 当鼠标松开停止绘画。
    elif event==cv2.EVENT_LBUTTONUP:
        drawing==False
        # if mode==True:
            # cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        # else:
            # cv2.circle(img,(x,y),5,(0,0,255),-1)

# 创建一副黑色图像
img=np.zeros((900,800,3),np.uint8)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
switch='0:OFF\n1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing)

cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        b,g,r = 0,0,0

cv2.destroyAllWindows()

# 响应事件 -〉 img -〉不断显示 -修改全局bgr -〉 响应事件