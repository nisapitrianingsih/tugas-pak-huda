import cv2

load=cv2.imread('D:/pengolahan citra/resize/adek.jpeg', 1)
size_x, size_y = load.shape[1]*2, load.shape[0]*2
new_image = cv2.resize(load,(size_x, size_y))
cv2.imshow('foto asli', load)
cv2.imshow('foto baru', new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
