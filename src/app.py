#Technology Imports
from flask import Flask
from flask_cors import CORS

#Depencies imports
from data.schema import init_database

#blueprint imports
from routes.products_route import post_product_bp, get_products_all_bp, get_product_id_bp, get_products_active_bp, deactivate_product_bp

app = Flask(__name__)
CORS(app)

#CONFIGS
DEBUG_MODE = True
app.config['JSON_SORT_KEYS'] = False

#BLUEPRINT IMPORTS
app.register_blueprint(post_product_bp)
app.register_blueprint(get_products_all_bp)
app.register_blueprint(get_product_id_bp)
app.register_blueprint(get_products_active_bp)
app.register_blueprint(deactivate_product_bp)

#INIT
if __name__ == '__main__':
    init_database()
    app.run(debug=DEBUG_MODE)


