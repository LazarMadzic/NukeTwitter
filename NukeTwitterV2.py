from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import os
from timeit import default_timer as timer
from datetime import timedelta
import sys

os.environ['PATH'] += r";C:\\SeleniumDrivers\\chromedriver_win32"

class Remover:

    def __init__(self,username) -> None:
        self._username = username
        self._my_tweets = f"https://twitter.com/{self._username}"
        self._my_followers = f"https://twitter.com/{self._username}/followers"
        self._my_following = f"https://twitter.com/{self._username}/following"
    
    def remove_followers(self):
        driver.get(self._my_followers)
        no_removed_followers = 0
        while True:
            try:    
                wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='css-1dbjc4n r-18u37iz r-1h0z5md r-19u6a5r']")))
                driver.find_element(By.XPATH, "//div[@class='css-1dbjc4n r-18u37iz r-1h0z5md r-19u6a5r']").click()
                wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Remove this follower']")))
                driver.find_element(By.XPATH, "//span[text()='Remove this follower']").click()
                wait.until(EC.element_to_be_clickable(((By.XPATH, "//span[text()='Remove']"))))
                driver.find_element(By.XPATH, "//span[text()='Remove']").click()
                no_removed_followers+=1
                driver.refresh()
                driver.find_elements(By.XPATH, "//div[@class='css-1dbjc4n r-18u37iz r-1h0z5md r-19u6a5r']")
            except TimeoutException:
                break
        return no_removed_followers

    def remove_followed(self):
        driver.get(self._my_following)
        no_removed_followed = 0
        while True:
            try:    
                wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='css-901oao css-16my406 css-1hf3ou5 r-poiln3 r-1b43r93 r-1cwl3u0 r-bcqeeo r-qvutc0']")))
                driver.find_element(By.XPATH, "//span[@class='css-901oao css-16my406 css-1hf3ou5 r-poiln3 r-1b43r93 r-1cwl3u0 r-bcqeeo r-qvutc0']").click()
                wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Unfollow']")))
                driver.find_element(By.XPATH, "//span[text()='Unfollow']").click()
                no_removed_followed+=1
                driver.refresh()
            except TimeoutException: 
                #driver.find_elements(By.XPATH, "//span[@class='css-901oao css-16my406 css-1hf3ou5 r-poiln3 r-1b43r93 r-1cwl3u0 r-bcqeeo r-qvutc0']")
                break

        return no_removed_followed


    def delete_tweets(self):
        pass


if __name__ == "__main__":
    try:
        username = str(sys.argv[1])
        remover_obj = Remover(username)
    except IndexError:
        print("Missing username!")

    opt = Options()
    opt.add_experimental_option("debuggerAddress","localhost:8989")
    driver=webdriver.Chrome(executable_path="C:\\SeleniumDrivers\\chromedriver_win32\\chromedriver.exe", options=opt)
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)
    driver.minimize_window()
    for option in range(2, len(sys.argv)):
        if int(sys.argv[option]) == 1:
            start = timer()
            print("Deleted " + str(remover_obj.delete_tweets()) + " tweets.")
            end = timer()
            print(timedelta(seconds=end-start))
        if int(sys.argv[option]) == 2:
            start = timer()
            print("Removed " + str(remover_obj.remove_followers()) + " followers.")
            end = timer()
            print(timedelta(seconds=end-start))
        if int(sys.argv[option]) == 3:
            start = timer()
            print("Removed " + str(remover_obj.remove_followed()) + " followed people.")
            end = timer()
            print(timedelta(seconds=end-start))
    driver.maximize_window()
