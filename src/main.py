from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

browser = webdriver.Chrome(executable_path='C:/Users/kikweina/Desktop/whatsapp_automate/drivers/chromedriver.exe')

browser.maximize_window()
browser.get('https://web.whatsapp.com/')

with open('groups.txt', 'r', encoding='utf8') as file:
    groups = [group.strip() for group in file.readlines()]

with open('msg.txt', 'r', encoding='utf8') as file:
    msg = file.read()

doc_path = 'C:/Users/kikweina/Desktop/whatsapp_automate/dress_invoice.pdf'

for group in groups:
    # search group
    search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
    search_box = WebDriverWait(browser, 500).until(
        EC.presence_of_element_located((By.XPATH, search_xpath))
    )
    pyperclip.copy(group)
    search_box.clear()
    search_box.send_keys(Keys.CONTROL + "v")

    time.sleep(1)

    # enter group
    group_xpath = f'//span[@title="{group}"]'
    group_title = browser.find_element_by_xpath(group_xpath)
    group_title.click()

    time.sleep(1)

    # get input_box & send msg
    input_xpath = '//div[@contenteditable="true"][@data-tab="10"]'
    input_box = browser.find_element_by_xpath(input_xpath)

    pyperclip.copy(msg)
    input_box.send_keys(Keys.CONTROL + "v")
    input_box.send_keys(Keys.ENTER)

    # open attachment
    attachment_xpath = '//div[@role="button"][@title="Attach"]'
    attachment_box = browser.find_element_by_xpath(attachment_xpath)
    attachment_box.click()

    time.sleep(1)

    # select doc & send
    try:
        doc_xpath = '//input[@type="file"][@accept="*"]'
        doc_box = browser.find_element_by_xpath(doc_xpath)
        doc_box.send_keys(doc_path)
        time.sleep(5)
        send_button = browser.find_element_by_xpath('//div[@role="button"][@aria-label="Send"]')
        send_button.click()
    except:
        pass
