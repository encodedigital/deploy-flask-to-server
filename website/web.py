from flask import Flask, render_template, request
from os import environ
from dotenv import load_dotenv
from db import *
import socket

app = Flask(__name__)
load_dotenv('../.env')


@app.route("/container")
def container():
    return f"Container ID: {socket.gethostname()}"

@app.route("/")
def home():
    if request.method == 'GET':
        if(request.args.get('stock')):
            selectedStock = request.args.get('stock')
        else:
            selectedStock = 'AAPL'
        stockData = getStockData(selectedStock)
      
    return render_template("home.html", stocks = getStocksName(), stockData = stockData, selectedStock=selectedStock)

def getStocksName():
    stocks = []
    try:
        db = get_db()
        cursor = db.cursor()
        sql = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'stocks' "

        cursor.execute(sql)     
        result = cursor.fetchall()
        
        for name in result:
            stocks.append(name[0].upper())
    except:
        pass
    return stocks

def getStockData(stock):
    json_data=[]
    try:
        db = get_db()
        cursor = db.cursor()
        sql = "SELECT stockDate, open, high, low, close, volume FROM " + stock

        cursor.execute(sql)     
        stockData = cursor.fetchall()
        
        for result in stockData:
            json_data.append({
                'date': result[0].strftime('%Y-%m-%d'),
                'open': result[1],
                'high': result[2],
                'low': result[3],
                'close': result[4],
                'volume': result[5]
            })
    except:
        pass
    return json_data

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=8081)

    