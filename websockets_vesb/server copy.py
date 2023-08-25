import asyncio
import websockets
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By



# Importaciones locales
from config_utils import (
    initialize_driver,
    seleccionar_tipo_documento_y_identificacion,
    switch_to_new_tab,
    get_data_table,
    close_browser,
    get_affiliation_table,
    extract_names,
    close_driver,
    click_send,download_captcha_image,
    solve_captcha_and_click_button

)

# Diccionario para mapear sockets a IDs de conexión
socket_to_id = {}

# async def handle_client(websocket, path):
#     try:
#         while True:
#             message = await websocket.recv()

#             if message == "generateCode":
#                 # Obtener el ID del socket y guardarlo en el diccionario
#                 socket_id = id(websocket)
#                 socket_to_id[websocket] = socket_id


#                 print(f"Generando código para socket ID: {socket_id}")

#                 page_status = True
#                 await websocket.send(json.dumps(page_status))

#                 driver = initialize_driver()

#                 #enviale la url de la iamgen la cliente para que la carge autumaticamnet

#                 captcha_file = download_captcha_image(driver)
#                 print('Información:',captcha_file)
                
             
#                 await websocket.send(json.dumps({"imageLink": captcha_file}))


#                 # codeNumber = await websocket.recv()
#                 # print(f"Código generado por el cliente: {codeNumber}")

#                 if message == "generateCode":

#                     infoData = await websocket.recv()
#                     print(f"Código generado por el cliente: {infoData}")

#                     document_type = infoData.get('document_type')
#                     identification_number = infoData.get('identification_number')
#                     imageCode = infoData.get('imageCode')

#                     #Imprimir los datos en la consola
#                     print("============Datos recibidos Cliente=================")
#                     print(" ")
#                     print("Tipo de documento:", document_type)
#                     print("Número de identificación:", identification_number)
#                     print("Codigo:", imageCode)

#                     print("=================================================")
#                     print(" ")  

#                     time.sleep(8)

#                     # Seleccionar el elemento <select> por su id
#                     elemento_select = Select(driver.find_element(By.ID, 'tipoDoc'))
#                     elemento_select.select_by_value(document_type)

#                     # Buscar el elemento por su id
#                     elemento_input = driver.find_element(By.ID, 'txtNumDoc')
#                     elemento_input.send_keys(identification_number)

                    
#                     #elemento_input = driver.find_element(By.ID, 'btnConsultar')
#                     time.sleep(8)





#                     #seleccionar_tipo_documento_y_identificacion(driver, infoData)
    




#         driver.quit()

#     except Exception as e:
#         error_response = {
#             "connectionStatus": "error",
#             "errorDescription": str(e)
#         }
#         await websocket.send(json.dumps(error_response))
#         # Eliminar el socket del diccionario en caso de error
#         if websocket in socket_to_id:
#             del socket_to_id[websocket]

# start_server = websockets.serve(handle_client, "localhost", 8765)

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()


async def handle_client(websocket, path):
    try:
        while True:
            message = await websocket.recv()

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



   
   
            #driver.switch_to.window(driver.window_handles[-1])
            switch_to_new_tab(driver)
            information = get_data_table(driver)

            
           

           
        
        
            affiliation_info = get_affiliation_table(driver)

            
            

        
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


            



                    # # Esperar a recibir los datos del cliente
                    # infoData = await websocket.recv()
                    # print(f"Código generado por el cliente: {infoData}")

                    # # Parse JSON data into a dictionary
                    # infoData_dict = json.loads(infoData)

                    # document_type = infoData_dict.get('documentType')  # Use 'documentType' key
                    # identification_number = infoData_dict.get('identificationNumber')  # Use 'identificationNumber' key
                    # imageCode = infoData_dict.get('imageCode')

                    # # Imprimir los datos en la consola
                    # print("============Datos recibidos Cliente=================")
                    # print(" ")
                    # print("Tipo de documento:", document_type)
                    # print("Número de identificación:", identification_number)
                    # print("Codigo:", imageCode)
                    # print("=================================================")
                    # print(" ")  

                    # time.sleep(8)


                # Resto de tu código para manejar los datos recibidos


    except Exception as e:
        # Resto de tu código para manejar excepciones
        print("=================hhhhhhhhh================================",e)

       



start_server = websockets.serve(handle_client, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()