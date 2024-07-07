#  Copyright (c) 2024. #  OCX Consortium https://3docx.org. See the LICENSE

from typing import Any
from abc import ABC, abstractmethod


# Rules interface
class IRule(ABC):

    def __init__(self, id:str, name: str, description: str):
        self._id = id
        self._name = name
        self._description = description

    @abstractmethod
    def validate(self, data: Any ) -> bool:
        pass
