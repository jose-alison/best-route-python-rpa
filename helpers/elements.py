from enum import Enum

class ButtonsRef(Enum):
    btn_rotas = '//button[@data-value="Rotas"]'
    btn_fechar_rotas = '//button[@aria-label="Fechar rotas"]'

class InputRef(Enum):
    search_bar = 'searchboxinput'
    address_input = '//div[contains(@id, "directions-searchbox")]//input'