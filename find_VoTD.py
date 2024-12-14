#Versión 3 busca la referencia en bible.com
#luego con ella busca en la biblia de bible.com con idioma esp latino y reina valera 2015

import requests
from bs4 import BeautifulSoup

# Realizamos la solicitud HTTP a la página
res = requests.get('https://www.bible.com/')
soup = BeautifulSoup(res.text, 'lxml')

# Buscamos el elemento <a> con la clase específica para la referencia
a_tag = soup.find('a', class_="no-underline font-11 text-gray-50")

# Extraemos el valor del atributo href de la referencia y obtenemos solo lo que viene después del último "/"
ref = a_tag['href'].split('/')[-1] if a_tag else 'No se encontró el enlace'

#acá se incluye el código que determina el idioma y la versión a usar de la biblia.
#se puede obtener entrando a bible.com, seleccionando idioma y versión y luego verlo en la url
#ejemplo: español reina valera = https://www.bible.com/bible/Código_Que_Necesitamos/...
lang_vers = 1782

urlVersiculo = f'https://www.bible.com/bible/{lang_vers}/{ref}'
#print(urlVersiculo)

res2 = requests.get(urlVersiculo)
soup2 = BeautifulSoup(res2.text, 'lxml')  # Usamos res2 y soup2 para el segundo análisis

# Buscamos el div con la clase específica para el versículo
div = soup2.find('p', class_="text-text-light dark:text-text-dark text-17 md:text-19 leading-default md:leading-comfy font-aktiv-grotesk font-medium mbe-2")

# Extraemos el texto del versículo
votd = f'"{div.text}"' if div else 'No se encontró el texto'
#print(votd)

# Buscamos el div con la clase específica para la referencia al versículo
div2 = soup2.find('h2', class_="text-text-light dark:text-text-dark font-bold font-aktiv-grotesk")
#Extraemos el texto del versículo
refVers = div2.text if div else 'No se encontró el texto'
#print(refVers)

votdfull = f"{votd}\n{refVers}"
#print(votdfull)