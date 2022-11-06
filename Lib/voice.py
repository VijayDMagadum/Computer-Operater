from Speak import Say
from Listen import Listen
import os
import random

Assistan_Name = "Karen"
emails = {
    # Your Emails Goes here like
    #'test' : 'test@gmail.com'
}
song_folder_path = ''# Like "D:\\SongFolder"
music_folder_path = ''# Like "D:\\MusicFolder"
Chrome_Path = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\brave.exe'# Like "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
Visual_Studio_Code_Path = '"C:\\Users\\mrstr\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"' # Like "C:\Users\Hanzla\AppData\Local\Programs\Microsoft VS Code\Code.exe"
VLC_Path = 'D:\\VLC\\vlc.exe'# Like "C:\Program Files\VideoLAN\VLC\vlc.exe"
Everything_Path = 'C:\\Program Files\\Everything\\Everything.exe'# Like "C:\Program Files\Everything\Everything.exe"


def exit():
    Say("GoodBye Sir! Hope to see you soon.")

def youtube_search(term):
    import webbrowser
    import pywhatkit as kit
    result = "https://www.youtube.com/results?search_query=" + term
    chromepath = Chrome_Path
    webbrowser.get(chromepath).open_new_tab(result)
    Say('your result has been searched')
    kit.playonyt(term)

def google_search(term):
    import webbrowser
    result = "https://www.google.com/search?q=" + term
    chromepath = Chrome_Path
    webbrowser.get(chromepath).open_new_tab(result)
    Say('your result has been searched')

def wishme():
    import datetime
    hour = int(datetime.datetime.now().hour)
    if  24 > hour < 4 :
        Say('pleasent night sir!')

    elif  12 > hour > 4 :
        Say('good morning!')

    elif  18 > hour < 12 :
        Say('good afternoon!')

    else:
        Say('good evening, hope you enjoyed your day sir!')

    Say(f"Hello Sir, {Assistan_Name} Here to Help You!")

def Task_exe():
    if __name__ == "__main__" :
        wishme()
        print("In Function")
        while True:
            # query = input("Enter the command")
            query = Listen().lower()
            if 'open youtube' in  query:
                import webbrowser
                webbrowser.open('youtube.com')

            elif 'search youtube' in query:
                Say('sir, what should i search on youtube')
                term = Listen().lower()
                term = term.replace("search for","")
                youtube_search(term)

            elif 'search google' in query:
                Say('sir, what should i search on google')
                term = Listen().lower()
                term = term.replace("search for","")
                google_search(term)

        # _________________   to search wikipedia   ______________

            elif 'wikipedia' in query or 'search wikipedia' in query:
                import wikipedia
                Say('What should i search on wikipedia')
                query = Listen().lower()
                query = query.replace('wikipedia', '').replace("search for","").replace("who is","").replace("what is","")
                result = wikipedia.summary(query, sentences=3)
                Say('According to wikipedia')
                Say(result)

    # _________________   to open google   ______________

            elif 'open google' in query:
                webbrowser.open("google.com")

    # _________________   to open facebook   ______________

            elif 'open facebook' in query:
                webbrowser.open("facebook.com")

    # _________________   to open instagram   ______________

            elif 'open instagram' in query:
                webbrowser.open("instagram.com")

    # _________________   to open gmail   ______________

            elif 'open gmail' in query:
                webbrowser.open("gmail.com")

    # _________________   to open stackoverflow   ______________

            elif 'open stack overflow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'open chrome' in query:
                Say('opening chrome')
                os.startfile(Chrome_Path)

            elif 'open code' in query:
                Say('opening code')
                os.startfile(Visual_Studio_Code_Path)

            elif 'open vlc' in query:
                Say('opening vlc')
                os.startfile(VLC_Path)

            elif 'open everything' in query:
                Say('opening everything')
                os.startfile(Everything_Path)

            elif 'open notepad' in query:
                Say('opening notepad')
                os.startfile("C:\\Windows\\system32\\notepad.exe")

            elif 'open command' in query:
                Say('opening command prompt')
                os.startfile("C:\\Windows\\system32\\cmd.exe")

            elif 'open calculator' in query:
                Say('opening calculator')
                os.startfile("C:\\Windows\\system32\\calc.exe")

    # _________________   to play songs   ______________

            elif 'play song' in query:
                song_dir = song_folder_path
                songs = os.listdir(song_dir)
                rsd = random.choice(songs)
                os.startfile(os.path.join(song_dir, rsd))

    # _________________   to play musics   ______________

            elif 'play music' in query:
                mpath = music_folder_path
                musics = os.listdir(mpath)
                rmd = random.choice(musics)
                os.startfile(os.path.join(mpath, rmd))

    # _________________   saying hello   ______________

            elif 'hello' in query:
                Say('Hi, sir!')

    # _________________   to check our location   ______________

            elif 'where' in query or 'my location' in query:
                Say('wait sir, let me check...')
                try:
                    import requests
                    ipaddress = requests.get('https://api.ipify.org').text
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipaddress+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json() # data in form of json
                    city = geo_data['city']
                    region = geo_data['region']
                    country = geo_data['country']
                    Say(f'we are in {city} city of {region} located in {country}')
                except:
                    Say("sorry sir, i can't locate where you are currently due to network issues")
                    pass

    # _________________   For Taking screenshot   ______________
            elif 'take screenshot' in query or 'capture screen' in query:
                import pyautogui
                Say('sir, please tell me the name for this screenshot')
                name = Listen().lower()
                Say('taking screenshot. please, hold the screen for few seconds')
                #datetime.time.  # delay due to the status of internet
                img = pyautogui.screenshot()
                img.save(f"Libraries\\Documents\\{name}.png")
                Say('i am done sir, screenshot is saved in windows document folder. now i am ready for next command')

            elif "what's my ip" in query or 'my ip address' in query:
                from requests import get
                ip = get('https://api.ipify.org').text
                Say(f"your ip address is {ip}")

            elif 'tell me a joke' in query or 'joke' in query:
                import pyjokes
                joke = pyjokes.get_joke()
                Say(joke)

            elif 'thanks' in query or 'thank you' in query:
                Say('its my pleasure sir,')

    # _________________   for note pad   ______________

            elif 'close notepad' in query:
                Say('closing notepad')
                os.system("taskkill /f /im notepad.exe")

            elif 'close chrome' in query:
                Say('closing chrome')
                os.system("taskkill /f /im chrome.exe")

            elif 'close code' in query:
                Say('closing code')
                os.system("taskkill /f /im Code.exe")

            elif 'close vlc' in query:
                Say('closing vlc')
                os.system("taskkill /f /im vlc.exe")

            elif 'close everything' in query:
                Say('closing search everything')
                os.system("taskkill /f /im Everything.exe")

            elif 'close calculator' in query:
                Say('closing calculator')
                os.system("taskkill /f /im calculator.exe")

            elif 'close command' in query:
                Say("Closing Command prompt")
                os.system("taskkill /f /im cmd.exe")

    # ===============================================   system commands   =====================================================

    # _________________   system shutting command   ______________

            elif 'shutdown the system' in query:
                Say('do you really want to shutdown the system')
                while True:
                    reply = Listen().lower()
                    if 'yes' in reply:
                        Say('shutting down the system')
                        os.system('shutdown /s /t 5')
                    else:
                        break

            elif 'restart the system' in query:
                Say('do you really want to restart the system')
                while True:
                    reply = Listen().lower()
                    if 'yes' in reply:
                        Say('restarting the system')
                        os.system('shutdown /r /t 5')
                    else:
                        break


            elif 'sleep the system' in query:
                Say('do you really want to sleep the system')
                while True:
                    reply = Listen().lower()
                    if 'yes' in reply:
                        Say('sleeping the system')
                        os.system('rundll32.exe powrprof.dll, SetSuspendState 0, 1, 0')
                    else:
                        break

            elif 'log off the system' in query:
                Say('do you really want to log off the system')
                while True:
                    reply = Listen().lower()
                    if 'yes' in reply:
                        Say('logging off the system')
                        os.system('shutdown -1')
                    else:
                        break

    # _________________   switcing window   ______________

            elif 'switch window' in query or 'switch the window' in query:
                import time
                pyautogui.keydown("alt")
                pyautogui.press('tab')
                time.sleep(2)
                pyautogui.keyup('alt')

   # _________________   to check time   ______________

            elif 'the time' in query or 'time' in query:
                import datetime
                Time = datetime.datetime.now().strftime("%I:%M %p")
                Say(f"The time is {Time}")

    # _________________   to check date   ______________

            elif 'the date' in query or 'date' in query:
                import datetime
                todaydate = datetime.datetime.now().date()
                Say(f"Sir, the date is {todaydate}")

            elif 'the day' in query or 'day' in query:
                import datetime
                day = datetime.datetime.now().strftime("%A")
                Say(f"Today is {day}")

            elif 'open drive d' in query:
                Say('Opening the D drive')
                path_to_d = "D:\\"
                os.startfile(path_to_d)

            elif 'open drive c' in query:
                Say('Opening the C drive')
                path_to_c = "C:\\"
                os.startfile(path_to_c)

            elif 'who made you' in query:
                Say("Hanzla Anjum Is The Creator Of Me! I Love him.")

            elif 'temprature' in query:
                import bs4 as BeautifulSoup
                Say('sir, tell me the place')
                search = Listen().lower()
                if search in query:
                    url = "https://www.google.com/search?q=" + {search}
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html parser")
                    temp = data.find("Div", class_="BNeawe").text
                    Say(f'sir, the temprature in {search} is {temp}')
                elif 'outside' in query:
                    Search = "Temprature in Hasilpur"
                    url = "https://www.google.com/search?q=" + {Search}
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html parser")
                    temp = data.find("Div", class_="BNeawe").text
                    Say(f'sir, the {search} is {temp}')

            elif 'run speed test' in query or 'test speed' in query or 'test internet speed' in query:
                import speedtest
                Say('testing the speed of internet. plese wait,')
                st = speedtest.Speedtest()
                dl_spd = st.download()
                up_spd = st.upload()
                Say(f'your downloading speed is {dl_spd} bits per second and the uploading speed is {up_spd} bits per second')

            elif 'how much' in query or 'how many' in query or 'battery' in query:
                import psutil
                battery = psutil.sensors_battery()
                percentage = battery.percent
                Say(f'sir, our system has {percentage} percent of battery.')
                if percentage >= 60:
                    Say('we have enough power to continue our work')
                elif percentage>= 45 and percentage<= 60:
                    Say('sir, you should connect the charger')
                elif percentage<=15 and percentage<=30:
                    Say('sir, we do not have enough power to continue our work. please, connect the charger ')
                elif percentage<=15:
                    Say('sir, our system has very low power, please connect the charger, other wise the system will shutdown soon.')

            elif 'volume up' in query or 'increase volume' in query:
                pyautogui.press("volumeup")

            elif 'volume down' in query or 'decrease volume' in query:
                pyautogui.press("volumedown")

            elif 'stop volume' in query or 'stop sound' in query:
                pyautogui.press("volumemute")

            elif 'send mail' in query or 'send email' in query:
                from email.mime.text import MIMEText
                from email.mime.multipart import MIMEMultipart
                import smtplib
                sender_email = 'hanzlaanjum0012@gmail.com'
                sender_password =  '0123@Tered'
                Say('tell me the name of the person you want to send mail')
                name = Listen()
                email = emails[f'{name}']
                send_to_mail = email
                Say('sir, what is the subject of the email')
                query = Listen().lower()
                subject = query
                Say('what is the message of email')
                query2 = Listen().lower()
                message = query2

                msg = MIMEMultipart()
                msg['from'] = email
                msg['to'] = send_to_mail
                msg['subject'] = subject
                msg.attach(MIMEText(message, 'plain'))

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(email, send_to_mail, message)
                server.close()
                Say(f'Email has been sent to the {name} at {send_to_mail}')

            elif 'exit' in query or 'stop' in query:
                exit()
                break
print("hello")
Task_exe()
