# service_a/app.py
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/sales')
def sales():
    # Memanggil service B
    response = requests.get('http://localhost:5001/promo')
    promo_data = response.json()

    return {
        'sales_message': 'Penjualan produk A sedang berlangsung',
        'promo': promo_data['message']
    }

if __name__ == '__main__':
    app.run(port=5000, debug=True)
