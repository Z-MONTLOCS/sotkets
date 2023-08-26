import asyncio
import websockets
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import os




# Importaciones locales
from websockets_vesb.config_utils import (
    initialize_driver,
    seleccionar_tipo_documento_y_identificacion,
    switch_to_new_tab,
    get_data_table,
    close_browser,
    get_affiliation_table,
    extract_names,
    close_driver,
    click_send,download_captcha_image,
    solve_captcha_and_click_button,solve_captcha

)

# Diccionario para mapear sockets a IDs de conexión
socket_to_id = {}


print("Generando código para socket ID:")


async def handle_client(websocket, path):

    print("Generando código para socket ID:")

    driver = initialize_driver()


    try:
        print("Generando código para socket ID:")

        while True:

            message = await websocket.recv()

            print("Generando código para socket ID:", message)



            print(f"Generando código para socket ID: {socket_id}")


            if message == "generateCode":
                # Obtener el ID del socket y guardarlo en el diccionario
                socket_id = id(websocket)
                socket_to_id[websocket] = socket_id

                print(f"Generando código para socket ID: {socket_id}")

                page_status = True

            if page_status == True:    
                await websocket.send(json.dumps(page_status))

                driver = initialize_driver()

                # Enviar la URL de la imagen al cliente para que la cargue automáticamente
                captcha_file = download_captcha_image(driver)
                await websocket.send(json.dumps({"imageLink": captcha_file}))

                page_status = False


            if message == "generateCode":
                 infoData = await websocket.recv()
                 print(f"Código generado por el cliente: {infoData}")

                 

                    # Parse JSON data into a dictionary
                 infoData_dict = json.loads(infoData)

                 #seleccionar_tipo_documento_y_identificacion(driver, infoData_dict)


                 solve_captcha_and_click_button(driver, infoData_dict)

                 texto_span=solve_captcha(driver)
                 #print(f"Código no es valido: {texto_span}")


            if texto_span == "El codigo ingresado no es valido":

                code_status = False


                print(f"Código no es valido: {texto_span}")
                await websocket.send(json.dumps(code_status))





   
   
            #driver.switch_to.window(driver.window_handles[-1])
            switch_to_new_tab(driver)

            
            
            information = get_data_table(driver)

            
           

           
        
        
            affiliation_info = get_affiliation_table(driver)


            if affiliation_info == None:

                elemento_span = driver.find_element(By.ID, 'lblError')

             # Obtener el texto del elemento span
                elemento_span = elemento_span.text


                print(f"Usuario no existe: {elemento_span}")

                await websocket.send(json.dumps({"error_message": elemento_span}))


            
            

        
            driver.execute_script("window.stop();")

            driver.quit()


        
        
            names_surnames_info = extract_names( information['NOMBRES'], information['APELLIDOS'])
        
        
   #               Create the info dictionary with the assigned values
            info = {
            'first_name': names_surnames_info['first_name'],
            'middle_name': names_surnames_info['middle_name'],
            'last_name': names_surnames_info['first_surname'],
            'second_last_name': names_surnames_info['second_surname'],
            'eps': affiliation_info['EPS'] 
}  


            
            # Convertir el diccionario 'info' a una cadena JSON
            info_json = json.dumps({"info": info})

                # Enviar la información al cliente para que la cargue automáticamente
            await websocket.send(info_json)
           
        
        
            # Mostrar los resultados
            print('Información:')
            print('Primer nombre:', info['first_name'])
            print('Segundo nombre:', info['middle_name'])
            print('Primer apellido:', info['last_name'])
            print('Segundo apellido:', info['second_last_name'])
            print('EPS:', affiliation_info['EPS'])


            

            



                    


            


    except Exception as e:
        # Resto de tu código para manejar excepciones
        
        print("=================hhhhhhhhh================================",e)


PORT = int(os.environ.get('PORT', 10000))

print(f"La aplicación se está ejecutando en el puerto: {PORT}")


start_server = websockets.serve(handle_client, "0.0.0.0", PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()