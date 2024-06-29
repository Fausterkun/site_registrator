from dataclasses import dataclass
from abc import ABC, abstractmethod

from const import DEFAULT_PASSWORD
from data_generator import SomeDataGenerator
from mail_agent import MailAgent, SomeMailAgent
from requester import Requester, SomeRequester


@dataclass
class Registrar(ABC):
    """Cite registrar interface"""
    mail_agent: type[MailAgent]
    requester: Requester

    @abstractmethod
    def register_one(self):
        """One account registration"""


@dataclass
class SomeRegistrar(Registrar):
    """Registrar for some cite"""
    requester = SomeRequester
    data_generator = SomeDataGenerator
    mail_agent = SomeMailAgent

    @classmethod
    def register_one(cls) -> tuple[str, str]:
        """Create one registration"""
        # create temporary email
        mail_agent: MailAgent = cls.mail_agent.init()
        email = mail_agent.email_address
        # request access code
        cls.requester.request_code(email)
        # wait mail with access code and parse it
        code = mail_agent.receive_code()
        # check access code
        cls.requester.send_check_code(email, code)
        # register account
        password = DEFAULT_PASSWORD
        registration_data = cls.data_generator.generate_data(email, code, password)
        cls.requester.register_account(registration_data)
        return email, password
