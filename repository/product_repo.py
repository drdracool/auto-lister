import sqlite3


class Product_Repo:
    def __init__(self, path):
        self.initialize(path)

    def initialize(self, path):
        try:
            with sqlite3.connect(path) as conn:
                print(
                    f"Opened SQLite database with version {sqlite3.sqlite_version} successfully."
                )

        except sqlite3.OperationalError as e:
            print("Failed to open database:", e)
