import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret,frame = cap.read()

    cv2.imshow('tmp',frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('tmp.jpg', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()