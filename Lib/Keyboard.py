import cv2
from cvzone.HandTrackingModule import HandDetector
from button import Button
from time import sleep
from pynput.keyboard import Key,Controller
# import SendKeys

def mainfun():
        keyboard = Controller()

        capture = cv2.VideoCapture(0)
        capture.set(3, 1360)
        capture.set(4, 720)

        detector = HandDetector(detectionCon=0.8, maxHands=2)

        button_list = []
        keys = [["1", "2", "3", "4", "5", "6", "7", "8", "9", "0","Clear"],
                ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]"],
                ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'"],
                ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/","Enter"],
                ["Space","close"]
                ]



        for i in range(len(keys)):
            for x, k in enumerate(keys[i]):
                button_list.append(Button((100*x+50, 100*i+50), k))

        lmList1 = []
        lmList2 = []
        while True:
            success, img = capture.read()
            hands, img = detector.findHands(img)
            flag=0
            count=0
            if hands:
                # Hand 1
                hand1 = hands[0]
                lmList1 = hand1['lmList']
                bbox1 = hand1['bbox']
                fingers1 = detector.fingersUp(hand1)

                if len(hands) == 2:
                    # Hand 2
                    hand2 = hands[1]
                    lmList2 = hand2['lmList']
                    bbox2 = hand2['bbox']
                    fingers2 = detector.fingersUp(hand2)

            for obj in button_list:
                img = obj.draw_button(img)

            if lmList1:
                for obj in button_list:
                    x, y = obj.pos
                    w, h = obj.size
                    if x < lmList1[8][0] < x+w  and y < lmList1[8][1] < y+h:
                        cv2.rectangle(img, obj.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, obj.text, (x + 20, y + 65), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255),
                                    5)
                        l,_,_ = detector.findDistance((lmList1[8][0],lmList1[8][1]), (lmList1[12][0],lmList1[12][1]),img)

                        if l<40:
                            cv2.rectangle(img, obj.pos, (x + w, y + h), (240, 165, 0), cv2.FILLED)
                            cv2.putText(img, obj.text, (x + 20, y + 65), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255),
                                    5)
                            if(obj.text!="Clear" and obj.text!="Enter"and obj.text!="Space" and obj.text!="close"):
                                # if flag==0:
                                    # for i in kbd:
                                    #     if obj.text==i:
                                keyboard.press(obj.text)
                                # else:
                                #     keyboard.press(obj.text)

                                sleep(0.3)
                            elif obj.text=="Clear":
                                keyboard.press(Key.backspace)
                                sleep(0.3)
                            elif obj.text=="Enter":
                                keyboard.press(Key.enter)
                                sleep(0.3)
                            elif obj.text=="Space":
                                keyboard.press(Key.space)
                                sleep(0.3)
                            elif obj.text=="close":
                                capture.release()
                                cv2.destroyAllWindows()
                                break


                            # elif obj.text =="Caps-Lock":
                            #     keyboard.press(Key.caps_lock)
                            #     flag=1
                            #     if flag==1:
                            #         keyboard.release(Key.caps_lock)
                            #         flag=0
                            #     sleep(0.3)



            cv2.imshow("keyboard", img)
            cv2.waitKey(2)
mainfun()
