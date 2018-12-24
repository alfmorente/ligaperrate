from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL_BIWENGER = 'https://biwenger.as.com/login'



driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
driver.implicitly_wait(4)
driver.get(URL_BIWENGER)
driver.find_element_by_tag_name('button').click()
cuadro_email = driver.find_element_by_name('email')
cuadro_email.send_keys('lephor2@yahoo.es')
cuadro_password = driver.find_element_by_name('password')
cuadro_password.send_keys('bvdhkj')
boton_acceder = driver.find_element_by_tag_name('button')
boton_acceder.send_keys(Keys.RETURN)
driver.implicitly_wait(10)
driver.find_element('id','nav-round').click()
driver.implicitly_wait(4)
# Ya estamos en la pantalla de jornada
# TODO leer la tabla con los puntos
tabla_resultados = driver.find_element_by_css_selector('table.table.condensed.text-right.selectable')
filas = tabla_resultados.find_elements_by_tag_name('tr')
print('llega aqui')