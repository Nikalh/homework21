from typing import Dict

from exceptions import BaseError, NotEnoughSpaceError
from classes.abstract_class import Storage
from classes.request import Request


class Courier:
    def __init__(self, request: Request, storages: Dict[str, Storage]):
        self.__request = request

        self.from_: Storage = storages[self.__request.from_]
        self.to: Storage = storages[self.__request.to]

    def move(self):
        self.from_.remove(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер забирает {self.__request.amount} {self.__request.product} из {self.__request.from_}')

        print(
            f'Курьер везет {self.__request.amount} {self.__request.product} '
            f'со {self.__request.from_} в {self.__request.to}')

        self.to.add(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер доставил {self.__request.amount} {self.__request.product} в {self.__request.to}')


    def cancel(self):

        print('Доставка отменена')

        if self.to.get_free_space() < self.__request.amount:
            self.from_.add(name=self.__request.product, amount=self.__request.amount)
            print(f'Курьер вернул {self.__request.amount} {self.__request.product} в {self.__request.from_}')