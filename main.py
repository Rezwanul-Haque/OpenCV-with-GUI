# importing packages
import cv2
import numpy as np
# importing packages end


img = cv2.imread("image/demoImage.jpg", 1) # loading image
cv2.imshow("Demo Image", img) # window name + the image to show  ## cv2.imshow(windowname, imagename)

# Must have this code for all cv2 application
cv2.waitKey()
cv2.destroyAllWindows()
# Must have this code for all cv2 application end
