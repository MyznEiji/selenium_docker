#!/usr/local/bin/python3
from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime

#browser = webdriver.Firefox()
#browser = webdriver.Chrome()

# HEADLESSブラウザに接続
driver = webdriver.Remote(
    command_executor='http://selenium-hub:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)

# youtubeSearchWord.txtから参照
file = open('./list/youtube.txt', 'r')
words = file.read().split(',\n')

print("open vnc://localhost:5900")
input()

# YouTubeを開く
driver.get("https://www.youtube.com/")


# ワードごとにチェック！
for word in words:
    if word is '':
        break

    wordNum = len(word)

    element = driver.find_element_by_id('search')
    element.send_keys(word)
    driver.find_element_by_id('search-icon-legacy').click()

    print("Please press the 'Enteer_Key' as soon as the check is over")
    input()
    element.send_keys(Keys.BACK_SPACE * wordNum)


# ダウンロードサイトを開く
driver.get("https://www.onlinevideoconverter.com/ja/video-converter")
print("Please press the 'Enteer_Key' when downloading is complete")
input()


driver.close()
driver.quit()
