from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

def iniciar_driver():
    
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    
    
    driver = webdriver.Chrome(options=options)
    return driver

def llenar_formulario(driver):
    try:
        
        driver.get("http://127.0.0.1:5500/login.html") 
        
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        
        
        nombre = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Nombre']")
        nombre.send_keys("Anderson Romero")
        sleep(2)
        
        
        email = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email']")
        email.send_keys("aromero@inter.edu.co")
        sleep(2)
        
        
        telefono = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Telefono']")
        telefono.send_keys("+5491122334455")
        sleep(2)
        
        
        checkbox = driver.find_element(By.CLASS_NAME, "ipt")
        checkbox.click()
        sleep(2)
        
        
        enviar = driver.find_element(By.CSS_SELECTOR, "input[value='Enviar ahora']")
        enviar.click()
        sleep(2)
        
    
        
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

def main():
    driver = iniciar_driver()
    try:
        llenar_formulario(driver)
        sleep(5)  
    finally:
        driver.quit()

if __name__ == "__main__":
    main()