from selenium.webdriver.common.by import By

def exitCommand(driver):
    driver.find_element(By.CLASS_NAME, 'hangup-button').click()
    driver.implicitly_wait(10)
    driver.quit()