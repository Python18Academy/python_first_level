from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('https://www.yandex.com')
assert 'Яндекс' in browser.title

elem = browser.find_element_by_class_name('input__control')  # Find the search box
elem.send_keys('Ozon 18+' + Keys.RETURN)

# browser.quit()