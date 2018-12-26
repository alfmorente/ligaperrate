from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

URL_BIWENGER = 'https://biwenger.as.com/login'

traduccion_usuarios = {'Joselillo': 'JoseAngel','Ale':'Ale','Karre':'Carre','Pepe':'Pepe','Moren':'Moren',
                       'Nando':'Nando','Vega':'Vega','Manuel':'Baeza','Francisco':'Paco','Jose':'Jose',
                       'Frangallego':'Fran','Daniel':'Dani','Manolo':'Manolo'}

driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
# driver = webdriver.PhantomJS()
driver.implicitly_wait(4)
driver.get(URL_BIWENGER)
driver.find_element_by_tag_name('button').click()
cuadro_email = driver.find_element_by_name('email')
cuadro_email.send_keys('lephor2@yahoo.es')
cuadro_password = driver.find_element_by_name('password')
cuadro_password.send_keys('bvdhkj')
boton_acceder = driver.find_element_by_tag_name('button')
boton_acceder.send_keys(Keys.RETURN)
# boton_jornada = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'nav-round')))
# boton_jornada.click()
try:
    driver.find_element('id', 'nav-round').click()
except Exception as ex:
    print(str(ex))
    driver.quit()
# Ya estamos en la pantalla de jornada
# TODO leer la tabla con los puntos
tabla_resultados = driver.find_element_by_css_selector('table.table.condensed.text-right.selectable')
filas = tabla_resultados.find_elements_by_tag_name('tr')
for fila in filas:
    if fila.text.split()[1] in traduccion_usuarios:
        print('{} tiene {} puntos'.format(traduccion_usuarios[fila.text[1]],fila.text[4]))
driver.quit()
