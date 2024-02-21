import lxml
from lxml.html import fromstring, tostring
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import FirefoxOptions
from configparser import ConfigParser


driver = webdriver.Firefox()
driver.implicitly_wait(0.5)
driver.maximize_window()
driver.get("https://students.mephi.ru/certificates?mode=normal&status=0")

# urlconf = "C:/Users/User/Desktop/dev/studoffice_automation/config.ini"
# config = ConfigParser()
# config.read(urlconf)
admin_id = ("sgsgsgsfgsg")
admin_pw = ("sgsgsgsfgsg")

driver.findElement(By.ID("username").send_keys(admin_pw))
driver.findElement(By.ID("password").send_keys(admin_id))


# def __init__(self):
#     options = FirefoxOptions()
#     options.add_argument('--headless')
#     self.agent = webdriver.Firefox(options=options)

