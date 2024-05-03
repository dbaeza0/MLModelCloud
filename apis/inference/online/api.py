from typing import Tuple

from fastapi import FastAPI
from apis.toolbox.api_constructs import BaseAPI


class OnlineInference(BaseAPI):
    """
   Wraps API methods for handling requests.

   Methods:
       root(item: Item): Handles POST requests to the root endpoint with JSON body.
   """

    def __init__(self):
        self._api_name = self.__class__.__name__
        self._record_start_time()
        self.app = FastAPI()

    def all_data_sources_reachable(self) -> Tuple[int, str]:
        """
        This api does not use data sources.

        Returns:
            tuple[int, str]: A tuple containing an HTTP status code and a message.
                The status code indicates the result of the operation.
                The message provides additional details about the status.
        """
        return 200, 'No data sources configured.'

    async def health_check(self):
        """
        Handles POST requests to the root endpoint.

        Returns:
            Response: A message confirming the received item.
        """
        health = self.collect_health_data()
        return health
