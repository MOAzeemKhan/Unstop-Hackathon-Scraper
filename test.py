import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
'''
driver.get('https://unstop.com/hackathons?filters=,all,open,all&types=teamsize,payment,oppstatus,eligible')

# Set up Selenium webdriver
driver = webdriver.Chrome(executable_path='C://chromedriver.exe')

links = driver.find_elements(By.CLASS_NAME, 'listing')

for link in links
# Open the competition link


# Wait for the page to load
time.sleep(5)

# Parse the HTML of the page using Beautiful Soup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the elements containing the dates
registration_deadline_element = soup.find('span', class_='registration-deadline')
start_date_element = soup.find('span', class_='start-date')
end_date_element = soup.find('span', class_='end-date')

# Extract the text content of the elements
registration_deadline = registration_deadline_element.text
start_date = start_date_element.text
end_date = end_date_element.text

# Close the webdriver
driver.close()

# Write the dates to a CSV file
with open('dates.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['Registration Deadline', 'Start Date', 'End Date'])
  writer.writerow([registration_deadline, start_date, end_date])
'''



'''# Set the path to the chromedriver executable
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Open the website
driver.get('https://unstop.com/hackathons?filters=,all,open,all&types=teamsize,payment,oppstatus,eligible')

# Wait for the website to load
driver.implicitly_wait(10)

# Find all the elements containing competition information
elements = driver.find_elements(By.CLASS_NAME, 'listing')

# Initialize an empty list to store the competition information
competitions = []

# Iterate through each element
for element in elements:
  WebDriverWait(driver, 10)
  link = element.get_attribute('href')
  driver.implicitly_wait(10)
  WebDriverWait(driver, 10)
  # Open the competition details page
  driver.get(link)


  driver.implicitly_wait(50)
  # Parse the HTML of the page
  soup = BeautifulSoup(driver.page_source, 'html.parser')

  # Find the deadline element
  deadline_element = soup.find('strong', class_='"ng-tns-c150-2')

  # Extract the deadline text
  deadline = deadline_element.text if deadline_element else 'Deadline not available'

  # Add the competition information to the list
  competitions.append([deadline])

# Close the browser
driver.quit()

# Write the competition information to a CSV file
with open("competitions_deadline.csv", "w", newline="") as f:
  writer = csv.writer(f)
  writer.writerows(competitions)
'''
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from scrapy.http import TextResponse

path_driver = 'C://chromedriver.exe'
driver = webdriver.Chrome(executable_path=path_driver)
driver.get('https://unstop.com/hackathons?filters=,all,open,all&types=teamsize,payment,oppstatus,eligible')
registration_deadlines = []
links = driver.find_elements(By.CLASS_NAME, 'listing')
apply_links = []

# Iterate through the list of elements and extract the links
for link in links:
    temp_link = link.get_attribute('href')
    apply_links.append(temp_link)

for link in apply_links: #Working
    driver.get(link)
    response = TextResponse(driver.current_url, body=driver.page_source, encoding='utf-8')
    deadline = response.xpath('//div[@class="ng-star-inserted"]/strong/text()').extract_first()
    print(deadline)
    registration_deadlines.append(deadline)
print(registration_deadlines)'''

# Import necessary libraries
from selenium import webdriver
from scrapy.selector import Selector
import requests
import time


'''def get_deadline(link):
  # Use selenium to access the link
  driver = webdriver.Chrome()
  driver.get(link)

  # Use scrapy's Selector to parse the HTML and locate the element containing the deadline
  html = driver.page_source
  selector = Selector(text=html)
  deadline_element = selector.css('.deadline-class-name')

  # Extract the deadline from the element
  deadline = deadline_element.extract()

  # Close the browser
  driver.close()

  return deadline
'''

# Set up Selenium webdriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://unstop.com/hackathons?filters=,all,open,all&types=teamsize,payment,oppstatus,eligible")

# Wait for the page to load
time.sleep(5)

# Use Selenium to find all the hackathon links on the page
hackathon_links = driver.find_elements(By.CLASS_NAME, 'listing')
ls = []
# Loop through each hackathon link
for link in hackathon_links:
  # Get the link for each hackathon
  hackathon_url = link.get_attribute("href")
  print(hackathon_url)

  # Use Scrapy to scrape the registration deadline for each hackathon
  response = Selector(text=requests.get(hackathon_url).text)
  '''deadline = response.xpath("//span[@class='date ng-star-inserted']/text()").extract_first()'''
  deadline = response.xpath("//span[contains(text(), 'Registration Deadline')]").get()
  print(deadline)
  ls.append(deadline)

print(ls)
# Close the webdriver
driver.close()
