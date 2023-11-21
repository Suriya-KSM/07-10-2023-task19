from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException



class web_page:
   username = "standard_user"
   password = "secret_sauce"
   
   def __init__(self):
        self.url = "https://www.saucedemo.com/"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #maximizing the window
        self.driver.maximize_window()

   def login(self):
       try:
            self.driver.get(self.url)
            sleep(2)

            #Login process by finding username and password
            self.driver.find_element(by=By.ID, value="user-name").send_keys(self.username)
            sleep(3)

            self.driver.find_element(by=By.ID, value="password").send_keys(self.password)           
            sleep(3)

            self.driver.find_element(by=By.ID, value= "login-button").click()           
            sleep(5)

            #Fetching the title of the webpage. 
            print("Webpage Title:",self.driver.title,"\n")
           
            #Fetching the Current URL of the webpage
            print("Current URL for the webpage is:",self.driver.current_url,"\n")
           
            #Extrating the entire content from the webpage and placing it in a text file
            text_file="Webpage_task_11.txt"
           
            t = open(text_file, "w")
            t.write(self.driver.find_element(By.XPATH, "/html/body").text)
            t.close()

            print('Contents of the webpage saved in the ',text_file, ' file\n')
          
        #Exception handling
       except NoSuchElementException as selenium_error:
            print("Element not found", selenium_error)
        
       finally:
            self.driver.close()

#creating object for the class
obj = web_page()

#calling the function using object
obj.login()
