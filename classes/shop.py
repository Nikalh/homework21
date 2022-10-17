from classes.base_storage import BaseStorage
from exceptions import TooManyDifferentProductError


class Shop(BaseStorage):
    def __init__(self, items, capacity, max_unique_items):
        self.max_unique_items = max_unique_items
        super().__init__(items, capacity)

    def add(self, name, amount: int) -> None:
        if self.get_unique_items_count() >= self.max_unique_items:
            raise TooManyDifferentProductError
        super().add(name, amount)
