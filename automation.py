from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


chrome_browser = webdriver.Chrome(
    'chromedriver', options=chrome_options)

chrome_browser.get('https://www.seleniumeasy.com/')


user_message = chrome_browser.find_element(By.ID, "edit-search-block-form--2")
user_message.clear()  # smaže, pokud tam něco je
user_message.send_keys('i am extra cool')  # napíše zprávu do okna

search_button = chrome_browser.find_element(
    By.CLASS_NAME, 'glyphicon-search')  # prepsanej komentar
search_button.click()  # kliknu na lupu

output_message = chrome_browser.find_element(By.ID, 'display')
assert 'i am looser, buheheee' in output_message.text

user_button = chrome_browser.find_element(By.CSS_SELECTOR, 'btn-success')
print(user_button)

chrome_browser.quit()
chrome_browser.quit()

print('zivot a svet')
