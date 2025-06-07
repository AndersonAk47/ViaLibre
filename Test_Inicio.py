from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

def iniciar_driver():
    
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    

    driver = webdriver.Chrome(options=options)
    return driver

def interactuar_con_pagina(driver):
    try:
        
        driver.get("http://127.0.0.1:5500/Inicio.html#evita")  
        
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "Via"))
        )
        
        

        menu_items = driver.find_elements(By.CSS_SELECTOR, ".menu li a")
        for item in menu_items:
            print(f"Haciendo clic en: {item.text}")
            ActionChains(driver).move_to_element(item).click().perform()
            sleep(1)  
        
        
        
        
        nombre = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Nombre de usuario ']")
        nombre.send_keys(" Estimado Docente")
        sleep(1)
        
        email = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Correo de usuario ']")
        email.send_keys("Docente@Ayuda.com")
        sleep(1)
        
        mensaje = driver.find_element(By.NAME, "Mensaje")
        mensaje.send_keys("Profe  paseme su llave  xD")
        sleep(3)
        
        
        driver.execute_script("arguments[0].scrollIntoView(true);", mensaje)
        sleep(1)
        
        
        enviar = driver.find_element(By.CSS_SELECTOR, "input[value='Enviar ahora']")
        enviar.click()
        sleep(2)
        
        
        
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

def main():
    driver = iniciar_driver()
    try:
        interactuar_con_pagina(driver)
        sleep(5)  
    finally:
        driver.quit()

if __name__ == "__main__":
    main()