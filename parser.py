from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from exceptions import ConfirmationCodeParseError


class CodeParser(ABC):
    """Response code parser"""

    @classmethod
    @abstractmethod
    def parse(cls, raw_body: str) -> str:
        """Parse msg body and return code"""


class SomeCodeParser(CodeParser):
    """Code parser for some cite"""

    @classmethod
    def parse(cls, html_content: str) -> str:
        """Parse code from html content"""
        raise NotImplemented("Redefine your site parser")
        # soup = BeautifulSoup(html_content, 'html.parser')
        # confirmation_code_element = soup.find()
        # if not confirmation_code_element:
        #     raise ConfirmationCodeParseError(f'Error due parse html msg code.\nHtml: {html_content}')
        # confirmation_code = confirmation_code_element.get_text(strip=True)
        # return confirmation_code
