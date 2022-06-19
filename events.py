from asyncio.windows_events import NULL
from datetime import date
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import houseDB

COOKIE_BUTTON = '/html/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div/span/span'
TIME_TO_WAIT = 0.5 
ADDRESS_PLACE = 'div:nth-child(3) > span:nth-child(1) > span:nth-child(1) > span:nth-child(1)'
DATE_PLACE = 'div:nth-child(1) > span:nth-child(1) > span:nth-child(1)'
TITLE_PLACE = 'div:nth-child(2) > span:nth-child(1) > span:nth-child(1) > object:nth-child(1) > a:nth-child(1) > span:nth-child(1)'
URL = 'https://www.facebook.com/events/search/?q='




def initDriver():
    try:
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        return driver
    except:
        print("Driver dead")


def getList(input):
    # Super nested functions?
    driver = initDriver()

    driver.get(URL + input)

    time.sleep(TIME_TO_WAIT)
    try:
        driver.find_element(By.XPATH,COOKIE_BUTTON).click()
    except:
        return getList(input)

    elemInfo = []

    event = driver.find_elements(By.XPATH,"//*[@class = 'tr9rh885 wkznzc2l sjgh65i0 dhix69tm']")
    

    for i in range(len(event)):

        try:
            title = event[i].find_element(By.CSS_SELECTOR,TITLE_PLACE)
        except:
            break
        
        try:
            img = event[i].find_element(By.CSS_SELECTOR,"img:nth-child(1)")
        except:
            img = NULL
        try:
            date = event[i].find_element(By.CSS_SELECTOR,DATE_PLACE)
        except:
            date = NULL
        try:
            address = event[i].find_element(By.CSS_SELECTOR,ADDRESS_PLACE)
        except:
            address = NULL
        link =  event[i].find_element(By.CSS_SELECTOR,'a:nth-child(1)')
        
        query = [title.text,img.get_attribute('src'),address.text,date.text,link.get_attribute('href')]

        elemInfo.append(query)

    return elemInfo




def recive(user):

    userLoc = houseDB.getUserLoc(user)
    userEvents = []
    for i in userLoc:
        currentLoc = getList(i)
        for j in range(len(currentLoc)):
            userEvents.append([currentLoc[j][0],currentLoc[j][1],currentLoc[j][2],currentLoc[j][3],currentLoc[j][4]])
    
    return userEvents


# recive("1125")


    

