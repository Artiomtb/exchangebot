import requests
import json

from models import Exchange


class PrivatBankExchangeService:
    URL = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'

    @staticmethod
    def _load_current_exchanges():
        return json.loads(requests.get(PrivatBankExchangeService.URL).text)

    @staticmethod
    def get_current_exchanges():
        return [Exchange(exchange_data) for exchange_data in PrivatBankExchangeService._load_current_exchanges()]

    @staticmethod
    def get_current_exchange(ccy):
        ccy = ccy.upper()
        try:
            exchange = next(
                Exchange(exchange_data) for exchange_data in PrivatBankExchangeService._load_current_exchanges() if
                exchange_data['ccy'] == ccy)
        except StopIteration:
            exchange = None

        return exchange
