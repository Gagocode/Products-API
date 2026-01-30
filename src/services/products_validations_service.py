import re

def validate_product_payload(payload: dict):

    MAX_NAME_LENGHT = 100   #NAME
    MIN_PRICE_VALUE = 0     #PRICE
    MAX_QUANTITY = 999      #QUANTITY
    MAX_CATEGORY_LENGHT = 100 #CATEGORY

    errors = []

    #Required fields in payload
    if "name" not in payload:
        errors.append("Field 'name' is required.")
    if "price" not in payload:
        errors.append("Field 'price' is required.")
    if "quantity" not in payload:
        errors.append("Field 'quantity' is required.")
    if "category" not in payload:
        errors.append("Field 'category' is required.")

    if errors:
        raise ValueError(errors)
    
    #validate fields (name)
    name = payload["name"]  
    if not isinstance(name, str):
        errors.append("Field 'name' must be a string.")
    else:
        if not re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ ]+", name):
            errors.append("Field 'name' can only contain letters and spaces.")
        payload["name"] = name.strip().title() 


    #valid fields (price)
    price = payload["price"]
    try:
        price = float(price)
    except (ValueError, TypeError):
        errors.append("Field 'price' need be a valid price.") 
    else: 
        payload["price"] = price
       

    #vald fields (quantity)
    quantity = payload["quantity"]
    try:
        quantity = int(quantity)
    except (ValueError, TypeError):
        errors.append("Field 'quantity' need be a valid quantity.")
    else:
        payload["quantity"] = quantity
        

    #valid field(category)   
    category = payload["category"]  
    if not isinstance(category, str):
        errors.append("Field 'category' must be a string.")
    else:
        if not re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ ]+", category):
            errors.append("Field 'category' can only contain letters and spaces.")
        
        payload["category"] = category.strip().title() 


    if errors:
        raise ValueError(errors)
    
    return payload
    