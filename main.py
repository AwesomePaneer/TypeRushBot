from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import json
import pyautogui

PATH = "chromedriver.exe"
options = {'disable_encoding': True}
driver = webdriver.Chrome(PATH,seleniumwire_options=options)
driver.get("https://www.typerush.com/account.html?play=1")

#driver.implicitly_wait(30)
#main_frame = driver.find_element_by_id("game_iframe")

try:
    main_frame = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID,"game_iframe"))
    )
except:
    driver.close()

string_found = False
game_string = ""

while not string_found:
    for request in driver.requests:
        if request.response and 'games/start' in request.path:
            game_string = json.loads(request.response.body.decode('utf-8'))
            string_found = True

game_string = game_string['gameData']['text'] + game_string['gameServerData']['text2']

user_input = input("Enter required wpm speed:\n")
interval = 10.2/float(user_input)
time.sleep(3)
pyautogui.write(game_string,interval=interval)

while True:
    pass