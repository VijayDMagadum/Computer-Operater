# import everything from tkinter module
from tkinter import *
import os
import sys


# import virtualmouse as vmouse
# create a tkinter window
root = Tk()

# Open window having dimension 100x100
root.geometry('550x550')
root.title("Computer Operator")
root.configure(bg='black')
# Create a Button
bg = PhotoImage(file = r"resources/background.png")
micimg = PhotoImage(file = r"resources/mic.png")
mouseimg = PhotoImage(file = r"resources/mouse.png")
keyboardimg = PhotoImage(file = r"resources/key.png")
doodleimg =PhotoImage(file = r"resources/paint.png")
cameraimg =PhotoImage(file = r"resources/camera.png")
cameraimg1 =PhotoImage(file = r"resources/camera1.png")


#stopimg=PhotoImage(file = r"../final_project/close.png")
def mic():
    # import Lib.voice as v
    # v.Task_exe()
    import Lib.demo1

    # voice.Task_exe()
def mouse():
    import Lib.Virtual_Mouse as vrm

def keyboard():
    import Lib.Keyboard as ky
    ky.mainfun()
def canvass():
    import canvas
def camera():
    import Lib.facerecognition2 as FL
    print(FL.status())
def camera1():
    import Lib.facerecognition





# background image
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)

voice_assistant = Button(root, text = 'Voice Assistant ',image = micimg , bd = '5', command = mic)
virtual_mouse = Button(root, text = 'Virtual Mouse ',image = mouseimg, bd = '5', command = mouse)
virtual_keyboard = Button(root, text = 'Virtual Keyboard',image=keyboardimg, bd = '5', command = keyboard)
virtual_doodle = Button(root, text = 'Virtual Doodle ',image=doodleimg,bd = '5', command = canvass)
Camera = Button(root, text = 'Virtual camera ',image=cameraimg,bd = '5', command = camera)
Camera1 = Button(root, text = 'Virtual camera1 ',image=cameraimg1,bd = '5', command = camera1)



label2 = Label( root, text="Voice_Assistant")
label2.place(x = 28, y = 470)
label3 = Label( root, text="VR-Mouse")
label3.place(x = 171, y = 470)
label4 = Label( root, text="VR-Keyboard")
label4.place(x = 326, y = 470)
label5 = Label( root, text="VR-Canvas")
label5.place(x = 471, y = 470)
label6 = Label( root, text="Face-Lock")
label6.place(x = 248, y = 95)
label7 = Label( root, text="Signup")
label7.place(x = 498, y = 55)
Camera.place(x=250, y=50)
Camera1.place(x=500, y=5)

# label7 = Label( root, text="Face-Lock")
# label7.place(x = 248, y = 95)


# Set the position of button on the top of window.
voice_assistant.place(x=40, y=400)
virtual_mouse.place(x=175, y=400)
virtual_keyboard.place(x=330, y=400)
virtual_doodle.place(x=475, y=400)




root.mainloop()
