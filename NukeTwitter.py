import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
 
"""
def clearFollowers():

def clearWhoIFollow():

def clearLikes():

def clearTweets():

def clearEverything():
    clearFollowers()
    clearWhoIFollow()
    clearTweets()
    clearLikes()
"""

#x=len(sys.argv)
#mail=sys.argv[2]
#pas=sys.argv[3]
#opt==sys.argv[4]

mail=
pas=


os.environ['PATH'] += os.pathsep + "C:/SeleniumDrivers/"
#instantiate the Chrome class web driver and pass the Chrome Driver Manager
driver = webdriver.Chrome()
 
#Maximize the Chrome window to full-screen
driver.maximize_window() 

#go to Twitter's Homepage
driver.get("https://twitter.com/i/flow/login")

inp_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input'
wait = WebDriverWait(driver, 10)
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath))) 
input_box.send_keys(mail + Keys.ENTER)

inp_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input'
wait = WebDriverWait(driver, 10)
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
input_box.send_keys(pas + Keys.ENTER)

xp_profile='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]/div/div[2]/span'
wait = WebDriverWait(driver, 10)
input_box = wait.until(EC.presence_of_element_located((By.XPATH, xp_profile)))
input_box.click()

"""  
match opt:
        case '1':
            clearFollowers()
        case '2':
            clearWhoIFollow()
        case '3':
            clearLikes()
        case '4':
            clearTweets()
        case '5':
            clearEverything()
        case _:
            print("Option does not exist")        
"""            
