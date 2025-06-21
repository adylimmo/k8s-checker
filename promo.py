# service_b/app.py
from flask import Flask

app = Flask(__name__)

@app.route('/promo')
def promo():
    return {'message': 'Diskon 50% untuk produk Baju'}

if __name__ == '__main__':
    app.run(port=5001, debug=True)
