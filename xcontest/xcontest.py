import os
import re
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


URL_PATTERN = 'https://www.xcontest.org/world/en/flights-search/?filter%5Bpoint%5D={long}%20{lat}&filter%5Bradius%5D=1000&filter%5Bmode%5D=START&filter%5Bdate_mode%5D=dmy&filter%5Bdate%5D={iso_date}&filter%5Bvalue_mode%5D=dst&filter%5Bmin_value_dst%5D=&filter%5Bcatg%5D=&filter%5Broute_types%5D=&filter%5Bavg%5D=&filter%5Bpilot%5D=&list%5Bsort%5D=pts&list%5Bdir%5D=down'
SITE_GEOLOC = {
                    #'Rammi':{'Long':10.430767, 'Lat':51.88985}
                    'Metzingen': {'Long':10.370157, 'Lat': 52.669415}
                    #,'Kella':{'Long':10.079683, 'Lat': 51.242917}
                    #,'Königszinne':{{'Long': 9.52568  'Lat': 51.9779}
                    #,'Nyikom':{'Long':19.76122, 'Lat':47.909978}                    
                    #,'Szarsomlyo':{'Long':18.410295, 'Lat': 45.855307}
            }
DELAY = 1 # seconds



def login():
    
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument('log-level=3')
    
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver = webdriver.Chrome(options=options)
    try: 
        driver.get('https://www.xcontest.org/')
        wait=WebDriverWait(driver, DELAY)
        results = wait.until(EC.presence_of_element_located((By.ID, "login-username")))
        username = driver.find_element(By.ID,"login-username")
        password = driver.find_element(By.ID,"login-password")
        submit = driver.find_element(By.CSS_SELECTOR,"input[type='submit']")
        username.send_keys(os.environ['XCONTEST_USER'])
        password.send_keys(os.environ['XCONTEST_PASS'])
        submit.click()    
    except TimeoutException:
        print("Couldn't load page")

    return driver

def load_from_file(launch):
    with open(os.environ['FLIGHT_DAYS_TXT'],'r') as f:
        rows = f.read()

    return rows

def save_to_file(flight_day_list):
    with open(os.environ['FLIGHT_DAYS_TXT'],'w') as f:
        for day in flight_day_list:
            f.write(f"{day}\n")

def flight_days(driver, launch):
    if launch not in SITE_GEOLOC:
        print('Takeoff ID not defined')
        return []


    #
    iso_date = '2024-01-01' # does not matter
    long, lat =  SITE_GEOLOC[launch]['Long'], SITE_GEOLOC[launch]['Lat']
    url = eval(f"f'{URL_PATTERN}'")  
    driver.get(url)
    wait=WebDriverWait(driver, DELAY)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#filter-flights > div > p > strong")))
    filter_date_dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#filter-date.short"))
    options = [x.text for x in filter_date_dropdown.options if re.fullmatch('^\d{2}.\d{2}.\d{4}$',x.text)]
    print(options )
    
    return options



def get_launch_day(driver, launch, iso_date):
    if launch not in SITE_GEOLOC:
        print('Takeoff ID not defined')
        return []
    
    # first page should be enough...
    long, lat =  SITE_GEOLOC[launch]['Long'], SITE_GEOLOC[launch]['Lat']
    url = eval(f"f'{URL_PATTERN}'")
    #print(url)
    driver.get(url)
    wait=WebDriverWait(driver, DELAY)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#filter-flights > div > p > strong")))
    counter= driver.find_elements(By.CSS_SELECTOR, "#filter-flights > div > p > strong")
    #print(counter)
    flights = []
    if counter:
        #print(counter)
        flights_source=driver.find_elements(By.CSS_SELECTOR, "table.flights")
        soup = BeautifulSoup(flights_source[0].get_attribute('outerHTML'), 'html.parser')
        table= soup.find('table',{'class':'flights'})
        for row in table.findChildren('tr')[1:]:
            cols = row.findAll('td')
            flight = cols[0]['title']
            flight_id = flight[flight.find('FLID:')+5:]                       
            launch = cols[3].find('a').text + ' (' +  cols[3].find('span',{'class':'cic'}).text + ')'
            flight_type = cols[4].find('div')['title']
            flight_length = cols[5].find('strong').text
            flight_points = cols[6].find('strong').text
            #flight_duration = cols[6].find('strong').text
            glider = cols[7].find('div')['title']
            details = cols[9].find('a')['href']
            #print([flight_id, launch,flight_type,flight_length,flight_points,glider,details])
            flights.append([iso_date, flight_id, launch,flight_type,flight_length,flight_points,glider,details])

    print(len(flights))
    
    return flights



if __name__=='__main__':
    print("testing connection...")

    load_dotenv()

    driver = login()

    fligtht_day_list= flight_days(driver, 'Metzingen')

