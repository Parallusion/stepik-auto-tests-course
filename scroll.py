from selenium import webdriver
import math
 
def calc(x):
    return str(math.log(abs(12*math.sin(x))))
 
link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
 
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(int(x))
  
input = browser.find_element_by_id("answer")
input.send_keys(y)

button = browser.find_element_by_tag_name("button")
browser.execute_script('return arguments[0].scrollIntoView(true);', button)
 
checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()
 
radioB = browser.find_element_by_css_selector("[for = 'robotsRule']")
radioB.click()
 
button = browser.find_element_by_css_selector("button.btn")
button.click()
