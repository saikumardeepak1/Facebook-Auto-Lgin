from selenium import webdriver
from getpass import getpass
from credentials import username, password

driver = webdriver.Chrome("C:\\Users\\91939\\OneDrive\\Documents\\chromedriver.exe")
driver.get("https://www.facebook.com/")

username_textbox = driver.find_element_by_id("email")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("pass")
password_textbox.send_keys(password)

login_button = driver.find_element_by_name("login")
login_button.submit()
