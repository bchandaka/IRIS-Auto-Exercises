import cv2
import numpy as np

# Change the image path to test out other images
img = cv2.imread("images/scene1.jpg")

cv2.imshow("Original", img)
# Step 1: Edge Detection
result = cv2.Canny(img, 20, 200)
cv2.imshow("Edges", result)

# Step 2: BottomFill
height, width, channels = img.shape
print(height, width)
for col in range(width):
    for row in range(height-1, 0, -1):
        if (result[row, col] == 255):
            break
        result[row,col] = 255
cv2.imshow("BottomFilled", result)

# Step 3: Erosion
kernel = np.ones((30,30),np.uint8)
result = cv2.erode(result, kernel, iterations=1)
cv2.imshow("Eroded", result)

# Step 4: Find max safe point
maxPoint = (0, height-1)    # bottom row, first column
for col in range(width):
    for row in range(height-1, 0, -1):
        if (result[row, col] == 0):
            break
        if row < maxPoint[1]:
            maxPoint = (col, row)

# Step 5: Draw the maxpoint on the original
center_coordinates = maxPoint
radius = 5
color = (255, 0, 0) # BLue in BGR
thickness = 2
result = cv2.circle(img, center_coordinates, radius, color, thickness)
cv2.imshow("Max Point", result)

# Step 6: Choose robot direction (left if maxpoint in left third, right for right third, straight for middle third)
x = maxPoint[0]
if (x < width/3):
    print("Move to the Left!")
elif (x > (2*width)/3):
    print("Move to the Right!")
else:
    print("Move straight forward!")

#waits for user to press any key 
# (this is necessary to avoid Python from stopping) 
cv2.waitKey(0)  

cv2.destroyAllWindows()