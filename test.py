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



# Set the path to the chromedriver executable
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
  '''driver.implicitly_wait(10)'''
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
