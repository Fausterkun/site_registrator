from abc import ABC, abstractmethod
import dataclasses
import datetime
from const import MAIL_RECEIVE_TIMEOUT
from parser import CodeParser, SomeCodeParser
from TempMail import TempMail, Inbox


@dataclasses.dataclass
class MailAgent(ABC):
    """Agent for managing email services"""
    tmp: TempMail
    inb: Inbox
    parser = CodeParser

    @classmethod
    def init(cls):
        """init mail agent"""
        tmp = TempMail()
        inb = TempMail.generateInbox(tmp)
        return cls(tmp=tmp, inb=inb)

    @property
    def email_address(self):
        """Get email address"""
        return self.inb.address

    @abstractmethod
    def _get_email_msg(self):
        """get message from email"""

    def receive_code(self) -> str:
        """Получить код"""
        email_msg = self._get_email_msg()
        code = self.parser.parse(email_msg)
        return code


class SomeMailAgent(MailAgent):
    """Agent for managing email services for some cite"""
    parser: CodeParser = SomeCodeParser
    recive_timeout = MAIL_RECEIVE_TIMEOUT

    def _get_email_msg(self) -> str:
        time_end = datetime.datetime.now() + datetime.timedelta(seconds=self.recive_timeout)
        while datetime.datetime.now() < time_end:
            emails = TempMail.getEmails(self.tmp, inbox=self.inb)
            if emails:
                # TODO: add filter by msg theme
                return emails[0].html
        raise TimeoutError(f'Email msg receive timeout error: {self.recive_timeout} sec. No response')
