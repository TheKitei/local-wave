from asyncio.windows_events import NULL
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import houseDB

COOKIE_BUTTON = '/html/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div/span/span'
TIME_TO_WAIT = 0.5 
URL = 'https://www.facebook.com/events/search/?q='
#Parody of event fetching



def initDriver():
    try:
        options = Options()
        options.headless = False
        driver = webdriver.Firefox(options=options)
        return driver
    except:
        print("Driver dead")


def getList(input):
    # Super nested functions?
    driver = initDriver()

    driver.get(URL + input)

    # wait for page to load 
    time.sleep(TIME_TO_WAIT+0.5)
    # Need to change find_element
    driver.find_element_by_xpath(COOKIE_BUTTON).click()

    elemInfo = []

    time.sleep(TIME_TO_WAIT)

    big = driver.find_elements(By.XPATH,"//*[@class = 'tr9rh885 wkznzc2l sjgh65i0 dhix69tm']")
    

    for i in range(len(big)):

        
        try:
            title = big[i].find_element(By.XPATH,".//*[@class = 'tojvnm2t a6sixzi8 abs2jz4q a8s20v7p t1p8iaqh k5wvi7nf q3lfd5jv pk4s997a bipmatt0 cebpdrjk qowsmv63 owwhemhu dp1hu0rb dhp61c6y iyyx5f41']")
        except:
            break
        try:
            img = big[i].find_element(By.XPATH,".//*[@class = 'k4urcfbm bixrwtb6 datstx6m q9uorilb']")
        except:
            img = type(title)
        try:
            clock = big[i].find_element(By.XPATH,".//*[@class = 'd2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh e9vueds3 j5wam9gi lrazzd5p oo9gr5id']")
        except:
            clock = type(title)
        try:
            address = big[i].find_element(By.XPATH,".//*[@class = 'd2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh jq4qci2q a3bd9o3v lrazzd5p m9osqain']")
        except:
            address = type(title)
        link =  big[i].find_element(By.CSS_SELECTOR,'a:nth-child(1)')
        
        query = [title.text,(img.get_attribute("src")),address.text,clock.text,link.get_attribute("href")]

        elemInfo.append(query)

    return elemInfo




def recive(user):

    userLoc = houseDB.getUserLoc(user)
    userEvents = []
    for i in userLoc:
        currentLoc = getList(i)
        for j in range(len(currentLoc)):
            userEvents.append([currentLoc[j][0],currentLoc[j][1],currentLoc[j][2],currentLoc[j][3]])
    # print("test")
    
    
    return userEvents


recive("1125")


    

