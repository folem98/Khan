# -*- coding: utf-8 -*-
import MySQLdb as mdb
from bs4 import BeautifulSoup
import bs4 as bs
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
scroll=1
while scroll!=0:
    scroll=scroll-1
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)


html = browser.page_source
soup = bs.BeautifulSoup(html,'lxml')


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX(CONECTAR A LA BD)XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
bd = mdb.connect('localhost','root','','taller', charset='utf8')
cursor=bd.cursor()
query="delete from scraping where 1"
cursor.execute(query)
bd.commit()

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX(OBTENCION DE CONTENIDO)XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
for paragraph in soup.find_all("div", class_="_1dwg"):
    nombre = ""
    fecha = ""
    publica = ""
    descri = ""
    precio = ""
    lk = ""
    var1 = ""
    print "\n"
    for nom in paragraph.find_all("span", class_="fwb"):
        nombre = nom.text
        print "nombre: ",nom.text
        for link in nom.find_all('a'):
            lk= link.get('href')
            print "Link de comunicacion: ",lk

    for fec in paragraph.find_all("span", class_="timestampContent"):
        fecha = fec.text
        print "fecha: ",fec.text

    for pub in paragraph.find_all("div", class_="_l53"):
        publica = pub.text
        print "publicacion: ", pub.text


    for desc in paragraph.find_all("div", class_="_5pbx"):
        descri = desc.text
        if "'" in descri:
            descri = descri.replace("'","")
        if '"' in descri:
            descri = descri.replace('"',"")
        print "descripcion: ", descri
    for prec in paragraph.find_all("div", class_="_l57"):
        precio = prec.text
        print "precio: ", prec.text

    ahora = time.strftime("%Y%m%d")+time.strftime("%I%M%S")
    print "fecha de registro en la pagina: ",ahora
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX(AGREGAMOS A LA BD)XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    query="INSERT INTO scraping (nombre,fecha,publicacion,descripcion,precio,link_com,fecharegpag) VALUES('" +nombre+ "','" +fecha+ "','"+publica+"','"+descri+ "','" +precio+ "','"+lk+"','" + ahora+ "')";

    cursor.execute(query)
    bd.commit()
    ids = "SELECT MAX(id) FROM scraping"
    cursor.execute(ids)
    for row in cursor.fetchall():
        print "id : ",row[0]
        idd = row[0]


    for url in paragraph.find_all('img'):
        var1= url.get('src')
        if 'jpg' in var1:
            if not 'p50x50' in var1:
                print "url: ",var1
                image="INSERT INTO imagenes (id_sc,img) VALUES ("+ str(idd) +",'"+ var1 +"')"
                cursor.execute(image)
                bd.commit()

browser.quit()
bd.close()


