from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

COOKIE_BUTTON = '/html/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div/span/span'
TIME_TO_WAIT = 0.5 #
#Parody of event fetching

def foo():

    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options)
    url = 'https://www.facebook.com/events/search/?q='
    input = 'Riga'

    time.sleep(0.5)

    driver.get(url + input)
    # Need to change find_element
    driver.find_element_by_xpath(COOKIE_BUTTON).click()

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
    # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Can this be change ?
        time.sleep(0.5)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


    # Need to change find_elements_by_xpath to find_elements

    elem = driver.find_elements_by_xpath('.//span[@class = "tojvnm2t a6sixzi8 abs2jz4q a8s20v7p t1p8iaqh k5wvi7nf q3lfd5jv pk4s997a bipmatt0 cebpdrjk qowsmv63 owwhemhu dp1hu0rb dhp61c6y iyyx5f41"]')

    return elem

test = foo()
for element in test:
    print (element.text)
