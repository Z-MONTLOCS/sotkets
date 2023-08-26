from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options




import time
import requests
import os
import subprocess 



def initialize_driver():

   # Configuración de opciones para el navegador
    chrome_options = webdriver.ChromeOptions()
    prefs = {
    "profile.default_content_setting_values": {
        "images": 2,  
        "javascript": 2, 
        "css": 2, 
        "plugins": 2,  
    }
}



    path = 'C:/Users/chromedriver-win64/chromedriver.exe'
    service = Service(path)



    try:


        print("************ INICIO VERSION **************")

        CHROME_PATH = os.environ.get('CHROME_PATH', '/opt/render/project/bin/chrome-linux64')
        CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/opt/render/project/bin/chromedriver-linux64')

        print("Installed Chromedriver Version:")
        chromedriver_version_cmd = f"{CHROMEDRIVER_PATH}/chromedriver-linux64/chromedriver --version"
        chromedriver_version_output = subprocess.getoutput(chromedriver_version_cmd)
        print(chromedriver_version_output)
        print("Installed Chrome Version:")
        chrome_version_cmd = f"{CHROME_PATH}/chrome-linux64/chrome --version"
        chrome_version_output = subprocess.getoutput(chrome_version_cmd)
        print(chrome_version_output)

        print("************ FIN VERSION **************")

        print("************ CHROMEDRIVER_PATH Linea 87 **************", CHROMEDRIVER_PATH )

        print("************ CHROMEDRIVER_PATH Linea 102 **************", CHROMEDRIVER_PATH )

        print("************ Driver Linea 106 **************" )
        #chrome_options = webdriver.ChromeOptions()

        options = Options()
       
        PATH_CHROME_PATH = f"{CHROME_PATH}/chrome-linux64/chrome"
       

        options.binary_location =PATH_CHROME_PATH   #chrome binary location specified here
        options.add_argument("--no-sandbox") #bypass OS security model


        options.add_argument('--headless')

        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--disable-extensions")
        #soptions.add_argument("--ignore-ssl-errors=true")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--remote-debugging-port=9222")
        
        options.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        PATH_CHROMEDRIVER_PATH = f"{CHROMEDRIVER_PATH}/chromedriver-linux64/chromedriver"

        service = Service(executable_path=PATH_CHROMEDRIVER_PATH)

        driver = webdriver.Chrome( service=service, options=options)
    

        #driver=webdriver.Chrome()
       
 
        

        website = 'https://aplicaciones.adres.gov.co/bdua_internet/Pages/ConsultarAfiliadoWeb.aspx'

        # Esperar a que cierto elemento esté presente en la página para verificar si la carga fue exitosa
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'btnConsultar'))


            )

            
            #      # Ocultar el botón utilizando JavaScript
            # hide_script = "document.getElementById('btnConsultar').style.display   = 'none';"
            # driver.execute_script(hide_script)


            
           
            print("Página cargada correctamente.")
        except Exception as e:
            print("Error al cargar la página:", e)
            driver.quit()
            raise

        return driver
    except Exception as e:
        print("Error al inicializar el controlador:", e)
        raise





def seleccionar_tipo_documento_y_identificacion(driver, datos):
   
    document_type = datos.get('documentType')  # Use 'documentType' key
    identification_number = datos.get('identificationNumber')  # Use 'identificationNumber' key
    imageCode = datos.get('imageCode')

    #Imprimir los datos en la consola
    print("============Datos recibidos Cliente=================")
    print(" ")
    print("Tipo de documento:", document_type)
    print("Número de identificación:", identification_number)
    print("Codigo:", imageCode)
    print("=================================================")
    print(" ")  
    # Seleccionar el elemento <select> por su id
    elemento_select = Select(driver.find_element(By.ID, 'tipoDoc'))
    elemento_select.select_by_value(document_type)

    # Buscar el elemento por su id
    elemento_input = driver.find_element(By.ID, 'txtNumDoc')
    elemento_input.send_keys(identification_number)

    
    elemento_input = driver.find_element(By.ID, 'btnConsultar')
    time.sleep(8)

    #         # Hacer clic en el botón
    elemento_input.click()

    # driver.close()




def solve_captcha_and_click_button(driver, datos):


    document_type = datos.get('documentType')  # Use 'documentType' key
    identification_number = datos.get('identificationNumber')  # Use 'identificationNumber' key
    imageCode = datos.get('imageCode')

    #Imprimir los datos en la consola
    print("============Datos recibidos Cliente=================")
    print(" ")
    print("Tipo de documento:", document_type)
    print("Número de identificación:", identification_number)
    print("Codigo:", imageCode)
    print("=================================================")
    print(" ")  
    # Seleccionar el elemento <select> por su id
    elemento_select = Select(driver.find_element(By.ID, 'tipoDoc'))
    elemento_select.select_by_value(document_type)

    # Buscar el elemento por su id
    elemento_input = driver.find_element(By.ID, 'txtNumDoc')
    elemento_input.send_keys(identification_number)






    # Buscar el elemento por su id y enviar el texto del captcha
    elemento_input = driver.find_element(By.ID, 'Capcha_CaptchaTextBox')
    elemento_input.send_keys(imageCode)

    # Buscar el elemento por su id
    elemento_input = driver.find_element(By.ID, 'btnConsultar')

    # Esperar antes de hacer clic en el botón (ajusta el tiempo según sea necesario)
    time.sleep(2)

    # Hacer clic en el botón
    elemento_input.click()

    # Esperar después de hacer clic en el botón (ajusta el tiempo según sea necesario)
    time.sleep(2)

   



def click_send(driver):
    # Buscar el elemento por su id
    elemento_input = driver.find_element(By.ID, 'btnConsultar')
    
    # Esperar antes de hacer clic en el botón
    time.sleep(3)

    # Hacer clic en el botón
    elemento_input.click()

def close_driver(driver):
    # Cerrar el controlador de Chrome
    driver.close()    




def switch_to_new_tab(driver):
    driver.switch_to.window(driver.window_handles[-1])





# def get_data_table(driver):
#     data_table = WebDriverWait(driver, 2).until(
#         EC.presence_of_element_located((By.ID, 'GridViewBasica'))
#     )
    
#     data_info = {}

#     # Limitar la búsqueda a un elemento específico si es posible
#     container_element = driver.find_element(By.CLASS_NAME, 'center')
#     rows = container_element.find_elements(By.TAG_NAME, 'tr')

#     for row in rows:
#         cells = row.find_elements(By.TAG_NAME, 'td')
#         if len(cells) == 2:
#             key = cells[0].text
#             value = cells[1].text
#             data_info[key] = value
#         # No imprimir aquí para hacer el proceso más rápido

#     return data_info




def get_data_table(driver):
    try:
        data_table = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, 'GridViewBasica'))
        )

        data_info = {}

        container_element = driver.find_element(By.CLASS_NAME, 'center')
        rows = container_element.find_elements(By.TAG_NAME, 'tr')

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            if len(cells) == 2:
                key = cells[0].text
                value = cells[1].text
                data_info[key] = value

        return data_info

    except NoSuchElementException:
        elemento_span = driver.find_element(By.ID, 'lblError')
        elemento_span_text = elemento_span.text

        print(f"Usuario no existe: {elemento_span_text}")

        # Aquí puedes manejar el mensaje de error y la comunicación con el WebSocket
        #await websocket.send(json.dumps({"error_message": elemento_span}))


    except TimeoutException:
        print("La tabla no está presente en la página.")
        # Manejar el caso de la tabla no presente (puede decidir qué hacer aquí)
        return None



# def get_affiliation_table(driver):
#     affiliation_table = WebDriverWait(driver, 2).until(
#         EC.presence_of_element_located((By.ID, 'GridViewAfiliacion'))
#     )
    
#     affiliation_info = {}
#     affiliation_rows = affiliation_table.find_elements(By.TAG_NAME, 'tr')

#     for affiliation_row in affiliation_rows:
#             affiliation_cells = affiliation_row.find_elements(By.TAG_NAME, 'td')
    
#             if len(affiliation_cells) == 6:
#                 keys = ['Status', 'EPS', 'Regime', 'Effective Date', 'End Date', 'Affiliate Type']
        
#                 for i, key in enumerate(keys):
#                     affiliation_info[key] = affiliation_cells[i].text

   
#     return affiliation_info




def get_affiliation_table(driver):
    try:
        affiliation_table = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, 'GridViewAfiliacion'))
        )
        
        affiliation_info = {}
        affiliation_rows = affiliation_table.find_elements(By.TAG_NAME, 'tr')

        for affiliation_row in affiliation_rows:
            affiliation_cells = affiliation_row.find_elements(By.TAG_NAME, 'td')
    
            if len(affiliation_cells) == 6:
                keys = ['Status', 'EPS', 'Regime', 'Effective Date', 'End Date', 'Affiliate Type']
        
                for i, key in enumerate(keys):
                    affiliation_info[key] = affiliation_cells[i].text

        return affiliation_info

    except NoSuchElementException:
        elemento_span = driver.find_element(By.ID, 'lblError')
        elemento_span_text = elemento_span.text

        print(f"Usuario no existe: {elemento_span_text}")

        # Aquí puedes manejar el mensaje de error y la comunicación con el WebSocket
        #await handle_websocket()

    except TimeoutException:
        print("La tabla de afiliación no está presente en la página.")
        # Manejar el caso de la tabla no presente (puede decidir qué hacer aquí)
        return None






def close_browser(driver):
    driver.quit()



def extract_names(name, last_name):
    names_list = name.split()
    surnames_list = last_name.split()

    first_name = names_list[0] if names_list else None
    middle_name = ' '.join(names_list[1:]) if len(names_list) > 1 else None
    first_surname = surnames_list[0] if surnames_list else None
    second_surname = ' '.join(surnames_list[1:]) if len(surnames_list) > 1 else None

    names_surnames_info = {
        'first_name': first_name,
        'middle_name': middle_name,
        'first_surname': first_surname,
        'second_surname': second_surname
    }


    return names_surnames_info




def download_captcha_image(driver):
    # Encontrar el elemento img por su ID
    elemento_img = driver.find_element(By.ID, 'Capcha_CaptchaImageUP')

    # Obtener la URL de la imagen
    url_imagen = elemento_img.get_attribute('src')

    # Descargar la imagen usando la librería requests
    response = requests.get(url_imagen)

    # Verificar si la descarga fue exitosa
    if response.status_code == 200:
        # Directorio donde se guardará la imagen
        directorio_guardado = 'C:/test-vesb/test-bakend-api-env-phyton/bdua'

        # Nombre de archivo para la imagen
        nombre_archivo = 'imagen_captcha.png'

        # Ruta completa del archivo
        ruta_archivo = os.path.join(directorio_guardado, nombre_archivo)

        # Guardar la imagen en el directorio especificado
        with open(ruta_archivo, 'wb') as archivo:
            archivo.write(response.content)

        # print(f'Imagen guardada en: {ruta_archivo}')
    else:
        print('Error al descargar la imagen')

    captcha_file = url_imagen  # Devolver la ruta completa del archivo de imagen
    return captcha_file






def solve_captcha(driver):
   

    # Esperar después de hacer clic en el botón (ajusta el tiempo según sea necesario)
    time.sleep(2)

    # Encontrar el elemento span por su id
    elemento_span = driver.find_element(By.ID, 'Capcha_ctl00')

    # Obtener el texto del elemento span
    texto_span = elemento_span.text

    # Imprimir el texto
    #print(texto_span)

    return texto_span



















 
