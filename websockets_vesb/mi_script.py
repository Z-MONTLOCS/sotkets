
# Importaciones locales
from .config_utils import (
    initialize_driver,
    seleccionar_tipo_documento_y_identificacion,
    switch_to_new_tab,
    get_data_table,
    close_browser,
    get_affiliation_table,
    extract_names,
    close_driver,
    click_send,download_captcha_image

)



def ejecutar_mi_script(datos):
    
    driver = initialize_driver()
   
    seleccionar_tipo_documento_y_identificacion(driver, datos)


    captcha_file = download_captcha_image(driver)
    print('Información:',captcha_file)




    


 
    click_send(driver)

    close_driver(driver)
    

  
    driver.switch_to.window(driver.window_handles[-1])


   
   

    #switch_to_new_tab(driver)
    information = get_data_table(driver)


    affiliation_info = get_affiliation_table(driver)


  
    names_surnames_info = extract_names( information['NOMBRES'], information['APELLIDOS'])


   # Create the info dictionary with the assigned values
    info = {
    'first_name': names_surnames_info['first_name'],
    'middle_name': names_surnames_info['middle_name'],
    'last_name': names_surnames_info['first_surname'],
    'second_last_name': names_surnames_info['second_surname'],
    'eps': affiliation_info['EPS'] 
}


    # Mostrar los resultados
    print('Información:')
    print('Primer nombre:', info['first_name'])
    print('Segundo nombre:', info['middle_name'])
    print('Primer apellido:', info['last_name'])
    print('Segundo apellido:', info['second_last_name'])
    print('EPS:', info['eps'])   



    return info
