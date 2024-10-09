import requests
from bs4 import BeautifulSoup

# Guardar la petición para el acceso a la URL
pagina = requests.get('https://www.kaggle.com/datasets/sanjanapatil7/largest-companies-in-usa-by-revenue')

# Verifico que la solicitud fue exitosa ya que estoy teniendo problemas con la salida
if pagina.status_code == 200:
    print("Solicitud exitosa")
else:
    print(f"Error en la solicitud: {pagina.status_code}")

soup = BeautifulSoup(pagina.text ,'html.parser')
print(soup.prettify())
# Busca los objetos con la etiqueta deseada y la clase concreta que hay en esta web
empresas_objetos = soup.find_all('div', class_='sc-jHCGmr sc-ewOTSi cJSYVK hirQyM')



# Iteramos sobre el array items  para introducir en una variable el valor que queremos extraer, e imprimo para ver como sale
for empresa in empresas_objetos:
    ranking = empresa.find_all('div')[0].text
    nombre = empresa.find_all('div')[1].text
    industria = empresa.find_all('div')[2].text
    ganancia = empresa.find_all('div')[3].text
    margen_beneficio = empresa.find_all('div')[4].text
    empleados = empresa.find_all('div')[5].text
    localizacion = empresa.find_all('div')[6].text
    print(f"CREATE (c:Company {{ranking: '{ranking}', nombre: '{nombre}', industria: '{industria}', ganancia: '{ganancia}', margen_beneficio: '{margen_beneficio}', empleados: '{empleados}', localizacion: '{localizacion}'}});")
