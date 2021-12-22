import pymysql
from flask import g
from os import environ

def get_db():
    if 'db' not in g:      

        if(environ.get('ENV') == 'LOCAL'):
            g.db = pymysql.connect(host=environ.get('DB_HOST'), 
                port=int(environ.get('DB_PORT')), 
                user=environ.get('DB_USER'), 
                passwd=environ.get('DB_PASSWORD'), 
                db=environ.get('DB_SCHEMA'))
        elif(environ.get('ENV') == 'DOCKER'):
            g.db = pymysql.connect(host=environ.get('DB_HOST'), 
                port=int(environ.get('DB_PORT')), 
                user=environ.get('DB_USER'), 
                passwd=environ.get('DB_PASSWORD'), 
                db=environ.get('DB_SCHEMA'),
                ssl_ca='/mysqlData/ca.pem',
                ssl_key='/mysqlData/client-key.pem',
                ssl_cert='/mysqlData/client-cert.pem')

    return g.db