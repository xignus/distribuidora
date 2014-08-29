#-*- coding: utf-8 -*-

import requests
import bs4

enlaces=open('enlaces.txt','r')
productos=open('productos.csv','wb')
imagenes=open('imagenes.csv','wb')

for enlace in enlaces:
    response = requests.get(enlace.strip())
    soup = bs4.BeautifulSoup(response.text)
    print "recolectado enlace %s" %(enlace.strip())
    items = soup.select('.cajaprod')
    images = soup.findAll('img',{"class":"imagen"})


    for image in images:
        imagenes.write(image['src']+"\n")



    for item in items:    
        productos.write(str(item.get_text().encode('utf8')))
    

enlaces.close()
imagenes.close()
productos.close()

