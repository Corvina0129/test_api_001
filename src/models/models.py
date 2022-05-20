from src.tests_errors.errors import ErrorMessages


class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def assert_for_emptiness(self):
        assert len(self.response_json) > 0, ErrorMessages.EMPTY_RESPONSE

    def assert_status_code(self, status_code):
        assert self.response_status == status_code, \
            ErrorMessages.WRONG_STATUS_CODE.value

    def validate_json_schema(self, pydantic_model):
        """iterates over each json object and parses it to pydantic model"""
        for item in self.response_json:
            pydantic_model.parse_obj(item)
