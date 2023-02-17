from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

asd = webdriver.Chrome()
link = 'https://www.yclients.com/signin/'
login = "a.filippov@yclients.tech"
password = "Ose7vgt5"
link2 = 'https://yclients.com/documents/goodstransactions/694561/0/?type=3'
code = '1.207576359389E'

try:
    asd.get(link)
    asd.maximize_window()
    button = WebDriverWait(asd, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]')))
    logn = asd.find_element(By.CSS_SELECTOR, "[name='email']")
    logn.click()
    logn.send_keys(login)
    paswd = asd.find_element(By.CSS_SELECTOR, '[type="password"]')
    paswd.click()
    paswd.send_keys(password)
    button.click()
    time.sleep(4)


    asd.get(link2)
    min_sbar = asd.find_element(By.ID, 'super-panel-close-btn')
    min_sbar.click()
    add = WebDriverWait(asd, 5).until(EC.element_to_be_clickable(
        (By.ID, 'add_good_transaction')))
    add.click()
    inp = asd.find_element(
        By.CSS_SELECTOR, '[class="form-control ui-autocomplete-input"][data-num="1"]')
    inp.click()
    inp.send_keys(code)
    time.sleep(2)
    inp2 = asd.find_element(
        By.CSS_SELECTOR, '[class="form-control ui-autocomplete-input"][data-num="2"]')
    inp2.click()
    for i in range(10000):
        inp2.send_keys(code)
        time.sleep(0.1)
    time.sleep(5)

finally:
    asd.quit()