import datetime
from dataclasses import dataclass


@dataclass
class Product:
    id: int
    foreign_id: int
    name: str
    url: str
    regular_price: int
    selling_price: int
    discount_amount: int
    discount_percentage: float
    image_url: str
    description: str
    stock: int
    additional_image_urls: str
    publish_status: int
    short_name: str
    short_description: str
    modified_date: datetime.datetime
