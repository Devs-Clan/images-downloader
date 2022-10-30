from selenium.webdriver.common.keys import Keys
from time import sleep
import urllib.request
import Driver 
import os



def main() -> None:        
    driver = Driver().get_driver()
    search_in_google(driver=driver, search_term=search_term)
    sleep(10)


def search_term() -> str:
    while(True):
        search_term = input("Enter the images you want to get (This will be the folder name of the data set): ")
        try:
            os.mkdir(f'data-set/{search_term}') 
            break
        except:
            print("File already exists. Try different name.")
    return search_term        


def search_in_google(driver: Driver, search_term: str):
    driver.get('https://www.google.com')
    driver.maximize_window()   
    input = driver.find_element_by_xpath("//input[@name='q']")
    input.clear()
    input.send_keys(search_term)
    input.send_keys(Keys.ENTER)
    sleep(3)
    tabs = driver.find_element_by_css_selector('div.MUFPAc>:nth-child(2)>:first-child')
    tabs.send_keys(Keys.ENTER)
    get_images(search_term)


def get_images(search_term: str) -> None:
    for i in range(1, 10):
        image = driver.find_element_by_css_selector(f"div.islrc>:nth-child({i})>:first-child>:first-child>:first-child")
        src = image.get_attribute('src')
        urllib.request.urlretrieve(src, f"data-set/{search_term}/image{i}.jpg")


if __name__ == "__main__":
    main() 
