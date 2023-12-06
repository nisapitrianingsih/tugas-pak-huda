import cv2
videoCam = cv2.VideoCapture(0)
while True:
    cond, frame = videoCam.read()
    edge = cv2.Canny(frame, 70, 70)
    cv2.imshow('Edge Detect', edge)
    exit = cv2.waitKey(0) & 0xff
    if exit == ord('q'):
        break
    videoCam.release()
    cv2.destroyAllWindows()