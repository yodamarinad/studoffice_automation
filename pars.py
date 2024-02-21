import lxml
from lxml.html import fromstring, tostring
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import FirefoxOptions

driver = webdriver.Firefox()
driver.implicitly_wait(0.5)
driver.maximize_window()
driver.get("https://students.mephi.ru/certificates?mode=normal&status=0")

# s = driver.find_element_by_xpath("//*[@id="name"]")
# s.send_keys('1')
# s.send_keys.submit()

# def __init__(self):
#     options = FirefoxOptions()
#     options.add_argument('--headless')
#     self.agent = webdriver.Firefox(options=options)

