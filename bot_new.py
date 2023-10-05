#pip install selenium, pip install from selenium import webdriver
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(GeckoDriverManager().install())

browser = webdriver.Firefox(service=service)


#aguardar ate um elemento especifico carregar na página:
# wait = WebDriverWait(browser, 10)
# wait.until(EC.presence_of_element_located((By.XPATH, 'xpath aqui')))

def wait_element(type_element, link_element):
    locators = {
        "XPATH": By.XPATH,
        "ID": By.ID,
        "NAME": By.NAME,
        "CLASS_NAME": By.CLASS_NAME,
    }

    if type_element not in locators:
        raise ValueError("Tipo de localizador inválido")

    WebDriverWait(browser, 10).until(EC.presence_of_element_located((locators[type_element], link_element)))


def login(email, password):
    browser.get("https://www.instagram.com/")
    time.sleep(5)

    browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input').send_keys(email)
    browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input').send_keys(password)
    time.sleep(2)

    browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()

def go_initial_page():
    xpath_inital_page = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div/span/div/a/div/div[2]'

    wait_element('XPATH', xpath_inital_page)
    #WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, xpath_inital_page)))

    browser.find_element(By.XPATH, xpath_inital_page).click()
    time.sleep(2)

    print('\nvou tentar algumas coisas agr')

    """
    try:
        print('\nlink text')
        browser.find_element(By.LINK_TEXT, 'Agora não').click()
    except:
        print('\ncss seletor')
        browser.find_element(By.CSS_SELECTOR, 'button._a9--:nth-child(2)').click()
    """
    try:
        print('\nxpath1')
        browser.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
    except:
        print('\nxpath2')
        browser.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
    
    print('continuando')


login('', '')
go_initial_page()
