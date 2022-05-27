# User Guide for Philippines project

<h2>Hello! This is the Walkthrough of the Philippines project code for WattTime.</h2>


First, let's start with the imports. You will need:

    from selenium import webdriver

    import time

    import pandas as pd


Check out any necessary documentation on how to install Selenium and Pandas at: https://selenium-python.readthedocs.io/getting-started.html and https://pandas.pydata.org/docs/getting_started/index.html respectively.

<h3>Moving on to the actual code.</h3>

# Initialize variables:

    #Resulting array of all the data from the table
  
    column_info = []

    #Table dimensions
  
    rows = 0
  
    columns = 0
 
Here, I have initialized three variables. <b>Column_info</b> is an array, where I intend to save the data that will be parsed; while <b>rows</b> and <b>columns</b> will account for the dimensions of the parsed table in order to recreate it using pandas.

# First function: getData()


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
  
  <h3> The code above sets up the Selenium Webdriver to automatically open Chrome. </h3>
  
  We add website and user-agent in order to avoid CAPTCHA. Also, you need to install Google Chrome Driver from  https://chromedriver.chromium.org/downloads. Install the <b>appropriate</b> version of chromedriver in order for the program to work.
  Your path to chromedriver.exe you should put into the <b><i>PATH</i></b> and replace current path with it.
  
  <h3> Getting to the table. </h3>
  
  Since we do not have a table wide-open on the first page of our website, we need to create code to auto-click on the buttons to get to the table.
  

    #Processing
    
    try:
    
        #Click on the "Weekly Outlook" button
    
        url = driver.get(url = website)
    
        time.sleep(2)
    
        weekly_button = driver.find_element_by_xpath('//div[@id="carousel-operation-body"]/div/div[@class="item active"]/ul/li[3]/span')
    
        weekly_button.click()
    
        time.sleep(5)
    
    //  For Visayas only
   
        place_button = driver.find_element_by_link_text("VISAYAS")
    
        place_button.click()
    
        time.sleep(5)   //

    except Exception as ex:
    
        print(ex)
 
  
  Here, we actually open our webdriver. We make him open the website <i>(url=website)</i>, then we make him click on the Weekly Button. If we want the data from Luzon, we stop right here,
  but if we need Visayas, we also click on the Visayas button. I added the delay of 2-5 seconds in order for browser to properly load.
  
  <h3>Scrape the data</h3>
  

    columns_names = driver.find_elements_by_xpath ('//table[@id="table-WeeklyVisayas"]/tbody/tr/td')
    
    rows = len(driver.find_elements_by_xpath('//table[@id="table-WeeklyVisayas"]/tbody/tr'))
    
    columns = len(driver.find_elements_by_xpath('//table[@id="table-WeeklyVisayas"]/tbody/tr[2]/td'))
  
  
  In these lines, we scrape all the data from the data into a columns_names variable, and the dimensions of the table into rows and columns. <b>NOTE:</b> the variable 
  columns_names contains the data in HTML format, which we will process in the next step.
  
  <h3>Process columns_names:</h3>
  
    for i in columns_names:
        column_info.append(i.text)
    
  Here, we put all the data from columns_names into columns_info, transforming the html element into the text.
  
  <h3>Quitting</h3>
    
    driver.quit()
    return column_info, rows, columns
    
  Just quitting. :D
  
  #Second Function:
  
  <h3>Here, we will be processing all the data we scraped.</h3>
  
    def processData(infoArray, rows, columns):
    
    mw =  [infoArray [columns * i] for i in range(rows - 1)]
    thu = [infoArray [columns*i + 1] for i in range (rows - 1)]
    fri = [infoArray [columns*i + 2] for i in range (rows - 1)]
    sat = [infoArray [columns*i + 3] for i in range (rows - 1)]
    sun = [infoArray [columns*i + 4] for i in range (rows - 1)]
    mon = [infoArray [columns*i + 5] for i in range (rows - 1)]
    tue = [infoArray [columns*i + 6] for i in range (rows - 1)]
    wed = [infoArray [columns*i + 7] for i in range (rows - 1)]
  
  As an input into the function we will take 3 variables we talked about before: infoArray (a.k.a. column_info), rows, columns (pretty straightforward)
  
  As we would like to create a dictionary for pandas dataframe, we need to organize the data. All the variables above organize the data by columns, distributing all parsed data by columns.
  
  <h3>Then, we create the dictionary itself.</h3>
  
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
    
  Here, we make first row of the parsed data to be the "header" row, and then assign other data from each variable by columns, creating a nice table.
  
  <h3>Create Pandas Dataframe and get CSV file</h3>
  
    #Create a pandas DataFrame
    df = pd.DataFrame(dict)
    #Convert to csv
    df.to_csv ('Luzon.csv')
  
  Pretty straightforward.
  
  # Execution
  
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

  Here, we make the program repeat until we get our CSV file.
  
  <h3>Thank you!</h3>


