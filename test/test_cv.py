import cv2
print dir(cv2)
for i in dir(cv2):
    if 'creat' in i:
        print i