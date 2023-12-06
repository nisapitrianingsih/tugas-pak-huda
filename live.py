import cv2
vidioCam = cv2.VideoCapture(0)
face = cv2.CascadeClassifier('face-detect.xml')
eye = cv2.CascadeClassifier('eye-detect.xml')
while True:
    cond, frame = vidioCam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2BGR)
    muka = face.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in muka:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 5)
        roi_warna = frame[y:y+h, x:x+w]
        roy_gray = gray[y:y+h, x:x+w]
        mata = eye.detectMultiScale(roi_gray)
        for (mx,my,mw,mh) in mata:
            cv2.rectangle(roi_warna, (mx,my), (mx,my), (mx+mw, my+mh), (255,255,0), 2)
        cv2.imshow('Face and Eye detection', frame)
        k = cv2.waitKey(1)& 0xff
        if k == ord('q')
        break
    vidioCam.release()
    cv2.destroyAllWindows()    