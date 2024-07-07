#  Copyright (c) 2024. #  OCX Consortium https://3docx.org. See the LICENSE

# Third party
from lxml
from py_rules import RuleEngine


class OcxRuleEngine(RuleEngine):
    def __init__(self):
        self
        super().__init__(context={})

    @property
    def context(self):
        return self.__root
