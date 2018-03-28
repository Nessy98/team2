import cv2

from analyzer.BaseAnalyzer import BaseAnalyzer

cap = cv2.VideoCapture(0)
cap.set(5, 1)
cap.set(3, 480)  # WIDTH
cap.set(4, 272)  # HEIGHT

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

class PostureAnalyzer(BaseAnalyzer):
    def has_exception(self):
        return not self.__is_person_in_frame()

    def __is_person_in_frame(self):

        
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    	personInFrame = face_cascade.detectMultiScale(gray, 1.3, 5)
	
	if len(personInframe) == 1:
		return True
	else:
		return False


