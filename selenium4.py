from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
usr = "lalistadelosdatosolvidados@gmail.com"
pwd = "123456789z"
pag="Libros para regalar vender comprar y trueque temuco"
path_to_chromedriver = 'C:\Python27\selenium\webdriver\Chrome/chromedriver.exe' # change path as needed
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
browser.set_page_load_timeout(30)
browser.maximize_window()
browser.get('http://www.facebook.com')
assert "Facebook" in browser.title
elem = browser.find_element_by_id("email")
elem.send_keys(usr)
elem = browser.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
elem = browser.find_element_by_css_selector("._1frb")
elem.send_keys(pag)
time.sleep(5)
elem.send_keys(Keys.DOWN)
elem.send_keys(Keys.RETURN)
time.sleep(5)
browser.quit()
print "OK"