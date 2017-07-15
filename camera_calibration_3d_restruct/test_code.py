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

def test_orb_epipole_geometry():
    img1 = cv2.imread('data/aloeL.jpg', 0)  # queryimage # left image
    img2 = cv2.imread('data/aloeR.jpg', 0)  # trainimage # right image

    orb = cv2.ORB_create()
    kp1 = orb.detect(img1, None)
    kp2 = orb.detect(img2, None)
    kp1, des1 = orb.compute(img1, kp1)
    kp2, des2 = orb.compute(img2, kp2)

    print 'length of kp1 is {0}'.format(len(kp1))
    print 'length of kp2 is {0}'.format(len(kp2))


# SIFT SURF
#     FLANN_INDEX_KDTREE = 0
#     index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)

    FLANN_INDEX_LSH = 6
    index_params = dict(algorithm=FLANN_INDEX_LSH,
                        table_number=6,  # 12
                        key_size=12,  # 20
                        multi_probe_level=1)  # 2
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)
    print matches
    print len(matches)  # 500

    print '---flann obj---'
    print [method for method in dir(flann) if callable(getattr(flann, method))and method[:2] != '__' ]


    good = []
    pts1 = []
    pts2 = []
    # ratio test as per Lowe's paper
    for i, (m, n) in enumerate(matches):

        # print i
        # print m,n
        # if m.distance < 0.8 * n.distance:
        #     good.append(m)
        #     pts2.append(kp2[m.trainIdx].pt)
        #     pts1.append(kp1[m.queryIdx].pt)
        pass

if __name__ == '__main__':
    # test_corners_funcSolvePnP()
    # print objp
    test_orb_epipole_geometry()
    pass