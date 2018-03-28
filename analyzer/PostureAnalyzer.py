import cv2
import numpy as np

from analyzer.BaseAnalyzer import BaseAnalyzer
cap = cv2.VideoCapture(0)
cap.set(5, 1)
cap.set(3, 480)  # WIDTH
cap.set(4, 272)  # HEIGHT

class PostureAnalyzer(BaseAnalyzer):
    
    def has_exception(self):
        return not self.__is_person_in_frame()

    def __is_person_in_frame(self):

        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")        
	ret, frame = cap.read()

    	gray = cv2.cvtColor(frame, 6)
    	personInFrame = face_cascade.detectMultiScale(gray, 1.3, 5)
	
	if len(personInFrame) == 1:
		return True
	else:
		return False


