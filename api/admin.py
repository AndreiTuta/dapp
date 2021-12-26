from flask import Blueprint, request, session, render_template
from flask.wrappers import Response
from repository import add_order_data, get_orders, get_products

ADMIN = '0x3AB21F324B5c61429A933d19547b7480D445b795'

admin_blueprint=Blueprint("admin", __name__)

@admin_blueprint.get('/')
def admin():
    wallet_address = None
    try: 
        wallet_address = session['wallet_address']
    except KeyError:
        pass
    if(wallet_address is not None and wallet_address != ADMIN):
        products = get_products()
        return render_template('admin-prod.html', products=products)
    else:
        return Response('Not available', 404)

@admin_blueprint.post('/products/<id>')
def edit_product(id: int):
    print(id)
    print(request.form['name'])
    print(request.form['price'])
    print(request.form['image'])
    return "Hello"