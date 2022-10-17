from abc import ABC, abstractmethod


class Storage(ABC):

    @abstractmethod
    def add(self, name, amount):
        pass

    @abstractmethod
    def remove(self, name, amount: int):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass

#
# print(f'{store.add(req.product, req.amount)}')
# print(f'Курьер забирает {req.amount} {req.product} из {req.from_}')
# print(f'{store.remove(req.product, req.amount)}')
# print(f'Курьер везет {req.amount} {req.product} со {req.from_} в {req.to}')
# print(f'{shop.add(req.product, req.amount)}')
# print(f'Курьер доставил {req.amount} {req.product} в {req.to}')
# print(store.get_unique_items_count())
