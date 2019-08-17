from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.chrome.service as service
import time
import requests

def change_date(element, date = 12311900 ):
    element.click()
    element.send_keys(Keys.ARROW_LEFT)
    element.send_keys(Keys.ARROW_LEFT)
    element.send_keys(date)
    return



url = r'http://www.buffalo.oarsystem.com/SearchOARS.aspx'

# Setting up selenium
path_to_chrome = r'C:\Users\Dylan\Desktop\chromedriver_win32\chromedriver.exe' 
service = service.Service(path_to_chrome)
service.start()
capabilities = {'chrome.binary': path_to_chrome}
driver = webdriver.Remote(service.service_url, capabilities)
driver.get(url)


# Click 'Advanced Search' button
# switch to iframe with button in it
iframe = driver.find_element_by_xpath("//iframe[@id='dnn_ctr435_IFrame_htmIFrame']")
driver.switch_to.frame(iframe)

python_button = driver.find_elements_by_xpath("//*[@value='Advanced Search']")[0]
python_button.click()


# Set the correct date for the drop down menus
date = '01012010' # [yyyy,dd,mm] 
begin_date = driver.find_elements_by_xpath("//*[@name='startDate']")[0]
change_date(begin_date, date)

date = '01012011'
end_date = driver.find_elements_by_xpath("//*[@name='endDate']")[0]
change_date(end_date,date)

# Click the Submit button
submit_button = driver.find_elements_by_xpath("//*[@value='Submit']")[0]
submit_button.click()

# # Quit the driver
time.sleep(5) # Let the user actually see something!
driver.quit()


#### This program uses selenium but I have found a URL that we can modify searches better.

