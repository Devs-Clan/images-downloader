from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from chrome import ChromeConfig 
from time import sleep
from datetime import datetime
import urllib.request
import os

GOOGLE_PATH = r'https://www.google.com'


def main():
    search_term = input("Object to download: ")
    if search_term not in os.listdir(os.path.join(os.getcwd(), 'data-set')):
        print(f'Creating folder with the name: {search_term}')
        os.mkdir(f'data-set/{search_term}')
    else:
        print(f'NOTE: new data will added to exsisting directory named: {search_term}')

    options = ChromeConfig(webdriver.ChromeOptions())
    driver = webdriver.Chrome(options=options)
   
    download_from_google(driver=driver, search_term=search_term)


def download_from_google(driver, search_term):
    driver.get(GOOGLE_PATH)
    driver.maximize_window()
    
    input = driver.find_element_by_xpath("//input[@name='q']")
    input.clear()
    input.send_keys(search_term)
    input.send_keys(Keys.ENTER)
    sleep(2)
    tabs = driver.find_element_by_css_selector('div.MUFPAc>:nth-child(2)>:first-child')
    tabs.send_keys(Keys.ENTER)

    for i in range (1, 200):
        if i % 25 == 0:
            continue
        image = driver.find_element_by_css_selector(f"div.islrc>:nth-child({i})>:first-child>:first-child>:first-child")
        src = image.get_attribute('src')
        current_datetime = datetime.now().strftime(f'%d-%m-%Y, %H:%M:%S')
        urllib.request.urlretrieve(src, f"data-set/{search_term}/{current_datetime}.jpg")

if __name__ == "__main__":
    main()  
