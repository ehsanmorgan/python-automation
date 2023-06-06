from selenium import webdriver
from selenium.webdriver.common.by import By
 
# create webdriver object
driver = webdriver.Firefox()
 
# enter keyword to search
keyword = "real madrid"

# get geeksforgeeks.org
driver.get("https://www.youtube.com/watch?v=eIU8uAR-TJM")
 
# get element
element = driver.find_element(By.XPATH, '//*[@id="search-input"]' )
# print complete element
print(element)