#Technology Imports
from flask import jsonify, Blueprint, request

#Depency Imports
from services.repository_service import create_product_service, list_product_service, get_product_or_404_service
from services.product_route_service import validate_route_payload
from exceptions.product_exceptions import ProductNotFoundError


post_product_bp = Blueprint("post_product_route", __name__)
get_products_all_bp = Blueprint("get_products_all", __name__)
get_product_id_bp = Blueprint("get_products_id", __name__)
get_products_active_bp = Blueprint("get_products_active", __name__)

@post_product_bp.route('/api/v1/products', methods=['POST'])
def post_product_route():

    payload = request.get_json()
    product = validate_route_payload(payload)
    
    create_product_service(product)
    
    return jsonify({
        "code": 201,
        "data": "None",
        "message": "Product created."
    }),201
    
@get_products_all_bp.route("/api/v1/products", methods=['GET'])
def get_products_all():
    
    query_params = request.args.get("active")
    products_list = list_product_service(query_params)

    return jsonify({
        "code": 200,
        "description": "returning all products from database",
        "data":[{
            "id": product["product_id"],
            "name": product["name"],
            "price": product["price"],
            "quantity": product["quantity"],
            "category": product["category"],
            "active": product["active"]
        } for product in products_list]
    }),200

@get_product_id_bp.route(f"/api/v1/products/<product_id>", methods=['GET'])
def get_products_id(product_id):

    try:
        product = get_product_or_404_service(product_id)
    except ProductNotFoundError:
        return jsonify({
        "code": 404,
        "description": f"the product with {product_id} id is not found.",
        }),404

    return jsonify({
        "code": 200,
        "description": f"returning product with {product_id} id.",
        "data":[{
            "id": product["product_id"],
            "name": product["name"],
            "price": product["price"],
            "quantity": product["quantity"],
            "category": product["category"],
            "active": product["active"]
        }for product in product]
    }),200

