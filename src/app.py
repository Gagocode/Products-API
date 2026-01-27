from flask import Flask
from flask_cors import CORS
from data.schema import init_database

from routes.products_route import post_product_bp

app = Flask(__name__)
CORS(app)

#CONFIGS
DEBUG_MODE = True
app.config['JSON_SORT_KEYS'] = False

#BLUEPRINT IMPORTS
app.register_blueprint(post_product_bp)

#INIT
if __name__ == '__main__':
    init_database()
    app.run(debug=DEBUG_MODE)


