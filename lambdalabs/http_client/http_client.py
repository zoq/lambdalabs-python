import requests
import json

from lambdalabs.exceptions import APIException
from lambdalabs.__version__ import VERSION


def handle_error(response: requests.Response) -> None:
    """checks for the response status code and raises an exception if it's 400 or higher.

    :param response: the API call response
    :raises APIException: an api exception with message and error type code
    """
    if not response.ok:
        data = json.loads(response.text)
        code = data['code'] if 'code' in data else None
        message = data['message'] if 'message' in data else None
        raise APIException(code, message)


class HTTPClient:
    """An http client, a wrapper for the requests library.

    For each request, it adds the authentication header with an access token.
    If the access token is expired it refreshes it before calling the specified API endpoint.
    Also checks the response status code and raises an exception if needed.
    """

    def __init__(self, api_key, base_url: str) -> None:
        """The Lambda Labs client

        :param api_key: API key
        :type api_key: str
        :param base_url: base url for all the endpoints, optional, defaults to "https://cloud.lambdalabs.com/api/v1/"
        :type base_url: str, optional
        """

        self._version = VERSION
        self._api_key = api_key
        self._base_url = base_url

    def post(self, url: str, json: dict = None, params: dict = None, **kwargs) -> requests.Response:
        """Sends a POST request.

        A wrapper for the requests.post method.

        :param url: relative url of the API endpoint
        :type url: str
        :param json: A JSON serializable Python object to send in the body of the Request, defaults to None
        :type json: dict, optional
        :param params: Dictionary of querystring data to attach to the Request, defaults to None
        :type params: dict, optional

        :raises APIException: an api exception with message and error type code

        :return: Response object
        :rtype: requests.Response
        """

        url = self._add_base_url(url)
        headers = self._generate_headers()

        response = requests.post(url, json=json, headers=headers, params=params, **kwargs)
        handle_error(response)

        return response

    def get(self, url: str, params: dict = None, **kwargs) -> requests.Response:
        """Sends a GET request.

        A wrapper for the requests.get method.

        :param url: relative url of the API endpoint
        :type url: str
        :param params: Dictionary of querystring data to attach to the Request, defaults to None
        :type params: dict, optional

        :raises APIException: an api exception with message and error type code

        :return: Response object
        :rtype: requests.Response
        """
        headers = self._generate_headers()
        url = self._add_base_url(url)

        response = requests.get(url, headers=headers)
        handle_error(response)

        return response

    def delete(self, url: str, json: dict = None, params: dict = None, **kwargs) -> requests.Response:
        """Sends a DELETE request.

        A wrapper for the requests.delete method.

        :param url: relative url of the API endpoint
        :type url: str
        :param json: A JSON serializable Python object to send in the body of the Request, defaults to None
        :type json: dict, optional
        :param params: Dictionary of querystring data to attach to the Request, defaults to None
        :type params: dict, optional

        :raises APIException: an api exception with message and error type code

        :return: Response object
        :rtype: requests.Response
        """
        headers = self._generate_headers()
        url = self._add_base_url(url)

        response = requests.delete(url, headers=headers, json=json, params=params, **kwargs)
        handle_error(response)

        return response

    def _generate_headers(self) -> dict:
        """Generate the default headers for every request

        :return: dict with request headers
        :rtype: dict
        """
        headers = {
            'User-Agent': self._generate_user_agent(),
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {self._api_key}"
        }
        return headers

    def _generate_user_agent(self) -> str:
        """Generate the user agent string.

        :return: user agent string
        :rtype: str
        """

        return f'lambdalabs-python-v{self._version}'

    def _add_base_url(self, url: str) -> str:
        """Adds the base url to the relative url

        :param url: a relative url path
        :type url: str
        :return: the full url path
        :rtype: str
        """
        return self._base_url + url
