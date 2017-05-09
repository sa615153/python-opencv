# -*- coding: utf-8 -*-
import numpy as np
import glob
import cv2

# dataset1
file_src = '../calibration_img/back_cam_big_grids/dataset1/'
files = file_src+'*.jpg'
# grids = (7,5)
cbrow = 5
cbcol = 7




# Load previously saved data
with np.load('cali_data.npz') as X:
    mtx, dist, _, _ = [X[i] for i in ('mtx','dist','rvecs','tvecs')]
# print mtx

def draw(img,corners,imgpts):
    corner = tuple(corners[0].ravel())
    img = cv2.line(img,corner,tuple(imgpts[0].ravel()),(255,0,0),5)
    img = cv2.line(img,corner,tuple(imgpts[1].ravel()),(0,255,0),5)
    img = cv2.line(img,corner,tuple(imgpts[2].ravel()),(0,0,255),5)
    return img

def draw_cube(img, corners, imgpts):
    imgpts = np.int32(imgpts).reshape(-1,2)
    # draw ground floor in green
    img = cv2.drawContours(img, [imgpts[:4]],-1,(0,255,0),-3)
    # draw pillars in blue color
    for i,j in zip(range(4),range(4,8)):
        img = cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]),(255),3)
    # draw top layer in red color
    img = cv2.drawContours(img, [imgpts[4:]],-1,(0,0,255),3)
    return img


criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((cbcol*cbrow,3), np.float32)
objp[:,:2] = np.mgrid[0:cbcol,0:cbrow].T.reshape(-1,2)
axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]).reshape(-1,3)

axis_cube = np.float32([[0,0,0], [0,3,0], [3,3,0], [3,0,0],
                   [0,0,-3],[0,3,-3],[3,3,-3],[3,0,-3] ])

cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.namedWindow('img_cube',cv2.WINDOW_NORMAL)

for fname in glob.glob(files):
    img = cv2.imread(fname)
    img_cube = img.copy()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (cbcol,cbrow),None)
    if ret == True:
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)

        # Find the rotation and translation vectors.两个vectors可用于将model参照系坐标转化为camera参照系坐标
        # objp是obj参考系下的35个点的坐标，所以z轴的坐标都为零
        # 返回的这两个矩阵某种意义上其实就是板子的pose
        ret, rvecs, tvecs = cv2.solvePnP(objp, corners2, mtx, dist)
        # project 3D points to image plane  将axis这三个点投射到image plane坐标
        imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)
        img = draw(img,corners2,imgpts)

        imgpts_cube, jac = cv2.projectPoints(axis_cube, rvecs, tvecs, mtx, dist)
        img_cube = draw_cube(img_cube, corners2, imgpts_cube)
        cv2.imshow('img',img)
        cv2.imshow('img_cube', img_cube)
        k = cv2.waitKey(0) & 0xFF
        if k == ord('s'):
            cv2.imwrite(fname[:6]+'.png', img)
cv2.destroyAllWindows()

