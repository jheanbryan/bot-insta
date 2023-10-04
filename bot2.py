#pip install selenium, pip install from selenium import webdriver
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import time

service = Service(GeckoDriverManager().install())

browser = webdriver.Firefox(service=service)

def login(email, password):
    browser.get("https://www.instagram.com/")

    time.sleep(5)
    #browser.find_element(XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input").send_keys(email)
    browser.find_element(By.xpath, ("/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")).send_keys(email)

    
login('jhean@email.com', 'jhean123')