class Exchange:
    base_ccy = ''
    ccy = ''
    sale = ''
    buy = ''

    def __init__(self, exchange_data):
        self.base_ccy = exchange_data['base_ccy']
        self.ccy = exchange_data['ccy']
        self.sale = exchange_data['sale']
        self.buy = exchange_data['buy']