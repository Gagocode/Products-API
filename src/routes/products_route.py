from flask import jsonify, Blueprint, request

from service.products_validations import validate_product_payload
from data.schema import DB_PATH
from model.product_model import Product
from repository.products_repository import ProductRepository

post_product_bp = Blueprint("post_product_route", __name__)


@post_product_bp.route('/api/v1/products', methods=['POST'])
def post_product_route():

    payload = request.get_json()

    try:
        validated_payload = validate_product_payload(payload)    
    except ValueError as err:
        return jsonify({
            "code": 400,
            "message": "Validation Error(s)",
            "erros": list(err.args[0])
        })

    product = Product(
        name = validated_payload["name"],
        price = validated_payload["price"],
        quantity = validated_payload["quantity"],
        category = validated_payload["category"]
    )

    errors = []
    product.validate(errors)
    
    if errors:
        return jsonify({
            "code": 400,
            "message": "Validation Error(s)",
            "erros": list(errors)
        })
    
    repo = ProductRepository(DB_PATH)
    repo.create(product)
    
    return jsonify({
        "code": 201,
        "data": "None",
        "message": "Product created."
    })
    

##QUANDO FOR FAZER MAIS ROTAS VOU REPETIR ESSA MESMA VALIDACAO VARIAS VEZES, PRECISA-SE FAZER UMA MANEIRA DE VALIDAR ISSO DE OUTRA FORMA EM OUTRA CAMADA DA APLICACAO