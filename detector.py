
import numpy as np
import cv2


class Detector (object):


	#~ def __init__(self):
		#~ super(face_recog,self).__init__()
	@staticmethod
	def detect():



			cam=cv2.VideoCapture(0)

			FaceDetect= cv2.CascadeClassifier('face.xml')
			w=400
			h=400
			cam.set(3,w)
			cam.set(4,h)




			rec=cv2.createLBPHFaceRecognizer();
			rec.load("trainer/trainer.yml")
			id=0
			font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,3,1,0,1)
			while(True):
				ret, img = cam.read()
				gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

				faces = FaceDetect.detectMultiScale(gray, 1.3, 5)
				if(len(faces)!=0):
					for (x,y,w,h) in faces :
						cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
						id,conf=rec.predict(gray[y:y+h,x:x+w])
						if(id == 678):
							person="kaustubh"


						#if (id == 13):
						#	person = "swapnil"
						if (id == 345):
							person = "Ramesh"
						elif (id == 123):
							person = "Vishal"
						#elif (id == 11):
							#person = "kaustubh"

					        #else:
						    #person = "unkown"
						cv2.cv.PutText(cv2.cv.fromarray(img),str(person), (x,y+h),font,255);
					ID= id




				cv2.imshow('frame',img)
				if cv2.waitKey(1) & 0xFF == ord('q'):
					break
			return ID

			cap.release()
			cv2.destroyAllWindows()

