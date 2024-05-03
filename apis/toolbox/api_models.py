from pydantic import BaseModel


class Item(BaseModel):
    """
    Represents an item in the inventory.

    Attributes:
        name (str): The name of the item.
        description (str, optional): The description of the item (default is None).
        price (float): The price of the item.
        tax (float, optional): The tax rate for the item (default is None).
    """
    name: str
    description: str = None
    price: float
    tax: float = None


class ServiceHealth(BaseModel):
    """
    Represents the health status of a service.

    Attributes:
        name (str): The name of the service.
        version (tuple[int, str]): The version of the service.
        status (int): The status code indicating the health status.
        timezone (str): The timezone in which the service is operating.
        uptime (str): A string representing the uptime of the service.
    """
    name: str
    version: str
    status: int
    status_message: str
    timezone: str
    uptime: str
