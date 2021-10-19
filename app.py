from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from chromedriver import chromeDriverSetup 
from time import sleep
import urllib.request

def main():
    options = webdriver.ChromeOptions()        
    chromeDriverSetup(options)
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
    driver = webdriver.Chrome()
   
    searchTerm = input("Enter the images you want to get : ")
    searchInGoogle(driver=driver, searchTerm=searchTerm)

    sleep(10)

def searchInGoogle(driver, searchTerm):
    driver.get('https://www.google.com')
    driver.maximize_window()
    input = driver.find_element_by_xpath("//input[@name='q']")
    input.clear()
    input.send_keys(searchTerm)
    input.send_keys(Keys.ENTER)
    sleep(3)
    tabs = driver.find_element_by_css_selector('div.MUFPAc>:nth-child(2)>:first-child')
    tabs.send_keys(Keys.ENTER)

    for i in range (0, 10):
        image = driver.find_element_by_css_selector(f"div.islrc>:nth-child({i})>:first-child>:first-child>:first-child")
        src = image.get_attribute('src')
        urllib.request.urlretrieve(src, f"image{i}.jpg")

main()  
