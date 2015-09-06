# -*- encoding=utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Firefox()
driver.get("http://vote-kkragoth.rhcloud.com/vote3/district/3/")
assert u"Wybierz jednostkę" in driver.title
elem = driver.find_element_by_css_selector("span.cards")
current_cards = str(elem.text)

elem = driver.find_element_by_css_selector("button.button-edit")
elem.click()
negative_number_cards = -512
elem = driver.find_element_by_css_selector("input.cards")
'''
http://stackoverflow.com/questions/20936403/sendkeys-are-not-working-in-selenium-webdriver
'''
time.sleep(1)
elem.click()
elem.clear()
elem.send_keys(negative_number_cards)
elem = driver.find_element_by_css_selector("button.button-save")
time.sleep(1)
elem.click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.alert_is_present())
time.sleep(2)
Alert(driver).dismiss()
elem = driver.find_element_by_css_selector("button.button-cancel")
time.sleep(1)
elem.click()

elem = driver.find_element_by_css_selector("span.cards")
current_cards = int(elem.text)
elem = driver.find_element_by_css_selector("button.button-edit")
time.sleep(1)
elem.click()
new_number_cards = current_cards + 1
elem = driver.find_element_by_css_selector("input.cards")
time.sleep(2)
elem.click()
elem.clear()
elem.send_keys(str(new_number_cards))
elem = driver.find_element_by_css_selector("button.button-save")
time.sleep(1)
elem.click()
wait = WebDriverWait(driver, 10)
time.sleep(1)
wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, "span.cards"),str(new_number_cards)))
driver.close()
