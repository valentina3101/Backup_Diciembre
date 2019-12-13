from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
import urllib.request
import bs4

def bajar(url):
    req = urllib.request.Request(url) #Peticionde url
    req.add_header('User-Agent', 'Mozilla/5.0') # le dice q la peticion es de Mozilla
    r = urllib.request.urlopen(req)
    return BeautifulSoup(r.read())

#var = "scraping" # Busqueda seleccionada
dir = "https://www.educacionit.com/empleos"
detalle = "https://www.educacionit.com/"
coso = urllib.request.urlopen(dir) #baja la pagina
sopa = BeautifulSoup(coso.read(), "lxml")
#print (sopa.body)

lista_de_empleos = sopa.findAll('h3') #para encontrar todos
lista_de_enlaces=[]
#ubicaciones = sopa.findAll('h3', class_="mt15 mb5")
#email = sopa.findAll('strong')

for c in range (2,len(lista_de_empleos)-2):
    empleo = lista_de_empleos[c]
    #lista de links
    link = (detalle + empleo.a["href"])
    #print (link)
    lista_de_enlaces.append(link)
    print (lista_de_enlaces)

remuneraciones = sopa.span.findAll('Remuneracion')
for remuneracion in remuneraciones:
    print (remuneracion)









