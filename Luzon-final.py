
from selenium import webdriver
import time
import pandas as pd #to read excel file
# from selenium.webdriver.common.keys import Keys

#initials:

column_info = []
rows = 0
columns = 0

def getData():
    website = 'https://www.ngcp.ph/operations#situation'

    #user agent
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36")

    # disable webdriver
    options.add_argument("--disable-blink-features=AutomationControlled")

    #path
    path = './chromedriver.exe'
    driver = webdriver.Chrome(path, options = options)

    try:
        url = driver.get(url = website)
        time.sleep(2)
        weekly_button = driver.find_element_by_xpath('//div[@id="carousel-operation-body"]/div/div[@class="item active"]/ul/li[3]/span')
        weekly_button.click()
        time.sleep(5)

    except Exception as ex:
        print(ex)


    columns_names = driver.find_elements_by_xpath ('//table[@id="table-WeeklyLuzon"]/tbody/tr/td')
    rows = len(driver.find_elements_by_xpath('//table[@id="table-WeeklyLuzon"]/tbody/tr'))
    columns = len(driver.find_elements_by_xpath('//table[@id="table-WeeklyLuzon"]/tbody/tr[2]/td'))


    for i in columns_names:
        column_info.append(i.text)
    
    driver.quit()
    return column_info, rows, columns

def processData(infoArray, rows, columns):
    
    mw =  [infoArray [columns * i] for i in range(rows - 1)]
    thu = [infoArray [columns*i + 1] for i in range (rows - 1)]
    fri = [infoArray [columns*i + 2] for i in range (rows - 1)]
    sat = [infoArray [columns*i + 3] for i in range (rows - 1)]
    sun = [infoArray [columns*i + 4] for i in range (rows - 1)]
    mon = [infoArray [columns*i + 5] for i in range (rows - 1)]
    tue = [infoArray [columns*i + 6] for i in range (rows - 1)]
    wed = [infoArray [columns*i + 7] for i in range (rows - 1)]

    dict = {
        'MW': mw,
        'THU': thu,
        'FRI': fri,
        'SAT': sat,
        'SUN': sun,
        'MON': mon,
        'TUE': tue,
        'WED': wed
    }

    df = pd.DataFrame(dict)
    df.to_csv ('Luzon.csv')


if __name__ == '__main__':
    print("Starting the Program...\n\n\n")
    while column_info == []:
        infoArray, rows, columns = getData()
    processData(infoArray, rows, columns)
    print("\n\n\nFinished Execution.")
#df = pd.DataFrame(columns=[s.text for s in columns_names])
#df.to_csv('Visayas.csv')