from selenium import webdriver
driver=webdriver.Chrome('C:\Python27\selenium\webdriver')
driver.set_page_load_timeout(30)
driver.get('http://www.facebook.com')
driver.maximize_window()
driver.implicitly_wait(20)
driver.get_screenshot_as_file("Facebook.png")
driver.quit()
print "OK"