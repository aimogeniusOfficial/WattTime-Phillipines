
from selenium import webdriver
import time
import pandas as pd #to read excel file
# from selenium.webdriver.common.keys import Keys

#Initialize variables:

#===================================================================#

#Resulting array of all the data from the table
column_info = []

#Table dimensions
rows = 0
columns = 0

#===================================================================#

#Function to obtain data from the website
def getData():

    #initialize driver:

    website = 'https://www.ngcp.ph/operations#situation'

    #user agent
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36")

    # disable webdriver
    options.add_argument("--disable-blink-features=AutomationControlled")

    #path
    path = './chromedriver.exe'
    driver = webdriver.Chrome(path, options = options)

    #Processing
    try:
        #Click on the "Weekly Outlook" button
        url = driver.get(url = website)
        time.sleep(2)
        weekly_button = driver.find_element_by_xpath('//div[@id="carousel-operation-body"]/div/div[@class="item active"]/ul/li[3]/span')
        weekly_button.click()
        time.sleep(5)
        #Click on the "Visayas" button
        place_button = driver.find_element_by_link_text("VISAYAS")
        place_button.click()
        time.sleep(5)

    except Exception as ex:
        print(ex)

    #Get data from the website
    columns_names = driver.find_elements_by_xpath ('//table[@id="table-WeeklyLuzon"]/tbody/tr/td')
    #Get dimensions
    rows = len(driver.find_elements_by_xpath('//table[@id="table-WeeklyLuzon"]/tbody/tr'))
    columns = len(driver.find_elements_by_xpath('//table[@id="table-WeeklyLuzon"]/tbody/tr[2]/td'))

    #Convert columns_names from html element to text and write it into an array
    for i in columns_names:
        column_info.append(i.text)
    
    #quit
    driver.quit()
    return column_info, rows, columns

#Process column_info
def processData(infoArray, rows, columns):
    #Create a dict for pandas
    mw =  [infoArray [columns * i] for i in range(rows - 1)]
    thu = [infoArray [columns*i + 1] for i in range (rows - 1)]
    fri = [infoArray [columns*i + 2] for i in range (rows - 1)]
    sat = [infoArray [columns*i + 3] for i in range (rows - 1)]
    sun = [infoArray [columns*i + 4] for i in range (rows - 1)]
    mon = [infoArray [columns*i + 5] for i in range (rows - 1)]
    tue = [infoArray [columns*i + 6] for i in range (rows - 1)]
    wed = [infoArray [columns*i + 7] for i in range (rows - 1)]

    dict = {
        mw[0]: mw[1:],
        thu[0]: thu[1:],
        fri[0]: fri[1:],
        sat[0]: sat[1:],
        sun[0]: sun[1:],
        mon[0]: mon[1:],
        tue[0]: tue[1:],
        wed[0]: wed[1:]
    }

    #Create a pandas DataFrame
    df = pd.DataFrame(dict)
    #Convert to csv
    df.to_csv ('Luzon.csv')

#Execution
if __name__ == '__main__':
    print("Starting the Program...\n\n\n")
    #Until the program gives a result...
    while column_info == []:
        #Get data
        infoArray, rows, columns = getData()
    #And then Process the Data
    processData(infoArray, rows, columns)
    print("\n\n\nFinished Execution.")
