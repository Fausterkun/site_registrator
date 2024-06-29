import json
from functools import lru_cache
from abc import ABC, abstractmethod

import requests
from exceptions import CodeRequestError, ResultRequestError, ResultErrorsReturned
from const import SOME_HEADERS, SOME_SEND_CODE_URl, SOME_CHECK_CODE_URL, SOME_REGISTER_URL


class Requester(ABC):
    """Interface for request to cites"""

    @classmethod
    @abstractmethod
    def request_code(cls, email: str):
        """Request code to email"""

    @classmethod
    def _check_response(cls, response):
        """Check response"""
        if not response.status_code == 200:
            raise CodeRequestError(f'Error due send request, status code != 200 {response.status_code}\n{response}')

    @classmethod
    @abstractmethod
    def register_account(cls, account_data: dict):
        """Register account"""

    @classmethod
    @lru_cache
    def _extract_response_data(cls, response: requests.Response):
        """Extract data from response"""
        return response.json()


class SomeRequester(Requester):
    """Requester for some cite"""
    base_headers: dict = SOME_HEADERS
    send_code_url = SOME_SEND_CODE_URl
    check_code_url = SOME_CHECK_CODE_URL
    register_account_url = SOME_REGISTER_URL

    @classmethod
    def request_code(cls, email: str):
        """Request code to some email"""
        email_body = {'email': email}
        body = json.dumps(email_body)
        response = requests.post(cls.send_code_url, data=body)
        cls._check_response(response)

    @classmethod
    def _check_response(cls, response):
        """Check response success"""
        super()._check_response(response)
        if not response.status_code == 200:
            raise CodeRequestError(f'Error due send request, status code != 200 {response.status_code}\n{response}')
        response_data = cls._extract_response_data(response)
        if not response_data.get('result'):
            raise ResultRequestError('Error due send request, status code != 200 {respone.status_code}\n{respone}')
        if 'errors' in response_data and response_data['errors']:
            raise ResultErrorsReturned(f'Site return errors in response {response_data}')

    @classmethod
    def send_check_code(cls, email: str, code: str):
        """Request to check code url"""
        body = {"email": email, "code": code}
        body = json.dumps(body)
        response = requests.post(cls.check_code_url, data=body, headers=cls.base_headers)
        cls._check_response(response)

    @classmethod
    def register_account(cls, account_data: dict):
        """Register account"""
        data = json.dumps(account_data)
        response = requests.post(cls.register_account_url, data=data, headers=cls.base_headers)
        cls._check_response(response)
