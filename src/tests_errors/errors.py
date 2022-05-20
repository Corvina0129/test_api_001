from enum import Enum


class ErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code isn't equal expected"
    EMPTY_RESPONSE = "Response is empty"
