from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import pytest

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["236895", "236896", "236897", "236898", "236899", "236903","236904","236905"])
def test_guest_should_see_login_link(browser, language):
    link = f"https://stepik.org/lesson/{language}/step/1/"
    browser.get(link)
    answer = math.log(int(time.time()))
    element1=browser.find_element_by_class_name("attempt")
    element1.send_keys(answer)
    button=browser.find_element_by_css_selector("#ember74 > div > section > div > div.attempt__inner > div.attempt__actions > button")
    button.click()
    check = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "smart-hints__hint"), "Correct!"))