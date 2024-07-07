#  Copyright (c) 2024. #  OCX Consortium https://3docx.org. See the LICENSE

# System import
from typing import Any

# Third party import
from py_rules.condition import Condition




class OcxCondition(Condition):
    def __init__(self,variable: str, operator, value: Any):
        super().__init__(variable, operator, value)
        pass
