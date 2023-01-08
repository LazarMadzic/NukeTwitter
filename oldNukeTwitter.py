import os
import profile
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
import math

os.environ['PATH'] += r";C:\\SeleniumDrivers\\chromedriver_win32"

def check_exists_by_xpath(xpath):
    try:
        time.sleep(5)
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

mail="lazarmbottest@gmail.com"
pas="bottest123"
usern="lazarmbottest"
profile="https://twitter.com/"+usern
driver = webdriver.Chrome() 
# driver.set_window_position(-10000,0)
driver.get("https://twitter.com/i/flow/login")
wait = WebDriverWait(driver, 60)

path_login="//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input"
mail_in= wait.until(EC.presence_of_element_located((By.XPATH, path_login))) 
mail_in.send_keys(mail + Keys.ENTER)


test_alt_path="//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input"
if(check_exists_by_xpath(test_alt_path)):
    #too many login attempts 
    username_in=wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))
    username_in.send_keys(usern + Keys.ENTER)
    print("yup 2")

    pas_path="//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input"
    #pas_path="//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]"
    pas_in=wait.until(EC.presence_of_element_located((By.XPATH, pas_path)))
    
    
    actionChains = ActionChains(driver)
    actionChains.move_to_element(pas_in).click().perform()
    actionChains.move_to_element(pas_in).send_keys(pas,Keys.ENTER).perform()
    
else:
    #first time login TBD
    print("yup 3")
    username_in=wait.until(EC.presence_of_element_located((By.XPATH, test_alt_path)))
    time.sleep(10)
    
    username_in.send_keys(usern + Keys.ENTER)


#go to profile page
prof_path="//*[@id=\"react-root\"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]/div"
prof=wait.until(EC.presence_of_element_located((By.XPATH, prof_path)))
prof.click()



css_tweet_class="//div[@class='css-1dbjc4n r-1niwhzg r-sdzlij r-1p0dtai r-xoduu5 r-1d2f490 r-xf4iuw r-1ny4l3l r-u8s1d r-zchlnj r-ipm5af r-o7ynqc r-6416eg']"
tweets=wait.until(EC.presence_of_element_located((By.XPATH, css_tweet_class)))
tweets=driver.find_elements(By.XPATH, css_tweet_class)





driver.refresh()
num_tweets=len(tweets)/3;
num_tweets=math.floor(num_tweets)

# for tweet in tweets:
    


# print(len(tweets))
# time.sleep(10)