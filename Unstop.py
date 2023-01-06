import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# All required info:
url = 'https://unstop.com/hackathons?filters=,all,open,all&types=teamsize,payment,oppstatus,eligible'
path_driver = 'C://chromedriver.exe'
xpath_endpage = "//div[@class='click_here mt-20 ng-star-inserted']"
xpath_main = '//app-opportunity-listbox[@class="ng-star-inserted"]'
xpath_names = './/h2[@class="double-wrap ng-star-inserted"]'
xpath_inst = './/h3[@class="double-wrap ng-star-inserted"]'

# create the webdriver object and specify the path to chromedriver
driver = webdriver.Chrome(executable_path=path_driver)

# open the website
driver.get(url)
driver.maximize_window()
'''cookie = driver.find_element(By.XPATH, "//button[contains(text(), 'Ok, Continue']")'''
while True:
    try:
        driver.find_element(By.XPATH, xpath_endpage)
        break
    except:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

hackathon_list_element = driver.find_element(By.XPATH, xpath_main)

# Find the elements containing the hackathon names
hackathon_name_elements = hackathon_list_element.find_elements(By.XPATH, xpath_names)


# extract the text from each element and store it in a list
hackathon_names = [element.text for element in hackathon_name_elements]

links = driver.find_elements(By.CLASS_NAME, 'listing')
apply_links = []

# Iterate through the list of elements and extract the links
for link in links:
    temp_link = link.get_attribute('href')
    apply_links.append(temp_link)

institutions = driver.find_elements(By.XPATH, xpath_inst)

# Create a list to store the institution names
institution_names = [element.text for element in institutions]

'''date = []
date_elements = driver.find_elements(By.XPATH, "//div[@class='registered']")
for i in range(len(hackathon_names)):
  date_string = date_elements[i].text
  last_date_to_apply = date_string.split(" ")[-1]
  date.append(last_date_to_apply)
'''
print(apply_links)
print(hackathon_names)
print(institution_names)

competitions = [["Hackathons", "Institutions", "Links"]]
for i in range(len(hackathon_names)):
    competitions.append([hackathon_names[i], institution_names[i], apply_links[i]])
with open("competitions.csv", "w", newline="") as f:
  writer = csv.writer(f)
  writer.writerows(competitions)

def scrape_date(apply_links):
    date=[]
    for i in range(len.(apply_links)):
        temp_driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
        url = apply_links[i]
        temp_driver.get(url)
        temp_date = driver.find_element(By.XPATH, '//strong[@class="ng-tns-c147-1"]')
        date.append(temp_date)
    return date

fun_date = scrape_date(apply_links)
print(fun_date)


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