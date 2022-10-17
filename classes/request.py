from typing import Dict, List

from classes.abstract_class import Storage
from exceptions import InvalidRequestError, UnknownStorageError


class Request:
    def __init__(self, request: str, storages: Dict[str, Storage]):
        split_request: List[str] = request.strip().lower().split(' ')
        # Выводим ошибку если запрос не верный
        if len(split_request) !=7:
            raise InvalidRequestError

        self.amount = int(split_request[1])
        self.product = split_request[2]
        self.from_ = split_request[4]
        self.to = split_request[6]

        #Выводим ошибку если не известно место назначения или отправления
        if self.from_ not in storages or self.to not in storages:
            raise UnknownStorageError