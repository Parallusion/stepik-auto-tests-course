from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    import math

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    print(x.text)
    y = calc(x)
  
    print(y.text)
   
    element1 = browser.find_element_by_css_selector("input")
    element1.send_keys(y)
   
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()

    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()