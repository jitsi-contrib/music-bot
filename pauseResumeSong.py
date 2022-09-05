from selenium.webdriver.common.by import By

def pauseResumeSong(driver, musicWindow):
    originalMeetWindow=driver.current_window_handle
    driver.switch_to.window(musicWindow)
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'play-pause-button').click()
    driver.implicitly_wait(10)
    driver.switch_to.window(originalMeetWindow)
    driver.implicitly_wait(10)
