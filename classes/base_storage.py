from classes.abstract_class import Storage
from exceptions import NotEnoughSpaceError, NotEnoughProductError, UnknownProductError


class BaseStorage(Storage):
    def __init__(self, items, capacity):
        self.__items = items
        self.__capacity = capacity

    def add(self, name,amount) -> None:
        if self.get_free_space() < amount:
            raise NotEnoughSpaceError

        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount

    def remove(self, name, amount) -> None:

        if name not in self.__items:
            raise UnknownProductError

        if self.__items[name] < amount:
            raise NotEnoughProductError

        self.__items[name] -= amount
        if self.__items[name] == 0:
            self.__items.pop(name)


    def get_free_space(self):
        return self.__capacity - sum(self.__items.values())


    def get_items(self):
        return self.__items


    def get_unique_items_count(self):
        return len(self.__items)
