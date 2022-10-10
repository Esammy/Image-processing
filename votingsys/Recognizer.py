import cv2
import numpy as np
import xlsxwriter
import time
from datetime import datetime, date


start = time.time()
period = 8

# datetime object containing current date and time
now = datetime.now()

# Month abbreviation, day and year
today = date.today()
now_date = today.strftime("%b-%d-%Y")
 

now_time = now.strftime("%H:%M:%S")


workbook = xlsxwriter.Workbook('Attendance.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Names')
worksheet.write('B1', 'Present')
worksheet.write('C1', 'Date')
worksheet.write('D1', 'Time')

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

flag = 0
id = 0
filename = 'filename'
dict = {
    'item1':1
    }

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('Trainer/Trainer.yml')

subject = ["", "Sam", "Jame", "Isah"]

cap = cv2.VideoCapture(1)
s_names = []
font = cv2.FONT_HERSHEY_SIMPLEX
ind_num = 1
while True:
        
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,
                                              scaleFactor=1.1,
                                              minNeighbors=5,
                                              minSize=(60,60),
                                              flags=cv2.CASCADE_SCALE_IMAGE)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
        
        gray_face = gray[y:y +h, x:x + w]
        id, conf = recognizer.predict(gray_face)
        print(id, conf)

        if (conf < 85):
            ind_num = ind_num + 1
            if (id == 1):
                id = 'Sam'
                if id not in s_names:
                    
                    worksheet.write('A'+str(ind_num), id)
                    worksheet.write('B'+str(ind_num), 'Yes')
                    worksheet.write('C'+str(ind_num), now_date)
                    worksheet.write('D'+str(ind_num), now_time)
                    s_names.append(id)
                    print(id, ' is present')

            elif (id == 2):
                id = 'James'
                if id not in s_names:
                    worksheet.write('A'+str(ind_num), id)
                    worksheet.write('B'+str(ind_num), 'Yes')
                    worksheet.write('C'+str(ind_num), now_date)
                    worksheet.write('D'+str(ind_num), now_time)
                    s_names.append(id)
                    print(id, ' is present')

            elif (id == 3):
                id = 'Isah'
                if id not in s_names:
                    worksheet.write('A'+str(ind_num), id)
                    worksheet.write('B'+str(ind_num), 'Yes')
                    worksheet.write('C'+str(ind_num), now_date)
                    worksheet.write('D'+str(ind_num), now_time)
                    s_names.append(id)
                    print(id, ' is present')

            else:
                id = 'Unknow, can not recognize'
                print(id)
                flag = flag + 1
                break

            cv2.putText(frame, str(id) + " " + str(conf), (x, y - 10), font, 0.55, (120, 255, 120),1)
        cv2.imshow('frame',frame)
        if flag == 10:
            print("Transaction Blocked")
        if time.time() > start + period:
            break

    c = cv2.waitKey(1)
    if c == ord('q'):
        break
workbook.close()

cap.release()
cv2.destroyAllWindows()
