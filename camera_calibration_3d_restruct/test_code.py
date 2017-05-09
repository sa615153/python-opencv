# -*- coding: utf-8 -*-
import numpy as np
import cv2


objp = np.zeros((6*7,3), np.float32)
# print objp
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
# print objp

axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]])
# print axis

axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]).reshape(-1,3)
# print axis

def test_corners_funcSolvePnP():
    with np.load('cali_data.npz') as X:
        mtx, dist, _, _ = [X[i] for i in ('mtx', 'dist', 'rvecs', 'tvecs')]
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    objp = np.zeros((7 * 5, 3), np.float32)
    objp[:, :2] = np.mgrid[0:7, 0:5].T.reshape(-1, 2)
    axis = np.float32([[3, 0, 0], [0, 3, 0], [0, 0, -3]]).reshape(-1, 3)
    img = cv2.imread('../calibration_img/back_cam_big_grids/dataset1/IMG_20170507_112713.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (7,5),None)
    # print ret
    # print corners
    corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
    # print '---------------------------------------------------------'
    # print corners2
    what = cv2.solvePnP(objp, corners2, mtx, dist)
    print what
    print type(what)
    # '''
    # (True, array([[ 0.15209269],
    #    [-0.02034258],
    #    [-0.58866694]]), array([[-3.64994464],
    #    [-1.32451522],
    #    [ 9.6160166 ]]))
    # '''


if __name__ == '__main__':
    test_corners_funcSolvePnP()
    # print objp
    pass