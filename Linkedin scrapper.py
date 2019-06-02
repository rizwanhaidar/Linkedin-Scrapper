#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
from itertools import zip_longest



driver=webdriver.Chrome(executable_path="C:\Python34\Drivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.linkedin.com/login")
driver.implicitly_wait(3)

usnm=input("Enter the Username: ")
pswd=input("Enter the Password")
post_url=input("Enter the post url which you want to scrape: ")

driver.find_element_by_xpath("//*[@id='username']").send_keys(usnm)
driver.find_element_by_xpath("//*[@id='password']").send_keys(pswd)
driver.find_element_by_xpath("//*[@id='app__container']/main/div/form/div[3]/button").click()
time.sleep(5)
driver.get(post_url)

while True:
    try:
        loadMoreButton = driver.find_element_by_xpath("//*[@id='show_prev']/span[1]")
        time.sleep(1)
        loadMoreButton.click()
        time.sleep(5)
    except Exception as e:
        break

name = driver.find_elements_by_css_selector("h3 > span.feed-shared-post-meta__name.t-14.t-black.t-bold > span.hoverable-link-text")
#name1 = name.find_elements_by_class_name("hoverable-link-text")
email_wide_view=driver.find_elements_by_class_name("ember-view")
#email_text=
nm=[]
em=[]
for span in name:
    nm.append(span.text)
for span in (email_wide_view):
    sub_str=span.get_attribute("href")
    if sub_str:
        if(sub_str.find("mailto:")!=-1):
            em.append(sub_str[7:])

with open('Desktop/data.csv', 'w') as data:
    writer = csv.writer(data)
    writer.writerow(["NAME", "EMAIL ID"])
    for row in zip_longest(nm,em):
        writer.writerow(row)

        
driver.close()
print("Process Successfully Completed!")
k=len(nm)
print(str(k)+' emails Scraped')


# In[ ]:




