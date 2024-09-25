import cv2
from playsound import playsound

webcam = cv2.VideoCapture(0)

while True:
    _, im1 = webcam.read()
    _, im2 = webcam.read()
    
    diff = cv2.absdiff(im1, im2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)
    
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        playsound('audio(1).wav') 

    cv2.imshow("Security Camera", thresh)
    
    if cv2.waitKey(10) == 27: 
        break
webcam.release()
cv2.destroyAllWindows()

