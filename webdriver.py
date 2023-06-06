from selenium import webdriver
from selenium.webdriver.common.by import By
  

#from selenium import webdriver


url = r' /Users/fatemaabdallah/Downloads/geckodriver'

driver = webdriver.Firefox(executable_path = url )

driver.get("https://www.google.com")

google_search =  driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")

google_search.send_keys("real madrid")






# import webdriver with find element by xpath
from selenium import webdriver
from selenium.webdriver.common.by import By
  
# create webdriver object
#url = r' /Users/fatemaabdallah/Downloads/geckodriver'
driver = webdriver.Firefox()
  
# get geeksforgeeks.org
driver.get("https://www.amazon.de/?&tag=hydraamazon09-21&ref=pd_sl_781ozcfkw7_e&adgrpid=71137539015&hvpone=&hvptwo=&hvadid=352566565909&hvpos=&hvnetw=g&hvrand=3627179024242247261&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9043843&hvtargid=kwd-10573980&hydadcr=12763_1720986")
  
# get element 
element = driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
  
# send keys 
element.send_keys("samsung ultra")
element_click = driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]')
element_click.click()







# create webdriver object
driver = webdriver.Firefox()
 
# enter keyword to search
keyword = "geeksforgeeks"
 
# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
 
# get element
element = driver.find_element(By.XPATH, "//form[input/@name ='search']")
 
# print complete element
print(element)
