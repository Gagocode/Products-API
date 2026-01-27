class Product:

    MAX_NAME_LENGHT = 100   #NAME
    MIN_PRICE_VALUE = 0     #PRICE
    MAX_QUANTITY = 999      #QUANTITY
    MAX_CATEGORY_LENGHT = 100 #CATEGORY


    def __init__(self, name: str, price: float, quantity: int, category: str):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.active = True

    def validate(self, errors: list):

        if not len(self.name) < self.MAX_NAME_LENGHT:
            errors.append("Field 'name' needs under 100 characters") 

        if self.price < self.MIN_PRICE_VALUE:
            errors.append(f"Field 'price' need be above {self.MIN_PRICE_VALUE}.")

        if self.quantity > self.MAX_QUANTITY: 
            errors.append(f"Field 'quantity' needs be above {self.MAX_QUANTITY}.")

        if not len(self.category) < self.MAX_CATEGORY_LENGHT:
            errors.append("Field 'category' needs under 100 characters")