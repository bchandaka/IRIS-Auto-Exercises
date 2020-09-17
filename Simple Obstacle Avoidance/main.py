import cv2
import numpy as np

img = cv2.imread("obstacle_scene_1.jpg")

cv2.imshow("Original", img)
# TODO: Write obstacle avoidance code here...



#waits for user to press any key 
# (this is necessary to avoid Python from stopping) 
cv2.waitKey(0)  

cv2.destroyAllWindows()