from repository.product_repo import Product_Repo
from model.product import Product

if __name__ == "__main__":
    repo = Product_Repo("database/products.db")

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
