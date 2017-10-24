from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unicodedata
import time
import urllib
usr1 = "lalistadelosdatosolvidados@gmail.com"
pwd1 = "123456789z"
usr=""
pwd=""
pag="Libros Para Regalar,Vender,Comprar y Trueque.. TEMUCO!!"


path_to_chromedriver = 'C:\SeleniumDrivers\chromedriver_win32\chromedriver.exe'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
browser.set_page_load_timeout(30)
browser.maximize_window()
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

#Extraccion del contenido:
element = browser.find_element_by_id('contentArea')
ar = element.text

# Extraccion de Imagenes:
"""
images = browser.find_elements_by_tag_name('img')
con = 0
for image in images:
    uimg = image.get_attribute('src') # Url de la imagen
    print uimg
    urllib.urlretrieve(uimg,'\imagenes\img %d.jpg'%(con))
    con +=1
"""

# Extraccion de contacto:
perf = browser.find_elements_by_tag_name('a')
for p in perf:
    link = p.get_attribute('href') # Url de la imagen
    print link
# se optiene los links para usar como direccion para extraer los datos de contacto

browser.quit()