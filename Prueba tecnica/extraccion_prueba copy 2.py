from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Configurar el navegador
driver = webdriver.Chrome()

# Abrir la página web
driver.get('https://www.kaggle.com/datasets/sanjanapatil7/largest-companies-in-usa-by-revenue')

# Esperar a que se cargue el contenido dinámico
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'sc-jHCGmr sc-ewOTSi cJSYVK hirQyM'))
    )
    print("Contenido cargado")
except:
    print("Error al cargar el contenido")

# Obtener el HTML de la página
pagina = driver.page_source

# Cerrar el navegador
driver.quit()

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
