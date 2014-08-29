#-*- coding: utf-8 -*-
import urllib

url="http://www.grupocanale.com"

imagenes = open('imagenes.csv','r')

for imagen in imagenes:
    filename = imagen.split('/')[-1]
    urllib.urlretrieve( url+imagen.strip() ,filename.strip())

imagenes.close()
