import cv2 as cv
gambar = cv.imread("D:\\pengolahan citra\\gambar\\nisa.jpg")
imggray = cv.imread("D:\\pengolahan citra\\gambar\\nisa.jpg", 0)
cv.imshow("gambar", gambar)
cv.imshow("gambar", imggray)
cv.waitKey(0)
cv.destroyAllwindows()