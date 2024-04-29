from fastapi import FastAPI, Response
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


class APIWrapper:
    """
   Wraps API methods for handling requests.

   Methods:
       root(item: Item): Handles POST requests to the root endpoint with JSON body.
   """

    def __init__(self):
        self.app = FastAPI()

    async def root(self, item: Item):
        """
        Handles POST requests to the root endpoint.

        Args:
            item (Item): The item data sent in the JSON body.

        Returns:
            Response: A message confirming the received item.
        """
        api_name = self.__class__()
        return Response({"message": f"Hello World {api_name}"})

    async def another_method(self):
        # Define your other API methods here
        pass


# Instantiate your API wrapper class
api = APIWrapper()

# Add routes to your FastAPI app
api.app.add_api_route("/", api.root, methods=["GET"])
