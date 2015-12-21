# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import json

url = "http://kiranico.com/es/mh4u/monstruo/"

# Realizamos la petición a la web
req = requests.get(url)

# Comprobamos que la petición nos devuelve un Status Code = 200
statusCode = req.status_code
if statusCode == 200:

    # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    html = BeautifulSoup(req.text)

    # Obtenemos todos los divs donde estan las entradas
    script = html.find_all('script',{'class':''})

    # Recorremos todas las entradas para extraer el título, autor y fecha
    fire=''
    ice=''
    thunder=''
    water=''
    dragon=''
    for i,entradas in enumerate(script):
        if i == 5:
            #print entradas
            values = re.findall(r'var.*?=\s*(.*?);', str(entradas), re.DOTALL | re.MULTILINE)
            j=0
            for x in str(values).split(","):
                if x.find("res_fire") != -1 and j < 20:
                    fire += x.split(':')[1].split('\"')[1]
                    fire += " "
                    j+=1
                if x.find("res_thunder") != -1 and j < 20:
                    thunder += x.split(':')[1].split('\"')[1]
                    thunder += " "
                    j+=1
                if x.find("res_water") != -1 and j < 20:
                    water += x.split(':')[1].split('\"')[1]
                    water += " "
                    j+=1
                if x.find("res_ice") != -1 and j < 20:
                    ice += x.split(':')[1].split('\"')[1]
                    ice += " "
                    j+=1
                if x.find("res_dragon") != -1 and j < 20:
                    dragon += x.split(':')[1].split('\"')[1]
                    dragon += " "
                    j+=1
            
    hp = "HP " + str(values).split(',')[1].split(':')[1]
    print hp
    print "Resistencia fuego: " + fire
    print "Resistencia trueno: " + thunder
    print "Resistencia agua: " + water
    print "Resistencia hielo: " + ice
    print "Resistencia dragon: " + dragon
else:
    print "Status Code %d" %statusCode