from repository.product_repo import Product_Repo
from talker.harvest import Harvest


class Collector:
    def __init__(self, repo: Product_Repo, harvest: Harvest):
        self.repo = repo
        self.harvest = harvest
