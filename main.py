import json

from flask import Flask, render_template, request, url_for, redirect, flash, session
from db import get_products
from api.orders import orders_blueprint
from api.admin import admin_blueprint
import argparse

app = Flask(__name__)
app.config['SECRET_KEY'] = 'not_s0_secr3t'

parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

@app.route('/')
def index():
    products = get_products()
    return render_template('home.html', products=products)

@app.route('/logout')
def logout():
    session['wallet_address'] = None
    return redirect('/')

@app.post('/set_wallet/<wallet_address>')
def set_wallet_session(wallet_address):
    session['wallet_address'] = wallet_address
    return 'OK'


if __name__ == '__main__':
    parser.add_argument('merchant')

    app.register_blueprint(orders_blueprint, url_prefix='/orders')
    app.register_blueprint(admin_blueprint, url_prefix="/admin")

    app.run(debug=True)

