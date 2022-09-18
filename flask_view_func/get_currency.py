import requests


def get_currency_exchange_rate_nbu(currency_a: str, currency_b: str, date: str):
    response = requests.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}')
    json = response.json()
    json_rates = json['exchangeRate']

    if response.status_code == 200:
        for i in range(len(json_rates)):
            if json_rates[i].get('baseCurrency') == currency_a and json_rates[i].get('currency') == currency_b:
                rate_buy_NBU = round(json_rates[i].get('saleRateNB'), 2)

                return f'Exchange rate {currency_a} to {currency_b} for {date}: ' \
                       f'\n <b>NBU RATE</b> {rate_buy_NBU}'
        return f'Not found: exchange rate {currency_a} to {currency_b}'
    else:
        return f"Api error {response.status_code}"


def get_currency_exchange_rate_pb(currency_a: str, currency_b: str, date: str):
    response = requests.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}')
    json = response.json()
    json_rates = json['exchangeRate']

    if response.status_code == 200:
        for i in range(len(json_rates)):
            if json_rates[i].get('baseCurrency') == currency_a and json_rates[i].get('currency') == currency_b:
                rate_buy_PB = round(json_rates[i].get('saleRate'), 2)
                rate_sell_PB = round(json_rates[i].get('purchaseRate'), 2)

                return f'Exchange rate {currency_a} to {currency_b} for {date}: ' \
                       f'\n <b>PRIVATE RATE</b> BUY - {rate_buy_PB} | SELL - {rate_sell_PB}'
        return f'Not found: exchange rate {currency_a} to {currency_b}'
    else:
        return f"Api error {response.status_code}"


# print(get_currency_exchange_rate_nbu('UAH', 'USD', '01.08.2022'))
# print(get_currency_exchange_rate_pb('UAH', 'USD', '01.08.2022'))
