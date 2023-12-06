import cv2
load = cv2.imread('D:/pengolahan citra/ukutan/nisa.jpg', 1)
print(load.shape)
print('width:', load.shape[1])
print('height:', load.shape[0])
print('size:', load.shape)