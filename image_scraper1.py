#Uncomment the code below if running on Google Colab

""" %%capture
import sys
!pip install selenium
#!apt-get update # to update ubuntu to correctly run apt install
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver') """

import requests
from bs4 import BeautifulSoup
import lxml
import re
import os
from PIL import Image
import sys
import urllib.request, urllib.parse, urllib.error
import ssl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(
        '/home/samuel/Downloads/Compressed/chromedriver')


driver.get("https://www.google.com/")

box = driver.find_element_by_xpath('//*[@id="sb_form_q"]')
#Change cranes to the object you wish to search for
box.send_keys("cranes")
box.send_keys(Keys.ENTER)

driver.find_element_by_xpath('//*[@id="b-scopeListItem-images"]/a').click()

#The line of code will keep scrolling down the webpage until it cannot scroll no more
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    try:
        driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
        time.sleep(2)
    except:
        pass
    if new_height == last_height:
        break
    last_height = new_height

for i in range(1, 1000):
    try:
        driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot('/home/samuel/images/crane/crane_'+str(i)+'.png')
        #Change the path to save the images
    except:
        pass