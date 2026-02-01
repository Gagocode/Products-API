from repository.products_repository import ProductRepository
from exceptions.product_exceptions import ProductNotFoundError
from data.schema import DB_PATH

def create_product_service(product):
    repo = ProductRepository(DB_PATH)
    repo.create(product)

def get_product_or_404_service(id):
    repo = ProductRepository(DB_PATH)
    product = repo.find_by_id(id)

    if not product:
        raise ProductNotFoundError()
    
    return product
    
def list_product_service(active_params: bool | None):
    
    repo = ProductRepository(DB_PATH)
    
    active = None
    if active_params is not None:
        active = active_params.lower() == "true"
        products_list = repo.find_active(active)
    else:
        products_list = repo.find_all()

    return products_list

       