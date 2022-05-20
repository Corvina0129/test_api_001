import requests

from config import URL
from src.pydantic_models.pydantic_models import SimpleJsonBaseModel
from src.models.models import Response


def test_api():
    """
    parses the response into an instance of the Response class,
    checks the status code, checks for data in response and validates the data
    """
    req = requests.get(URL)
    response = Response(req)
    response.assert_status_code(200)
    response.assert_for_emptiness()
    response.validate_json_schema(SimpleJsonBaseModel)
