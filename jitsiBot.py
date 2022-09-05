from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import tkinter as tk
import threading

from joinMeet import turnMicCamOff, joinNow
from commands import commands

# Handling permission popups and browser window props
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("enable-usermedia-screen-capturing")
opt.add_argument("auto-select-desktop-capture-source=YouTube Music")    #Auto select which screen to share, for now YTM
opt.add_experimental_option('excludeSwitches', ['test-type'])
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1,
})

root = tk.Tk()
root.geometry("500x400")
root.minsize(400, 380)
root.title("Jitsi Music Bot")

#title
heading = tk.Label(root, text="Jitsi Music Bot", font="opensans 20 bold", pady=10)
heading.pack(pady=20)

#description
description = tk.Label(root, text="A simple music bot for Jitsi", font="opensans 10", pady=10)
description.pack()

#Variables
meetLinkVar = tk.StringVar()
chromedriverPathVar = tk.StringVar()
meetLink=""
chromedriverPath=""
global driver

#function
def bot(event):
    if btnText.get()=="Start Bot":
        btnText.set("Bot Started")
        botThread = threading.Thread(target=startBot).start()

def startBot():
    meetLink=(meetLinkVar.get())
    chromedriverPath=(chromedriverPathVar.get())
    
    # Starting browser
    driver= webdriver.Chrome(executable_path=chromedriverPath,options=opt)
    print("browser start")

    driver.get(meetLink)
    driver.implicitly_wait(100)
    time.sleep(1)

    # Joining meet
    turnMicCamOff(driver)
    driver.implicitly_wait(100)
    joinNow(driver)
    driver.implicitly_wait(100)
    time.sleep(1)
    # Accessing chat and following commands
    commands(driver)

#meet link input
meetLinkLabel = tk.Label(root, text="Enter the meet link", font="opensans 10", pady=10)
meetLinkLabel.pack()
meetLinkInput = tk.Entry(root, width=50, textvariable=meetLinkVar)
meetLinkInput.pack()

#path to chromedriver input
chromedriverPathLabel = tk.Label(root, text="Enter the path to chromedriver", font="opensans 10", pady=10)
chromedriverPathLabel.pack()
chromedriverPathInput = tk.Entry(root, width=50, textvariable=chromedriverPathVar)
chromedriverPathInput.pack()

#submitButton
btnText = tk.StringVar()
submitButton = tk.Button(root, textvariable=btnText, font="opensans", bg="#1D76BC", fg="white", height=1, width=12)
btnText.set("Start Bot")
submitButton.pack(pady=20)
submitButton.bind("<Button-1>", bot)

root.mainloop()