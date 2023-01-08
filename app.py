from flask import Flask
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from flask import Flask, request, send_file
from flask import render_template

def date_extractor(date):
    current_date = datetime.now()
    strin = date
    x = strin.split("left")
    x = x[0]
    if 'day' in x:
      x = x.split("day")
      x = x[0]
      x = int(x)
      final_date = current_date + timedelta(days=x)
      return final_date.strftime("%d-%m-%Y")
    elif 'days' in x:
      x = x.split("days")
      x = x[0]
      x = int(x)
      final_date = current_date + timedelta(days=x)
      return final_date.strftime("%d-%m-%Y")
    elif 'hours' in x:
      x = x.split("hours")
      x = x[0]
      final_date = current_date + timedelta(hours=int(x))
      return final_date.strftime("%d-%m-%Y")
    else:
      if 'months' in x:
        x = x.split("months")
      else:
        x = x.split("month")
      x = x[0]
      x = int(x)
      final_date = current_date + timedelta(days=x * 30)
      return final_date.strftime("%d-%m-%Y")

def scrape_website(url):
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
    registration_deadlines = []

    date = []
    time_left_elements = driver.find_elements(By.XPATH, './/strong[@class="ml-5"]')
    time_left = []

    count_time_left = 0
    for element in time_left_elements:
        time_left.append(element.text)

    count_date = 0
    for i in range(1, len(time_left), 2):
        temp = time_left[i]
        new_date = date_extractor(temp)
        date.append(new_date)

    date.append('Not Found')
    competitions = [["Hackathons", "Institutions", "Links", "Registration Deadline"]]
    for i in range(len(hackathon_names)):
        competitions.append([hackathon_names[i], institution_names[i], apply_links[i], date[i]])
    with open("competitions.csv", "w", newline="") as f:
      writer = csv.writer(f)
      writer.writerows(competitions)
    f.close()

    return f
    # close the browser
    driver.close()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
  # get the URL from the form
  url = request.form['url']

  # call your function to scrape the website and generate the CSV file
  csv_file = scrape_website(url)
  print(csv_file)

  # send the CSV file as a response
  return send_file(csv_file, as_attachment=True, download_name='hackathons.csv')

if __name__ == '__main__':
  app.run()
