import datetime as dt
from typing import List
from uuid import uuid4

from pyqiwi import Wallet
from pyqiwi.types import Transaction


class QiwiWallet(Wallet):

    def __init__(self, token):
        super().__init__(token=token)
        self.nickname = self.profile.raw['contractInfo']['nickname']['nickname']

    def get_transactions(self, days: int = 0, hours: int = 0, minutes: int = 0, **kwargs) -> List[Transaction]:
        """
        Возвращает список транзанкций(максимум 50)
        """
        start_date = dt.datetime.utcnow() - dt.timedelta(days=days, hours=hours, minutes=minutes)
        transactions = self.history(**kwargs, rows=50, start_date=start_date, end_date=dt.datetime.utcnow()).get(
            'transactions', [])
        return transactions

    @staticmethod
    def generate_comment() -> str:
        """
        Генерирует рандомную строку из 32 символом и возвращает ее срез
        """
        uuid: str = str(uuid4())
        comment: str = ''.join(uuid.split('-'))

        return comment[:8]
