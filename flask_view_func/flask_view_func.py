from flask import Flask, request
from datetime import datetime
from get_currency import get_currency_exchange_rate_nbu
from get_currency import get_currency_exchange_rate_pb

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p><b>WOW, it's work</b></p>"


@app.route("/rates", methods=['GET'])
def get_rates():
    today = datetime.now().strftime('%d.%m.%Y')

    currency_a = request.args.get('currency_a', default='USD')
    currency_b = request.args.get('currency_b', default='UAH')
    date = request.args.get('date', default=today)
    rate_type = request.args.get('type', default='nbu')

    if rate_type == 'nbu':
        result = get_currency_exchange_rate_nbu(currency_a, currency_b, date)
    else:
        result = get_currency_exchange_rate_pb(currency_a, currency_b, date)

    return result


if __name__ == '__main__':
    app.run(debug=True)