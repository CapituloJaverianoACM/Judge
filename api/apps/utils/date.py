from django.utils import timezone
from datetime import datetime


class Date:

    @classmethod
    def datetime_now(cls) -> str:
        """
        Get the datetime now of TIME_ZONE
        :return: datetime
        """
        return timezone.localtime(timezone.now())

    @classmethod
    def format(cls, date, format: str) -> str:
        """
        :param date: date or datetime
        :param format: str
        :return: str
        """
        return datetime.strftime(date, format)
