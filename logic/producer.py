from repository.product_repo import Product_Repo
from talker.lister import Lister


class Producer:
    def __init__(self, repo: Product_Repo, lister: Lister):
        self.repo = repo
        self.lister = lister
