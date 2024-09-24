from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from helpers.elements import (ButtonsRef, InputRef)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)
driver.implicitly_wait(2)

driver.get('https://google.com/maps')

def verify_bot_in_page_routes():
    btn_close_route = driver.find_elements(By.XPATH, ButtonsRef.btn_fechar_rotas.value)
    return len(btn_close_route) > 0

def add_address(address, num_box: int = 1):
    try:
        if not verify_bot_in_page_routes():

            find_bar = driver.find_element(By.ID, InputRef.search_bar.value)
            find_bar.clear()
            find_bar.send_keys(address)
            find_bar.send_keys(Keys.RETURN)
        
        else:
            box_addresses = driver.find_elements(By.XPATH, InputRef.address_input.value)

            box_addresses = [x for x in box_addresses if x.is_displayed()]

            if len(box_addresses) >= num_box:
                box_address = box_addresses[num_box-1]
                box_address.clear()
                box_address.send_keys(address)
                box_address.send_keys(Keys.ENTER)
            else:
                print(f"Erro ao adicionar o endereço {len(box_address)}")
    except Exception as e:
        print(e, e.__traceback__)

def open_routes():
    wait = WebDriverWait(driver, timeout=5)

    button_route = wait.until(EC.presence_of_element_located((By.XPATH, ButtonsRef.btn_rotas.value)))
    button_route.click()

    wait = WebDriverWait(driver, timeout=5)
    button_route = wait.until(EC.presence_of_element_located((By.XPATH, ButtonsRef.btn_fechar_rotas.value)))
