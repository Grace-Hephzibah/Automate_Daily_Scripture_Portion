from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, \
    UnexpectedAlertPresentException, NoAlertPresentException
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
from sys import platform

import time
from year import year
from Phone_Numbers import numbers

def text_required():
    month = time.localtime().tm_mon - 1
    day = time.localtime().tm_mday - 1

    today_text = f'Today\'s Bible Portion : {year[month][day]}'
    return today_text


options = Options()
if platform == "win32":
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

message = "Ignore Me" # text_required()
message = quote(message)


total_number = len(numbers)
delay = 30

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com')

input("Press ENTER after login into Whatsapp Web and your chats are visible	.")

for idx, number in enumerate(numbers):
    number = number.strip()

    if number == "":
        continue

    print('{}/{} => Sending message to {}.'.format((idx + 1), total_number, number))

    try:
        url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
        sent = False

        for i in range(3):

            if not sent:
                driver.get(url)

                try:
                    click_btn = WebDriverWait(driver, delay).until(
                        EC.element_to_be_clickable((By.CLASS_NAME, '_4sWnG')))
                except Exception as e:
                    print(f"Something went wrong..\n Failed to send message to: {number}, retry ({i + 1}/3)")
                    print("Make sure your phone and computer is connected to the internet.")
                    print("If there is an alert, please dismiss it.")
                    input("Press enter to continue")

                else:
                    sleep(1)
                    click_btn.click()
                    sent = True
                    sleep(3)
                    print('Message sent to: ' + number)

    except Exception as e:
        print('Failed to send message to ' + number + str(e))