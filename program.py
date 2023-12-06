import cv2 as cv
img = cv.imread("D:\pengolahan citra\gambar.jpg")

cv.imshow("gambar", img)
cv.waitKey(0)
cv.destroyAllWindows()