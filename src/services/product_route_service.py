#Technology Imports
from flask import jsonify

#Dependencies Imports
from services.products_validations_service import validate_product_payload
from model.product_model import Product

def validate_route_payload(payload):

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
    
    return product