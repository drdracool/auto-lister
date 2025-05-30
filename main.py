from repository.product_repo import Product_Repo
from model.product import Product
from logic.collector import Collector
from logic.producer import Producer
from talker.harvest import Harvest
from talker.lister import Lister
from client.selenium_client import Selenium_client

if __name__ == "__main__":
    selenium_client = Selenium_client()
    repo = Product_Repo("database/products.db")
    harvest = Harvest(selenium_client)
    lister = Lister(selenium_client)
    collector = Collector(
        repo,
        harvest,
    )
    producer = Producer(repo, lister)

    product = Product(
        None,
        6425,
        "43",
        "642",
        623,
        532,
        532,
        65342.543,
        "grsew",
        "hreabg",
        643,
        "jtnehbasrg",
        3,
        "gadfvw",
        "jtnerahweghjtrsrahwbgsde",
        None,
    )

    # repo.insert_product(product)
    prod = repo.get_product_by_foreign_id(6425)
    print(prod)
