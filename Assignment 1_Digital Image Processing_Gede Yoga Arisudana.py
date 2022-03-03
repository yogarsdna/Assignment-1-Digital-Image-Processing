import numpy as np
import cv2

#Pass the name of the file that we want to operate on regions of interest (ROI)
#We write Lenna.bmp because we are given the Lenna.bmp image
filename = "Lenna.bmp"

#Read the file or image in this case
img = cv2.imread(filename, -1)

#Decide the x, y and also the rows and columns for the image
ROI_x,ROI_y = eval(input("Enter (x, y) for ROI: "))
ROI_nr, ROI_nc = eval(input("Enter (rows, columns) for ROI: "))

#Calculate the x and y for the image by adding the previous function
#ROI_x will add x and rows
#ROI_y will add y and columns
ROI = img[ROI_x: ROI_x + ROI_nr, ROI_y: ROI_y + ROI_nc]

#Show the image that have been operated on regions of interest (ROI)
#With the 0 passed in the argument in waitKey function, the image will remain open until any key is pressed
#Using destroyAllWindows function, we can close the window that previously open the image
cv2.imshow("ROI", ROI)
cv2.waitKey(0)
cv2.destroyAllWindows()
