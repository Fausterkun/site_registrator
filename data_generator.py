import copy
import random
from abc import ABC, abstractmethod

from faker import Faker
from utils import merge_dicts
from const import SOME_DATA_TEMPLATE, DEFAULT_PASSWORD, DATA_GENERATION_LOCALE

fake = Faker(DATA_GENERATION_LOCALE)


class DataGenerator(ABC):
    """Generate data for registration"""

    @classmethod
    @abstractmethod
    def generate_data(cls, email: str, code: int) -> dict:
        """Generate account data"""


class SomeDataGenerator(DataGenerator):
    """Some cite data generator"""

    @classmethod
    def generate_data(cls, email: str, code: str, password: str | None = None) -> dict:
        """Generate request data for registration"""
        template = copy.deepcopy(SOME_DATA_TEMPLATE)
        cls.__add_request_data(template, email, code)
        user_register = cls.generate_account_data(password)
        return merge_dicts(template, user_register)

    @classmethod
    def __add_request_data(cls, template: dict, email: str, code: str):
        """Add non-personal data in request"""
        template['email'] = email
        template['code'] = code

    @classmethod
    def generate_account_data(cls, password: str | None = DEFAULT_PASSWORD) -> dict:
        """Generate account data"""
        raise NotImplemented('Redefine your account data generator')
        # first_name = fake.first_name()
        # last_name = fake.last_name()
        # middle_name = fake.middle_name()
        # phone_number = fake.phone_number()
        # birthday = str(fake.date_of_birth(minimum_age=13, maximum_age=31))
        # return {
        #         'name': {
        #             'first_name': first_name,
        #             'last_name': last_name,
        #             'middle_name': middle_name
        #         },
        #         'phone': phone_number,
        #         'birth_date': birthday,
        #         'password': password
        #     }
        # }
