# 04/05/2024
# THis is my first attempt at scraping a website. I will use BeautifulSoup: https://realpython.com/beautiful-soup-web-scraper-python/
# Prompt :Please scrape this page and add all project Twitter handles to a CSV file.
 
# Here is the webpage containing over 4,000 projects to scrape:

# https://defillama.com/

# Each project name is clickable, leading to another page where you can find its Twitter handle.
# For example, this is how the page looks for on project: https://defillama.com/protocol/filda 

import requests
from bs4 import BeautifulSoup
# this import should help me access info 'hidden' behind JS
from selenium import webdriver
from selenium.webdriver.common.by import By

# Not exactly sure what this is or does. its a driver for Firefox
driver = webdriver.Firefox()

# We will store the firefox page information, instead of just the HTML, in driver using get
driver.get("https://defillama.com/protocol/filda#information")
#print(driver)

# Request browser info
title = driver.title
print("this is the title: ", title)

# impliment a wait period so the code and browser is synced
driver.implicitly_wait(0.5)

#Find element by ID
id_next = driver.find_element(By.ID, "__next")
print(id_next)

#find element in id_next by class name
#class_name = id_next.find_element(By.CLASS_NAME, "sc-9019a257-0 leNWDO")
#print(class_name)

# this is it FIND AN ELEMENT
tag_a = id_next.find_element(By.LINK_TEXT, "Twitter")
twitter = tag_a.get_attribute("href")
print(twitter)

#print the links
# for t in twitter:
#     print(t.text)




























#URL of the page I am scraping
#URL = "https://defillama.com/protocol/filda"

# #Store the page using get
# page = requests.get(URL)

# # store the soup, this is what the webserver sent us.
# soup = BeautifulSoup(driver.page_source, "lxml")
# print(soup.prettify())



# #Results - this is the ID 
# results = soup.find(id="challenge-error-title")
# if results is None:
#     print('results is EMPTY')
# print(results.prettify())

# # This will find elements by class name
# job_elements = soup.find_all("div", class_="card-content")

# twitter = soup.find_all("a")
# print(twitter)

# loop
# for job_element in python_job_elements:
#     # -- snip --
#     links = job_element.find_all("a")
#     for link in links:
#         link_url = link["href"]
#         print(f"Apply here: {link_url}\n")
