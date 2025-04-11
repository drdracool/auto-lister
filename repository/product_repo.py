import sqlite3
from model.product import Product
import datetime


class Product_Repo:
    def __init__(self, path: str):
        self.DB_PATH: str = path
        self.initialize()

    def initialize(self):
        query = """
        CREATE TABLE IF NOT EXISTS product (
          id INTEGER PRIMARY KEY,
          foreign_id INTEGER UNIQUE NOT NULL,
          name TEXT NOT NULL,
          url TEXT NOT NULL,
          regular_price INTEGER NOT NULL,
          selling_price INTEGER NOT NULL,
          discount_amount INTEGER NOT NULL,
          discount_percentage REAL NOT NULL,
          image_url TEXT NOT NULL,
          description TEXT NOT NULL,
          stock INTEGER NOT NULL,
          additional_image_urls TEXT,
          publish_status INTEGER NOT NULL,
          short_name TEXT NOT NULL,
          short_description TEXT NOT NULL,
          modified_date TIMESTAMP
        )
      """

        try:
            with sqlite3.connect(self.DB_PATH) as conn:
                print(
                    f"Opened SQLite database with version {sqlite3.sqlite_version} successfully."
                )
                cursor = conn.cursor()
                cursor.execute(query)
                conn.commit()
                print("Table created successfully or table already existed.")

        except sqlite3.OperationalError as e:
            print("Failed to open database:", e)

    def insert_product(
        self,
        product: Product,
    ):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO product (foreign_id, name, url, regular_price, selling_price, discount_amount, 
                                      discount_percentage, image_url, description, stock, additional_image_urls, publish_status, short_name, short_description, modified_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    product.foreign_id,
                    product.name,
                    product.url,
                    product.regular_price,
                    product.selling_price,
                    product.discount_amount,
                    product.discount_percentage,
                    product.image_url,
                    product.description,
                    product.stock,
                    product.additional_image_urls,
                    product.publish_status,
                    product.short_name,
                    product.short_description,
                    datetime.datetime.now(),
                ),
            )
            print(f"Product {product.short_name} has been successfully inserted!")

    def get_product_by_foreign_id(self, id: int) -> Product:
        with sqlite3.connect(self.DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            row: sqlite3.Row = cursor.execute(
                "SELECT * FROM product WHERE foreign_id=?", (id,)
            ).fetchone()
            product: Product = Product(*row)
            print(f"Product with foreign_id {product.foreign_id} fetched.")
            return product
