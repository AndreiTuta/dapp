from flask import Blueprint, request, session, render_template
from repository import add_order_data, get_orders


orders_blueprint=Blueprint("orders", __name__)


@orders_blueprint.post('/')
def add_order():
    result = 'OK'
    try:
        wallet_address = request.form.get('wallet_address')
        tx = request.form.get('tx')
        name = request.form.get('name')
        invoice_id = request.form.get('invoice_id')
        o = add_order_data(wallet_address, tx, name, invoice_id)
        if not o:
            result = 'FAIL'
    except Exception as ex:
        print('Exception while adding order ' + ex)
        result = 'FAIL'
    finally:
        return result


@orders_blueprint.get('/')
def orders():
    user_orders = get_orders(session['wallet_address'])
    return render_template('orders.html', orders=user_orders)