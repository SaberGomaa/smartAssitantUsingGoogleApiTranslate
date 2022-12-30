import os
import subprocess
import sys
import time
from windows_tools.installed_software import get_installed_software

# importing the pygame library
import pygame
import pygame.camera
import pyttsx3
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('detach', True)


engine = pyttsx3.init()



#covert Text to speech

# Import the required module for text
# to speech conversion

# This module is imported so that we can
# play the converted audio

# The text that you want to convert to audio
txtbeforeLiten = 'Please say somthing'
txtafterLiten = 'sir you said'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should

def takingImage():
    # initializing  the camera
    pygame.camera.init()

    # make the list of all available cameras
    camlist = pygame.camera.list_cameras()

    # if camera is detected or not
    if camlist:

        # initializing the cam variable with default camera
        cam = pygame.camera.Camera(camlist[0], (640, 480))

        # opening the camera
        cam.start()

        # capturing the single image
        image = cam.get_image()

        # saving the image
        pygame.image.save(image, "camImage.jpg")

        listenfun("Image taked do you want to show it")
    # if camera is not detected the moving to else part
    else:
        print("No camera on current device")

def showImage():
    # activate the pygame library .
    pygame.init()
    X = 600
    Y = 600

    # create the display surface object
    # of specific dimension..e(X, Y).
    scrn = pygame.display.set_mode((X, Y))

    # set the pygame window name
    pygame.display.set_caption('image')

    # create a surface object, image is drawn on it.
    imp = pygame.image.load("camImage.jpg").convert()

    # Using blit to copy content from one surface to other
    scrn.blit(imp, (0, 0))

    # paint screen one time
    pygame.display.flip()
    status = True
    while (status):

        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for i in pygame.event.get():

            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if i.type == pygame.QUIT:
                status = False

    # deactivates the pygame library
    pygame.quit()
    listenfun("Do you want any thing else ali basha")

def getSofwareLocation(softwareName):
    print(os.system('where is '+softwareName))

def getSystemInstalledSoftware(softwareName):
    softwareChosedName=" "
    for software in get_installed_software():
        # if softwareName in software["name"]:
        if (software["name"].find(softwareName)==0):
            engine.say("ali basha i found "+software["name"]+" do you want to open")
            engine.setProperty('rate', 0)
            engine.setProperty('volume', 0.2)
            engine.runAndWait()
            print(software["name"])
            print(type(software["name"]))
            reco=getrecognize()
            if(reco.find("yes")==0):
                print("done")
                softwareChosedName=software["name"]
                break
            # print(getSofwareLocation(software['name']))
    getSofwareLocation(softwareChosedName)

def getOreder(text):
    if "google" in text.lower():
        getSystemInstalledSoftware("Google")
        print("opening google..")
        # driver = webdriver.Chrome()
        # driver.get("https://www.google.com")
        # listenfun("Do you want any thing else ali basha")
        # time.sleep(60)
    elif "facebook" in text.lower():
        print("opening facebook..")
        driver = webdriver.Chrome()
        driver.get("https://www.facebook.com")
        time.sleep(60)
    elif "notepad" in text.lower():
        print("opening notepad..")
        subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
    elif "image" in text.lower():
        print("Taking Image..")
        takingImage()
    elif "yes" in text.lower():
        print("showing Image..")
        showImage()
    elif "exit" in text.lower():
        print("Exit..")
        engine.say("ok goodbye ali basha")
        engine.setProperty('rate', 0)
        engine.setProperty('volume', 0.2)
        engine.runAndWait()
        sys.exit()
    elif "happy" in text.lower():
        print("happy birthday saber basha")
        engine.say("happy birthday saber basha")
        engine.setProperty('rate', 0)
        engine.setProperty('volume', 0.2)
        engine.runAndWait()
        listenfun("Do you want any thing else ali basha")
    else:
        print("re-listen")
        listenfun("I do not understand you  say it again")


def listenfun(text):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print(text)
        engine.say(text)
        engine.setProperty('rate', 0)
        engine.setProperty('volume', 0.2)
        engine.runAndWait()
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        print("Recognizing Now .... ")

        try:
            text=r.recognize_google(audio)
            print("you said "+text.lower())
            getOreder(text)
        except Exception as e:
            print("Error : " +str(e))
            listenfun("I do not understand you  say it again")

def getrecognize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Recognizing Now .... ")

        try:
            text = r.recognize_google(audio)
            print("you said " + text.lower())
        except Exception as e:
            print("Error : " + str(e))

    return text.lower();
def say(text):
    print("from sying method")
    engine.say(text)
    engine.setProperty('rate', 0)
    engine.setProperty('volume', 0.2)
    engine.runAndWait()

listenfun("what do you want ali basha")


