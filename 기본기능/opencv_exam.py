import cv2

#img = cv2.imread("Steve.jfif", 1)

#cv2.imshow("Test", img)
#cv2.waitKey(0)

# 이미지 띄우는 법
cap = cv2.VideoCapture("Changes.webm")

while cap.isOpened():
    success, frame = cap.read()
    if success:
        cv2.imshow('Camera Window', frame)

        key = cv2.waitKey(1) & 0xFF
        if (key == 27):
            break

cap.release()
cv2.destoryAllWindows()
