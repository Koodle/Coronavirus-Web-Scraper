from selenium import webdriver  # The webdriver is what is performing the actions (links up with browser etc)
from selenium.webdriver.common.keys import  Keys  # Gives us access to the "Enter Key", or "Escape" key so i can press enter in the search bar

PATH = "C:\Program Files (x86)\chromedriver.exe"  # Location of the chrome driver on my system
driver = webdriver.Chrome(PATH)  # Picks the browser that we will be using with selenium

try:
    driver.get("https://www.ovulation-calculators.com/coronavirus/gb/leicester/#reports")  # Opens up a website
except Exception as e:
    print(f"error in loading webpage {e}")

try:
    print(driver.title)  # Will print the title of the Web-Page
    # driver.close()  # closes tab
    # print(driver.page_source)  allows us to view the entire page source code

    search = driver.find_element_by_id("search_cities")  #Finds the search bar on the webpage
    search.send_keys("Leicester")  # enters Leicester into the search bar
    search.send_keys(Keys.RETURN)  # hits enter

    table = driver.find_element_by_tag_name("table")  # plural elements means python will create a list of all the tags specified
    print(table.text)
    print(type(table))

    #driver.quit()  # closes entire browser
except Exception as e:
    print(f"struggled to navigate DOM: {e}")