# -*- coding: utf-8 -*-
'''
自己的图片总是出现roi=[0,0,0,0],消除畸变的图片也是很奇怪，原因可能是重复图片和chessboard所占图片比例不够大，具体参见
http://stackoverflow.com/questions/36387602/strange-results-with-opencv-camera-calibration
'''









import numpy as np
import cv2
import glob

# #------------------------------------------------------------------------------------
# file_src = '../calibration_img/sample_pic/'
# files = file_src+'*.jpg'
# grids = (7,6)
# cbrow = 6
# cbcol = 7

# file_src = '../calibration_img/PIC_front_double_cam_small_grids/'
# files = file_src+'*.jpg'
# grids = (9,7)
# cbrow = 7
# cbcol = 9

# dataset1
file_src = '../calibration_img/back_cam_big_grids/dataset1/'
files = file_src+'*.jpg'
grids = (7,5)
cbrow = 5
cbcol = 7

# dataset2
# file_src = '../calibration_img/back_cam_big_grids/dataset2'
# files = file_src+'*.jpg'
# grids = (5,7)
# cbrow = 7
# cbcol = 5

# general
# file_src = '../calibration_img/back_cam_big_grids/dataset2/'
# files = file_src+'*.jpg'
# cbrow = 5
# cbcol = 7

# #------------------------------------------------------------------------------------



# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)


# #--------------np.mgrid[0:cbcol, 0:cbrow].T.reshape(-1, 2)-------------------------------
# general
objp = np.zeros((cbcol*cbrow,3), np.float32)
objp[:,:2] = np.mgrid[0:cbcol,0:cbrow].T.reshape(-1,2)
# #---------------------------------------------



# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob(files)

rows, cols = 0, 0

cv2.namedWindow('img',cv2.WINDOW_NORMAL)
for fname in images:  # 遍历文件名列表
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Find the chess board corners    findChessboardCorners(gray, (cbcol, cbrow), None)
    # ret, corners = cv2.findChessboardCorners(gray, grids, None)
    ret, corners = cv2.findChessboardCorners(gray, (cbcol,cbrow), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        # print objpoints
        # print '--------------corners-----------------'
        # print corners
        # print img.shape
        # print gray.shape[::-1]
        rows,cols = gray.shape


        corners2=cv2.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)
        # Draw and display the corners   findChessboardCorners(gray, (cbcol, cbrow), None)
        # cv2.drawChessboardCorners(img, grids, corners2, ret)
        cv2.drawChessboardCorners(img, (cbcol,cbrow), corners2, ret)
        cv2.imshow('img', img)
        cv2.waitKey(0)
cv2.destroyAllWindows()
#
#
# calibration

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, (cols,rows,), None, None)
results = cv2.calibrateCamera(objpoints, imgpoints, (cols,rows,), None, None)
print 'results of cv2.calibrateCamera(objpoints, imgpoints, (cols,rows,), None, None)'
print results
print type(results)  # tuple(float,array([[][][]]),array([[]]),[array,array,array,array],[array,array,array,array])
np.savez_compressed('cali_data.npz',mtx=mtx,dist=dist,rvecs=rvecs,tvecs=tvecs)

#
#
# ---------------------------------------------------------------------------------------------------
# #--------------------------------------------------------
# img = cv2.imread(file_src+'left12.jpg')

# img = cv2.imread(file_src+'IMG_20170505_105250.jpg')

img = cv2.imread(file_src+'IMG_20170507_112713.jpg')
# img = cv2.imread(file_src+'IMG_20170508_095919.jpg')

# #--------------------------------------------------------

h,  w = img.shape[:2]
newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

# undistort
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
# crop the image
x, y, w, h = roi
print 'roi'
print roi
print 'mtx'
print mtx
print  'dist'
print dist
print 'rvecs'
print rvecs
print 'tvecs'
print tvecs

# dst = dst[y:y+h, x:x+w]
cv2.imwrite('./result/npz.png', dst)