import numpy as np
import cv2

#Input the name of the file that we want to operate on regions of interest (ROI)
filename = input("Please enter filename: ")

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
#With waitKey function the image will remain open for 10000 milliseconds 
#After 10000 milliseconds the image will be close because destroyAllWindows function will close the opened windows and in this case the opened image
cv2.imshow("ROI", ROI)
cv2.waitKey(10000)
cv2.destroyAllWindows()