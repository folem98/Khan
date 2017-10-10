from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import urllib
usr1 = "lalistadelosdatosolvidados@gmail.com"
pwd1 = "123456789z"
pag="Libros Para Regalar,Vender,Comprar y Trueque.. TEMUCO!!"


path_to_chromedriver = 'C:\Python27\selenium\webdriver\Chrome/chromedriver.exe'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
browser.set_page_load_timeout(30)
#browser.maximize_window()
browser.get('http://www.facebook.com')
assert "Facebook" in browser.title
time.sleep(5)
elem = browser.find_element_by_id("email")
elem.send_keys(usr1)
elem = browser.find_element_by_id("pass")
elem.send_keys(pwd1)
elem.send_keys(Keys.RETURN)
browser.get('https://www.facebook.com/groups/librosdetemuco/')
assert "Libros Para Regalar,Vender,Comprar y Trueque.. TEMUCO!!!" in browser.title
url = urllib.urlopen("https://www.facebook.com/groups/librosdetemuco/")
elem = browser.find_element_by_xpath("//*[@id='u_jsonp_9_1r']/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div")
elem.send_keys(Keys.RETURN)
content = url.readlines()
#for letter in content:
#        f = open("datos.txt","w")
#        f.write(letter),
#        time.sleep(.1)


time.sleep(5);
#f.close()
browser.quit()
print ("")
print ("CONTENIDO ROBADO")
print ("<3")
print ("7u7")