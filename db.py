import re
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


def get_connection():
    path = './dapp.sqlite3'
    connection = sqlite3.connect(path)
    return connection


def get_products():
    records = None
    conn = get_connection()
    sql = 'SELECT * from products'
    cursor = conn.cursor()
    cursor.execute(sql)
    records = cursor.fetchall()
    products = []
    for record in records:
        products.append({
            'id': records.index(record) + 1,
            'name': record[0],
            'price': record[1],
            'image': record[2]
        })
    return products


def add_order_data(wallet_address, tx, name, invoice_id):
    result = True
    try:
        conn = get_connection()
        sql = 'INSERT INTO orders(wallet_address,tx,product_name,invoice_id) VALUES (?,?,?,?)'
        cursor = conn.cursor()
        cursor.execute(sql, (wallet_address, tx, name, invoice_id))
        conn.commit()
        conn.close()
    except Exception as ex:
        print('Exception in add_order function in db:- ' + ex)
        result = False
    finally:
        return result


def get_orders(wallet_address):
    records = None
    conn = get_connection()
    sql = 'SELECT * from orders where wallet_address = ?'
    cursor = conn.cursor()
    cursor.execute(sql, (wallet_address,))
    records = cursor.fetchall()
    return records
