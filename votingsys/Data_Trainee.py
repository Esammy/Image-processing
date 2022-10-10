import cv2
import os
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#recognizer = cv2.face.EigenFaceRecognizer_create()

def getImageAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    Ids = []
    #print()
    #imagePaths[0]
    
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        Id = int(os.path.split(imagePath)[-1].split(".")[0].split("_")[0])
        faces = face_cascade.detectMultiScale(imageNp)
        
        for (x, y, w, h) in faces:
            faceSamples.append(imageNp[y:y + h, x:x + w])
            Ids.append(Id)
            #cv2.imshow("Adding faces for Training",imageNp)
    return faceSamples, Ids

faces, Ids = getImageAndLabels("Student Dataset/")

def train(recognizer=recognizer,faces=faces,Ids=Ids):
    recognizer.train(faces, np.array(Ids))
    print("Successfully Trained")
    recognizer.save('Trainer/Trainer.yml')

train()


