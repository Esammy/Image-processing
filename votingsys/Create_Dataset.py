import cv2
import os
import time

class ColectImages():
    def assure_path_exists(path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            os.makedirs(dir)

    cap = cv2.VideoCapture(1)

    face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def reg():
        print("NOTE: Once the camera comes up, wait for 10sec and press 'q' to quite and save")
        name, face_id =input('Enter your name: '), input('Enter your Id: ')
        print('Saving images...')
        return name, face_id

    name, face_id = reg()

    def face_detection(cap=cap, name=name, face_id=face_id):
    
        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray,
                                                scaleFactor=1.1,
                                                minNeighbors=5,
                                                minSize=(60,60),
                                                flags=cv2.CASCADE_SCALE_IMAGE)
            for i in range(50):

                for (x,y,w,h) in faces:
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

                    image_frame = gray[y:y + h, x:x + w]

                    
                    cv2.imwrite('Student Dataset/' + str(face_id) +'_'+ str(i)+'.jpg', image_frame)
                    time.sleep(1)

                    cv2.imshow('frame', frame)
                c = cv2.waitKey(1)
                if c == ord('q'):
                    print('Image saved successfully')
                    break
            if c == ord('q'):
                print('Image saved successfully')
                break
    face_detection()

    cap.release()
    cv2.destroyAllWindows()


def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

img_dataset = ['Student Dataset/','Trainer/']
for folder in img_dataset:
    assure_path_exists(folder)

cap = cv2.VideoCapture(1)

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def reg():
    print("NOTE: Once the camera comes up, wait for 10sec and press 'q' to quite and save")
    name, face_id =input('Enter your name: '), input('Enter your Id: ')
    print('Saving images...')
    return name, face_id
name, face_id = reg()

def face_detection(cap=cap, name=name, face_id=face_id):

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray,
                                              scaleFactor=1.1,
                                              minNeighbors=5,
                                              minSize=(60,60),
                                              flags=cv2.CASCADE_SCALE_IMAGE)
        for i in range(50):

            for (x,y,w,h) in faces:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

                image_frame = gray[y:y + h, x:x + w]

                
                cv2.imwrite('Student Dataset/' + str(face_id) +'_'+ str(i)+'.jpg', image_frame)
                time.sleep(1)

                cv2.imshow('frame', frame)
            c = cv2.waitKey(1)
            if c == ord('q'):
                print('Image saved successfully')
                break
        if c == ord('q'):
            print('Image saved successfully')
            break
face_detection()

cap.release()
cv2.destroyAllWindows()
