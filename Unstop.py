'''from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

path = 'C://chromedriver.exe'
browser = webdriver.Chrome(executable_path=path)
browser.get('https://unstop.com/hackathons?filters=,all,open,all&types=teamsize,payment,oppstatus,eligible')
browser.maximize_window()

tk = browser.find_element(By.CLASS_NAME("double-wrap ng-star-inserted"))

sleep(5000)'''
import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# create the webdriver object and specify the path to chromedriver


driver = webdriver.Chrome(executable_path='C://chromedriver.exe')

# open the website
driver.get('https://unstop.com/hackathons?filters=,all,open,all&types=teamsize,payment,oppstatus,eligible')

while True:
    try:
        driver.find_element(By.XPATH, "//div[@class='click_here mt-20 ng-star-inserted']")
        break
    except:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
'''# Scroll down the page

driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

# Wait for the page to load
time.sleep(2)

# Scroll up the page
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)

# Wait for the page to load
time.sleep(2)
'''

hackathon_list_element = driver.find_element(By.XPATH, '//app-opportunity-listbox[@class="ng-star-inserted"]')

# Find the elements containing the hackathon names
hackathon_name_elements = hackathon_list_element.find_elements(By.XPATH, './/h2[@class="double-wrap ng-star-inserted"]')


# extract the text from each element and store it in a list
hackathon_names = [element.text for element in hackathon_name_elements]

links = driver.find_elements(By.CLASS_NAME, 'listing')
apply_links = []

# Iterate through the list of elements and extract the links
for link in links:
    temp_link = link.get_attribute('href')
    '''driver.get('https://unstop.com/hackathons?filters=,all,open,all&types=teamsize,payment,oppstatus,eligible')'''

    apply_links.append(temp_link)

institutions = driver.find_elements(By.XPATH, './/h3[@class="double-wrap ng-star-inserted"]')

# Create a list to store the institution names
institution_names = [element.text for element in institutions]

date = []
date_elements = driver.find_elements(By.XPATH, "//div[@class='registered']")
for i in range(len(hackathon_names)):
  date_string = date_elements[i].text
  last_date_to_apply = date_string.split(" ")[-1]
  date.append(last_date_to_apply)

print(apply_links)
print(hackathon_names)
print(institution_names)

competitions = [["Hackathons", "Institutions", "Links"]]
for i in range(len(hackathon_names)):
    competitions.append([hackathon_names[i], institution_names[i], apply_links[i]])
with open("competitions.csv", "w", newline="") as f:
  writer = csv.writer(f)
  writer.writerows(competitions)

'''date = []

for link in links:
    temp_link = link.get_attribute('href')
    driver.get(temp_link)
    temp_date = driver.find_element(By.XPATH, '//strong[@class="ng-tns-c147-1"]')
    date.append(temp_date)

print(date)'''

# close the browser
driver.close()

'''//div[@class="click_here mt-20 ng-star-inserted"]'''