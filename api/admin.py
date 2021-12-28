from flask import Blueprint, request, session, render_template
from flask.wrappers import Response
from db import get_products, set_product, remove_product

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
    updated = set_product(id, request.form['name'], request.form['price'], request.form['image'])
    msg, code = "Fail", 400
    if updated:
        msg, code = "Success", 200
    return Response(msg, code)

@admin_blueprint.delete('/products/<id>')
def delte_product(id: int):
    updated = remove_product(id)
    msg, code = "Fail", 400
    if updated:
        msg, code = "Success", 200
    return Response(msg, code)