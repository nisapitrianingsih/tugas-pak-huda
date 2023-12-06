import cv2
img = cv2.imread('D:/pengolahan citra/detektor/salsa.jpeg')
edge = cv2.Canny(img, 70, 70)
cv2.imshow('deteksi edge', edge)
cv2.imshow('original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()