import re
import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

url2 = 'https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0'
service = Service(executable_path=r"C:\Users\annap\Downloads\chromedriver-win64\chromedriver.exe")
browser = webdriver.Chrome(service=service)
browser.get(url2)
time.sleep(2)
# to store html code in beatifulsoup
src = browser.page_source
soup = BeautifulSoup(src, 'lxml')

type1="Contract"
type2="Full Time"
job_type1=browser.find_element(By.XPATH," //*[@id='jserp-filters']/ul/li[5]/div/div/div/div/div")
job_type= soup.find_all('div', {'class': 'filter-values-container__filter-values'})

dd=browser.find_element(By.XPATH,'//*[@id="jserp-filters"]/ul/li[5]/div/div/button')
drop = browser.find_element(By.XPATH,'//*[@id="jserp-filters"]/ul/li[5]/div/div/button').click()
dd.send_keys(Keys.TAB + Keys.SPACE)
dd.send_keys(Keys.TAB * 3 + Keys.SPACE) 

browser.find_elements_by_css_selector("label[for='f_JT-0']").click()

browser.find_element(By.XPATH,'//*[@id="jserp-filters"]/ul/li[5]/div/div/button').click()
uname = browser.find_element(By.NAME,"f_JT")
uname.send_keys(Keys.TAB)

title = soup.find_all('h3', {'class': 'base-search-card__title'})
Job_Title = []
for i in title:
    Job_Title.append(i.text.strip())
 

jobs =browser.find_elements(By.XPATH,"//*[@id='main-content']/section/ul/li/div/a")
Jobs_Post_Link=[]
for link in jobs:
    Jobs_Post_Link.append(link.get_attribute("href"))


company = soup.find_all('h4', {'class': 'base-search-card__subtitle'})
Company_Name=[]
for name in company:
    Company_Name.append(name.text.strip())
