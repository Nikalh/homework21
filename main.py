from typing import Dict

from classes.abstract_class import Storage
from classes.courier import Courier
from exceptions import BaseError
from classes.request import Request
from classes.shop import Shop
from classes.store import Store

store = Store(
    items={
        "печеньки": 3,
        "собачки": 2,
        "коробки": 5,
        "карандаши": 15,
    },
    capacity=100,
)

shop = Shop(items={
    "печеньки": 5,

}, capacity=20,
    max_unique_items=5
)

storages: Dict[str, Storage] = {
    'склад': store,
    'магазин': shop,
}


def main():
    print("Добрый день!\n")
    # Выводим содержимое склада
    while True:
        for storage_name, storage in storages.items():
            print(f' В {storage_name} хранится:\n{storage.get_items()}')
        # Просим пользователя ввести строку
        raw_request: str = input(
            'Введите запрос в формате "Доставить 3 печеньки из склад в магазин"\n'
            'Введите "stop" или "стоп", чтобы закончить:'

        )
        if raw_request in ('stop', 'стоп'):
            break

        # Обрабатываем заказ
        try:
            request = Request(request=raw_request, storages=storages)
        except BaseError as e:
            print(e.message)
            continue

        # Доставляем товар
        courier = Courier(request=request, storages=storages)
        try:
            courier.move()
        except BaseError as e:
            print(e.message)
            courier.cancel()


if __name__ == '__main__':
    main()
