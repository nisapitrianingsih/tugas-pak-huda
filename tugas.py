import cv2
load=cv2.imread('D:/pengolahan citra/ukutan/nisa.jpg', 1)
new_img = cv2.resize(load, (0,0), fx=0.5, fy=0.5)
cv2.imshow('foto asli', load)
cv2.imshow('foto baru', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()