import requests
from bs4 import BeautifulSoup

# Guardar la petición para el acceso a la URL
page = requests.get('https://www.trendencias.com/propuestas-y-consejos/100-peliculas-que-ver-vez-vida')

soup = BeautifulSoup(page.text ,'html.parser')

# Busca los objetos con la etiqueta deseada
blockquote_items = soup.find_all('h3')

# Iteramos sobre el array items  para introducir en una variable el valor que queremos extraer, e imprimo para ver como sale
for blockquote in blockquote_items:
    titulo = blockquote.text
    print(titulo)

