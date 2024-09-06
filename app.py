from vosk import Model,KaldiRecognizer
import speech_recognition as sr
import pyaudio
import pyttsx3
import cv2
import face_recognition
import os
import numpy as np
import json
import time
from datetime import datetime,date
from num2words import num2words
import detect
import cv2



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
print(voices)
engine.setProperty('voice', voices[1].id)
# Encoding--------------------------------------------------
path = "C:\\Users\\jinka\\OneDrive\\Desktop\\images"
images = []
classNames = []
mylist = os.listdir(path)
print(mylist)
for cl in mylist:
    curimg = cv2.imread(f'{path}/{cl}')
    images.append(curimg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEncodings(images)
print("encoding completed")
# -----------------------------------------------------------------

# img = r"C:\Users\jinka\Downloads\Screenshot 2022-12-22 201121.png"
img = r"C:\Users\jinka\Downloads\Screenshot 2022-12-22 212543.png"
img = r"C:\Users\jinka\OneDrive\Documents\Pictures\Camera Roll 1\WIN_20221023_17_30_18_Pro.jpg"

# -------------------------------------------------------------------



p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')

recognizer = sr.Recognizer()

for i in range(0, numdevices):
    if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

model = Model(r"F:\files\ECS PROJECT\vosk-model-en-in-0.5\vosk-model-en-in-0.5")
# model = Model(r"F:\files\ECS PROJECT\vosk-model-small-en-in-0.4\vosk-model-small-en-in-0.4")

test1 = 0
test2 = 0
test3 = 0

rc = KaldiRecognizer(model,16000)


mic = pyaudio.PyAudio()
stream = mic.open(rate=16000,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=8192,input_device_index=0)
stream.start_stream()

while True:
    try:
        data = stream.read(4096, exception_on_overflow = False)
        if (rc.AcceptWaveform(data)):
            res = json.loads(rc.Result())
            print(res['text'])
            if (res['text'].find('lena') != -1 or res['text'].find('leena') != -1 or res['text'].find('lina') != -1 or res['text'].find('nancy'
                                                                                                                                        '') != -1):
                print("inside nancy")
                engine.say("Yes How can i help you")
                engine.runAndWait()
                # audio = b''
                # for i in range(0, int(16000 / 4096 * 4)):
                #     print("||||")
                #     data = stream1.read(4096, exception_on_overflow = False)
                #     audio = audio + data
                # stream1.stop_stream()
                # for i in range(0, int(16000 / 8192 * 10)):
                #     # print("111")
                #     data = stream.read(4096,exception_on_overflow = False)
                #     audio = audio + data
                # audio = stream.read(4096, exception_on_overflow = False)
                # print(audio)

            if (res['text'].find('time') != -1):
                now = datetime.now()
                hour = int(now.strftime("%I"))/1
                print(hour)
                min = int(now.strftime("%M"))/1
                str = "it is " + num2words(hour) + " " + num2words(min) + " " + now.strftime("%p") + " now"
                engine.say(str)
                engine.runAndWait()
            elif res['text'].find('date') != -1  or res['text'].find("today's") != -1:
                now = date.today()
                            # str = "it is " + num2words(int(now.strftime("%I")), to='ordinal') + " " + num2words(
                            #     int(now.strftime("%M")), to='ordinal') + " " + now.strftime("%p") + " now"
                engine.say(now.strftime("%B %d, %Y"))
                engine.runAndWait()
            elif (res['text'].find('read') != -1  or res['text'].find('text') != -1 or test1==1 ):
                print("casasc")

                # import pytesseract
                # from PIL import Image
                # import pyttsx3
                #
                # pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
                cap = cv2.VideoCapture(0)
                # cap = cv2.VideoCapture(0)

                success, img = cap.read()
                success, img = cap.read()
                success, img = cap.read()
                cap.release()
                # img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
                os.chdir(r"F:\files\ECS PROJECT\main_file")
                cv2.imwrite("image123.png", img)

                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                # result = pytesseract.image_to_string(img)
                # print("TEXT RESULT"  ,result)

                import easyocr

                engine.say("Please wait for a second")
                engine.runAndWait()
                reader  = easyocr.Reader(['en','ch_tra'])

                try:
                    result = reader.readtext(img)
                    print(result[0][1])
                    res=result[0][1]
                    if (len(res) > 2):
                        print(res)
                        engine.say(res)
                        engine.runAndWait()
                    else:
                        engine.say(" I can't find any text hear")
                        engine.runAndWait()
                except:
                    engine.say(" I can't find any text hear")
                    engine.runAndWait()
                # if(len(res)>2):
                #     print(res)
                #     engine.say(res)
                #     engine.runAndWait()
                # else:
                #     engine.say(" I can't find any text hear")
                #     engine.runAndWait()

            elif (res['text'].find('who') != -1  or res['text'].find('person') != -1 or res['text'].find('persons') != -1 or test2==1):
                cap = cv2.VideoCapture(0)
                # cap = cv2.VideoCapture(0)

                time.sleep(1)
                success, img = cap.read()
                success, img = cap.read()
                success, img = cap.read()
                cap.release()
                # img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
                imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                os.chdir(r"F:\files\ECS PROJECT\main_file")
                cv2.imwrite("image123.png", img)

                facesCurFrane = face_recognition.face_locations(imgS)
                land_marks = face_recognition.face_landmarks(imgS, facesCurFrane)
                encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrane)
                if len(facesCurFrane) > 0:
                    for encodeFace, faceLoc, landmark in zip(encodesCurFrame, facesCurFrane, land_marks):
                        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                        #         print(faceDis,matches)

                        matchIndex = np.argmin(faceDis)
                        if faceDis[matchIndex] < 0.50:
                            name = classNames[matchIndex].upper()
                        else:
                            name = 'Unknown'

                        print(name)
                        str = name.lower() + " in front of you"
                        engine.say(str)
                        engine.runAndWait()
                else:
                    engine.say("No people in front of you")
                    engine.runAndWait()
                print("IN who cls  -------------------------------")
            elif (res['text'].find('objects') != -1  or res['text'].find('objects') != -1 or test3==1):
                cap = cv2.VideoCapture(0)
                # cap = cv2.VideoCapture(0)

                success, img = cap.read()
                success, img = cap.read()
                success, img = cap.read()
                cap.release()
                # img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
                imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                os.chdir(r"F:\files\ECS PROJECT\main_file")
                cv2.imwrite("image123.png", img)
                engine.say("Please wait for a second")
                engine.runAndWait()
                ans = detect.ans()
                ans+=" are in the image"
                engine.say(ans)
                engine.runAndWait()





    except :
        print("error.....................")
        rc = KaldiRecognizer(model, 16000)

        mic = pyaudio.PyAudio()
        stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192,
                          input_device_index=0)
        stream.start_stream()

