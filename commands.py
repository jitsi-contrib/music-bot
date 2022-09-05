from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from playSong import playSong
from pauseResumeSong import pauseResumeSong
from helpCommand import helpCommand
from exitCommand import exitCommand

def commands(driver):
    driver=driver
    # To wait until bot joins the meet.
    WebDriverWait(driver, 10000000).until(EC.visibility_of_element_located((By.ID,'new-toolbox')))

    # Open chat box
    chatIcon=driver.find_element(By.CLASS_NAME, 'toolbar-button-with-badge')
    ActionChains(driver).move_to_element(chatIcon).click().perform()
    driver.implicitly_wait(3)

    # To wait until text message box is visible
    WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.CLASS_NAME, 'icon-input')))

    # Introduce bot in chat
    driver.find_element(By.CLASS_NAME, 'icon-input').send_keys("Hi! I'm Music bot." + Keys.ENTER)
    driver.implicitly_wait(3)
    print("Introduced in chat")

    #Read chat commands
    msgIndex=1
    run=1
    while(run==1):
        chatList=driver.find_elements(By.CLASS_NAME, 'usermessage')
        if len(chatList)>msgIndex:
            chatText=chatList[msgIndex].text
            msgIndex=msgIndex+1

            # Ignoring messages sent by bot itself
            if chatText[:2]=="me":
                continue

            #Removing author details
            actualChatText=str(chatText).split("\n",1)[1]
            actualChatText=str(actualChatText).lower()

            if "/play" in actualChatText:
                print("Play Song")
                songNameStartIdx=actualChatText.find("/play")+6
                songName=actualChatText[songNameStartIdx:]
                if len(songName)==0:
                    print("Invalid song name")
                    continue
                musicWindow=playSong(driver, songName)
            elif "/pause" in actualChatText:
                print("Pause Song")
                pauseResumeSong(driver, musicWindow)
            elif "/resume" in actualChatText:
                print("Resume song")
                pauseResumeSong(driver, musicWindow)
            elif "/help" in actualChatText:
                print("Bot help")
                helpCommand(driver)
            elif "/exit" in actualChatText:
                run=0
                print("Exit bot")
                exitCommand(driver)