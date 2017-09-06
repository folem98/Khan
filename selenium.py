from selenium import webdriver
chrome_path = "C:\SeleniumDrivers\chromedriver_win32\chromedriver.exe"
browser = webdriver.Chrome(chrome_path)
browser.get("https://www.facebook.com")
user = browser.find_element_by_css_selector('#email')
user.send_keys('')
password = browser.find_element_by_css_selector('#pass')
password.send_keys('')
login=browser.find_element_by_css_selector('#loginbutton')
login.click()
