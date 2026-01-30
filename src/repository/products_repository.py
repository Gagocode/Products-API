import sqlite3 as sq

class ProductRepository:

    def __init__(self, DB_PATH):
        self.DB_PATH = DB_PATH

    def find_all(self):
        with sq.connect(self.DB_PATH) as CONNECT:
                CONNECT.row_factory = sq.Row
                CURSOR = CONNECT.cursor()
                CURSOR.execute(
                        '''
                                SELECT * FROM PRODUCTS;
                        '''    
                )
                return CURSOR.fetchall()

    def find_active(self, status):
         with sq.connect(self.DB_PATH) as CONNECT:
                CONNECT.row_factory = sq.Row
                CURSOR = CONNECT.cursor()
                CURSOR.execute(
                        '''
                                SELECT * FROM PRODUCTS
                                WHERE ACTIVE = ?
                        ''',(status,)    
                )
                return CURSOR.fetchall()
         
    def find_by_id(self, product_id):
        with sq.connect(self.DB_PATH) as CONNECT:
                CONNECT.row_factory = sq.Row
                CURSOR = CONNECT.cursor()
                CURSOR.execute(
                        '''
                                SELECT * FROM PRODUCTS
                                WHERE PRODUCT_ID = ? 
                        ''',(product_id,)    
                )
                return CURSOR.fetchall()
        
    def create(self, product):
        with sq.connect(self.DB_PATH) as CONNECT:
                CURSOR = CONNECT.cursor()
                CURSOR.execute(
                        '''
                                INSERT INTO PRODUCTS 
                                (
                                        NAME,
                                        PRICE,
                                        QUANTITY,
                                        CATEGORY,
                                        ACTIVE
                                )
                                VALUES
                                (
                                        ?,
                                        ?,
                                        ?,
                                        ?,
                                        ?
                                )
                        ''', (product.name, product.price, product.quantity, product.category, product.active)
                )

    
    def update(self, product_id, product):
        with sq.connect(self.DB_PATH) as CONNECT:
                CURSOR = CONNECT.cursor()
                CURSOR.execute(
                        '''
                                UPDATES PRODUCTS SET 
                                        NAME = ?,
                                        PRICE = ?,
                                        QUANTITY = ?,
                                        CATEGORY = ?,
                                        ACTIVE = ?
                                WHERE PRODUCT_ID = ?
                        ''',(product.name, product.price, product.quantity, product.category, product.active, product_id) 
                )

    def deactivate(self, product_id):
        with sq.connect(self.DB_PATH) as CONNECT:
                CURSOR = CONNECT.cursor()
                CURSOR.execute(
                        '''
                                UPDATE PRODUCT SET
                                        ACTIVE = "false"
                                WHERE PRODUCT_ID = ?
                        ''', (product_id,)
                )