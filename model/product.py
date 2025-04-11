import datetime


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

    def __init__(
        self,
        id: int,
        foreign_id: int,
        name: str,
        url: str,
        regular_price: int,
        selling_price: int,
        discount_amount: int,
        discount_percentage: float,
        image_url: str,
        description: str,
        stock: int,
        additional_image_urls: str,
        publish_status: int,
        short_name: str,
        short_description: str,
        modified_date: datetime.datetime,
    ):
        self.id: int = id
        self.foreign_id: int = foreign_id
        self.name: str = name
        self.url: str = url
        self.regular_price: int = regular_price
        self.selling_price: int = selling_price
        self.discount_amount: int = discount_amount
        self.discount_percentage: float = discount_percentage
        self.image_url: str = image_url
        self.description: str = description
        self.stock: int = stock
        self.additional_image_urls: str = additional_image_urls
        self.publish_status: int = publish_status
        self.short_name: str = short_name
        self.short_description: str = short_description
        self.modified_date: datetime.datetime = modified_date
