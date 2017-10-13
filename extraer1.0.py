from selenium import webdriver
from selenium.webdriver.common.keys import Keys
path_to_chromedriver = 'C:\Python27\selenium\webdriver\Chrome/chromedriver.exe'
import time
import urllib
usr1 = "panquequeprodigio@gmail.com"
pwd1 = "567000504"
pag="Libros Para Regalar,Vender,Comprar y Trueque.. TEMUCO!!"
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
element = browser.find_element_by_id('u_0_1l')
contenido=element.text
browser.quit()
contenido= contenido[contenido.find("PUBLICACIONES DESTACADAS")+24:contenido.find("Publicaciones anteriores")+24] #RECORTA CONTENIDO UTIL
veces=4
while veces!=0:
    print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    veces=veces-1
    print "nombre: ",contenido[1:contenido.find("\n", 2, 30)]
    contenido=contenido[contenido.find("\n", 1,30):len(contenido)]
    print "hace: ",contenido[1:contenido.find("\n", 1, 30)]
    contenido=contenido[contenido.find("\n", 1,30):len(contenido)]
    if 'Me gusta' not in contenido[1:contenido.find("\n", 1, 30)]:
        print "descripcion: ",contenido[1:contenido.find("\n", 1, 30)]
        contenido=contenido[contenido.find("\n", 1,30):len(contenido)]
    if 'Me gusta' not in contenido[1:contenido.find("\n", 1, 30)] and 'reacciones' not in contenido[1:contenido.find("\n", 1, 30)]:
        print "precio: ",contenido[1:contenido.find("\n", 1, 30)]
        contenido=contenido[contenido.find("\n", 1,30):len(contenido)]
    contenido= contenido[contenido.find("para publicar.")+14:len(contenido)]
