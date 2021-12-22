from os import environ
from flask import Flask, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
from db import *
import socket

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False #Prevent flask to sort json data and keep order as specified

limiter = Limiter(app, key_func=get_remote_address, storage_uri="redis://redis:6379")

load_dotenv('../.env')


@app.route('/')
def home():
    return jsonify({'Container ID': socket.gethostname()}), 200

@app.route('/<stock>')
@limiter.limit("5/minute")
def stockData(stock):
    
    if(stock.isalpha()):
        try:
            db = get_db()
            cursor = db.cursor()
            sql = "SELECT stockDate, open, high, low, close, volume FROM "+ stock
        
            cursor.execute(sql)     
            stockData = cursor.fetchall()
            
            json_data=[]
            for result in stockData:
                json_data.append({
                    'date': result[0].strftime('%Y-%m-%d'),
                    'open': result[1],
                    'high': result[2],
                    'low': result[3],
                    'close': result[4],
                    'volume': result[5]
                })
            return jsonify(json_data), 200
        except:
            return jsonify({'data': 'Record Not Found'}), 422
    else:
        return jsonify({'data': 'Record Not Found'}), 422

@app.errorhandler(429)
def ratelimit_handler(e):
    return "You have exceeded your rate-limit"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    