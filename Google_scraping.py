#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from os import sys
from selenium.webdriver.common.keys import Keys


# In[25]:


url = 'https://www.google.co.in/'
driver_msn = webdriver.Edge()
driver_msn.get(url)
time.sleep(5)
#searchbox = driver_msn.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[1]')
searchbox = WebDriverWait(driver_msn, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[1]')))
m = driver_msn.find_element_by_name("q")
#enter search text
m.send_keys("azure devops")
time.sleep(0.2)
#perform Google search with Keys.ENTER
m.send_keys(Keys.ENTER)




# In[ ]:




