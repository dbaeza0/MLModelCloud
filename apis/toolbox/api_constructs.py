from abc import ABC, abstractmethod
from typing import Tuple
from starlette.responses import FileResponse
from apis.toolbox.api_models import ServiceHealth
from datetime import datetime
from pathlib import Path


class BaseAPI(ABC):
    _start_time: datetime
    _api_name: str
    __version__ = "0.0.1"
    _favicon_path = 'static/favicon.ico'

    @abstractmethod
    def all_data_sources_reachable(self) -> Tuple[int, str]:
        """
        Check if all data sources are reachable. If one fails, return (503, f'{failed_source_name}: error message')

        Returns:
            tuple[int, str]: A tuple containing an HTTP status code and a message.
                The status code indicates the result of the operation.
                The message provides additional details about the status.
        """
        pass

    def collect_health_data(self) -> ServiceHealth:
        status_code, message = self.all_data_sources_reachable()
        health = ServiceHealth(name=self._api_name,
                               version=self.__version__,
                               status=status_code,
                               status_message=message,
                               timezone=str(datetime.now().astimezone().tzinfo),
                               uptime=str(datetime.now() - self._start_time))
        return health

    @classmethod
    async def favicon(cls):
        return FileResponse(Path(cls._favicon_path).absolute())

    @classmethod
    def _record_start_time(cls):
        cls._start_time = datetime.now()
