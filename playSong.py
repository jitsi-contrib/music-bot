from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def playSong(driver, songName):
    originalMeetWindow=driver.current_window_handle
    driver.switch_to.new_window('tab') 
    youtubeMusicWindow=driver.current_window_handle

    driver.get("https://music.youtube.com/search?q="+songName)
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'play-button').click()
    driver.implicitly_wait(10)
    
    # Wait until song starts playing
    WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.CLASS_NAME, 'playing-mode')))

    driver.execute_script('var sink_id = "";navigator.mediaDevices.enumerateDevices().then(inspect_devices).catch(errorCallback);function inspect_devices(deviceInfos) {console.log("Inspecting Devices: " + deviceInfos.length + " device(s) total (audio/video input/output)");for (var deviceIdx = 0; deviceIdx < deviceInfos.length; deviceIdx++) {var deviceInfo = deviceInfos[deviceIdx];if ((deviceInfo.kind == "audiooutput") && (deviceInfo.label.includes("VB-Audio") || deviceInfo.label.includes("BlackHole"))) {sink_id = deviceInfo.deviceId;update_all_sinks();}}}function update_all_sinks() {var allMedia = document.querySelectorAll("audio,video");for (var mediaElement = 0; mediaElement < allMedia.length; mediaElement++) {allMedia[mediaElement].setSinkId(sink_id);}}function errorCallback(error) {console.log("Error: "+ error);}')
    driver.implicitly_wait(1000)

    driver.switch_to.window(originalMeetWindow)
    driver.implicitly_wait(10)

    return youtubeMusicWindow