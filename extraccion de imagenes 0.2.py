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
images = browser.find_elements_by_tag_name('img')
con = 0
for image in images:
    uimg = image.get_attribute('src') # Url de la imagen
    print uimg
    urllib.urlretrieve(uimg,'img %d.jpg'%(con))
    con +=1


#https://scontent.faep3-1.fna.fbcdn.net/v/t31.0-8/22553077_2365217903704117_3377287580353045576_o.jpg?oh=3b24d5618e86d69543dda2b37db1b0e0&oe=5A6DD330
#https://scontent.faep3-1.fna.fbcdn.net/v/t31.0-8/22553077_2365217903704117_3377287580353045576_o.jpg?oh=49730da4956b95b45eb8c6f759a01bea&oe=5A73F32C
#https://scontent.faep3-1.fna.fbcdn.net/v/t31.0-8/22553077_2365217903704117_3377287580353045576_o.jpg?oh=49730da4956b95b45eb8c6f759a01bea&oe=5A73F32C
#https://scontent.faep3-1.fna.fbcdn.net/v/t1.0-9/22688783_10155772442709061_7470663696022306145_n.jpg?oh=7a9ae5a515cc1d7e9c16c19eb6e7e12c&oe=5A81EC11
browser.quit()