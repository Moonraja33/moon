from flask import Flask, render_template

# ایپ بنانا
app = Flask(__name__)

# سمبلز کی لسٹ (Dropdown میں دکھانے کے لیے)
symbols = [
    "BTCUSD",
    "ETHUSD",
    "EURUSD",
    "GBPUSD",
    "AAPL",
    "TSLA"
]

# ڈیش بورڈ روٹ
@app.route('/')
def dashboard():
    return render_template('dashboard.html', symbols=symbols)

# مین فنکشن
if __name__ == '__main__':
    app.run(debug=True)
