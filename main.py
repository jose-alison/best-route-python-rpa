from time import sleep
from src.add_route import (add_address, open_routes)

if __name__ == "__main__":
    enderecos = [
        'Rua 1',
        'Rua 2',
        ]
    add_address(enderecos[0], num_box=1)
    open_routes()
    add_address(enderecos[0], num_box=1)
    sleep(2)
    add_address(enderecos[1], num_box=2)

    sleep(10)