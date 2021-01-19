import pdb

import requests
from src.crawling.agents import random_agent
from src.utils.logger import get_logger


class BaseSession(requests.Session):

    DEFAULT_HEADERS = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'cache-control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'TE': 'Trailers',
    }

    def __init__(self):
        super().__init__()
        self._logger = get_logger(self.__class__.__name__)


class TikiSession(BaseSession):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        headers = self.DEFAULT_HEADERS.copy()
        headers['User-Agent'] = random_agent()
        self.headers.update(headers)
