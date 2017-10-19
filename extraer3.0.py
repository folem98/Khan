# -*- coding: utf-8 -*-
import MySQLdb as mdb
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
path_to_chromedriver = 'C:\Python27\Lib\site-packages\selenium\webdriver\chrome/chromedriver.exe'
import time
import urllib
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX(LOGEO)XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
usr1 = "panquequeprodigio@gmail.com"
pwd1 = "567000504"
pag="Libros Para Regalar,Vender,Comprar y Trueque.. TEMUCO!!"
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
#    browser.maximize_window()
browser.get('http://www.facebook.com')
assert "Facebook" in browser.title
time.sleep(5)
elem = browser.find_element_by_id("email")
elem.send_keys(usr1)
elem = browser.find_element_by_id("pass")
elem.send_keys(pwd1)
elem.send_keys(Keys.RETURN)

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX(ABRIR COMPRA Y VENTA)XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
browser.get('https://www.facebook.com/groups/librosdetemuco/')
assert "Libros Para Regalar,Vender,Comprar y Trueque.. TEMUCO!!!" in browser.title
url = urllib.urlopen("https://www.facebook.com/groups/librosdetemuco/")

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX(SCROLL HACIA ABAJO PARA ABARCAR MAS INFO)XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
scroll=30
while scroll!=0:
    scroll=scroll-1
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX(OBTENCION DE CONTENIDO)XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
id1='u_0_1l'
id2='u_jsonp_4_x'
id3='u_0_1j'
id4='u_0_1k'
element = browser.find_element_by_id('u_0_1k')
contenido = element.text

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX(ORDENAR CONTENIDO E INSERTAR EN BD)XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
bd = mdb.connect('localhost','root','','taller', charset='utf8')
cursor=bd.cursor()
query="delete from scraping where 1"
cursor.execute(query)
bd.commit()
contenido = contenido[contenido.find("PUBLICACIONES DESTACADAS")+24:contenido.find("Publicaciones anteriores")+24]
veces=50
while veces!=0:
    nombre=""
    fecha=""
    descripcion=""
    precio=""
    veces=veces-1
    print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    print "nombre: ",contenido[1:contenido.find("\n", 1,len(contenido))]
    nombre=contenido[1:contenido.find("\n", 1,len(contenido))]
    contenido=contenido[contenido.find("\n", 1,len(contenido)):len(contenido)]

    print "hace: ",contenido[1:contenido.find("\n", 1, len(contenido))]
    fecha=contenido[1:contenido.find("\n", 1, len(contenido))]
    contenido=contenido[contenido.find("\n", 1,len(contenido)):len(contenido)]
    if 'Me gusta' not in contenido[1:contenido.find("\n", 1, len(contenido))]:
        print "descripcion: ",contenido[1:contenido.find("\n", 1, len(contenido))]
        descripcion=contenido[1:contenido.find("\n", 1, len(contenido))]
        contenido=contenido[contenido.find("\n", 1,len(contenido)):len(contenido)]
    if 'Me gusta' not in contenido[1:contenido.find("\n", 1, len(contenido))] and 'reacciones' not in contenido[1:contenido.find("\n", 1, len(contenido))] and 'Enviar mensaje al vendedor' not in contenido[1:contenido.find("\n", 1, len(contenido))]:
        print "precio: ",contenido[1:contenido.find("\n", 1, len(contenido))]
        precio=contenido[1:contenido.find("\n", 1, len(contenido))]
        contenido=contenido[contenido.find("\n", 1,len(contenido)):len(contenido)]
    contenido= contenido[contenido.find('Pulsa "Intro" para publicar.')+28 :len(contenido)]
    query="INSERT INTO scraping (nombre,fecha,descripcion,precio) VALUES ('"+nombre+"','"+fecha+"','"+descripcion+"','"+precio+"');"
    cursor.execute(query)
    bd.commit()
browser.quit()
bd.close()


