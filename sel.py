from selenium import  webdriver
from selenium.webdriver.common.by import By     
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def get_driver(options:list[str]=[]) -> WebDriver:

    opt: webdriver.ChromeOptions= webdriver.ChromeOptions()
    for option in options:
        opt.add_argument(option)

    driver = webdriver.Chrome(options=opt)
    driver.get("http://127.0.0.1:5500/login.html")
    return driver
    

OPTIONS: list[str]=[
    "--disable-extensions",
    "-disable-gpu",
    "start-maximized",
]


def llenar_texto_by_id(driver: WebDriver , id_element: str, texto) -> WebElement:
    element: WebElement = driver.find_element(By.ID , id_element)
    element.send_keys(texto)
    scroll_to_element(drive=driver , elemet=element)
    return 



def  scroll_to_element(drive: WebDriver , elemet: WebElement) -> None:
    drive.execute_script("arguments[0].scrollIntoView();", elemet)
    sleep(1)



def llenar_formulario(driver: WebDriver) -> None:
    campos_texto: dict[str , str] = {
        "nombre": "Anderson",
        
    }
    for key, value in campos_texto.items():
        llenar_texto_by_id(driver=driver, id_element=key , texto=value)
        sleep(1)



def main()-> None:
    driver: WebDriver= get_driver(options=OPTIONS)
    llenar_formulario(driver=driver)
    sleep(10) 
    driver.quit()   


if __name__ == "__main__":
    main()

