from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("http://www.google.com")
print("URL of the Webpage is : ",driver.current_url)

'''
print("Title of the Webpage is : ",driver.title)

print("URL of the Webpage is : ",driver.current_url)

script = "alert('Welcome to Google Chrome')"

driver.execute_async_script(script)

time.sleep(30)

driver.quit()
'''

driver.title # => "Google"

driver.implicitly_wait(1)

search_box = driver.find_element(By.NAME, "q")
search_button = driver.find_element(By.NAME, "btnK")

search_box.send_keys("Selenium")
search_button.click()

driver.find_element(By.NAME, "q").get_attribute("value") # => "Selenium"

#driver.quit()