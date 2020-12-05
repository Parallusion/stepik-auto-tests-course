from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        try: 
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)
   
            element1 = browser.find_element_by_css_selector("div.first_block > div.form-group.first_class > input")
            element1.send_keys("Zdarova")

            element2 = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input")
            element2.send_keys("Zdarova")

            element3 = browser.find_element_by_css_selector("div.first_block > div.form-group.third_class > input")
            element3.send_keys("Zdarova")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(3)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!",welcome_text, "Success")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()
            
    def test_abs2(self):
        try: 
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)
   
            element1 = browser.find_element_by_css_selector("div.first_block > div.form-group.first_class > input")
            element1.send_keys("Zdarova")

            element2 = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input")
            element2.send_keys("Zdarova")

            element3 = browser.find_element_by_css_selector("div.first_block > div.form-group.third_class > input")
            element3.send_keys("Zdarova")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(3)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
          
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!",welcome_text, "Success")


        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()
        
if __name__ == "__main__":
    unittest.main()