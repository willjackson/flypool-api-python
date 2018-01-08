import json
from urllib.parse import urljoin

import requests


class PoolAPI:
    """
    API to connect to the FlyPool and other pools e.g.;
        - Ethermine.org endpoint: https://api.ethermine.org
        - Ethpool.org endpoint: http://api.ethpool.org
        - Ethermine ETC endpoint: https://api-etc.ethermine.org
        - Flypool Zcash endpoint: https://api-zcash.flypool.org
    All APIs are CORS-Enabled
    """
    def __init__(self, api_url):
        """
        An API to connect to the Pool
        :param api_url: The url of the API
        """
        self.api_url = api_url

    def create_url(self, method, *args, **kwargs):
        """
        Formats urls to connect to the api
        Examples:
        api.create_url('/example')
        api.create_url('/example/{}', pk)
        api.create_url('/example/{pk}', pk=10)

        :param method: Address for http method
        :param args: List of arguments to put in the formatted string
        :param kwargs: Dictionary to put instead of named variables in formatted string
        :return: The formatted url
        """
        if not (args or kwargs):
            return urljoin(self.api_url, method)
        return urljoin(self.api_url, method).format(*args, **kwargs)

    def json_response(self, method, *args, **kwargs):
        """
        Request GET on some HTTP methods of API and returns dictionary of the output
        :param method: Address for http method
        :param args: List of arguments to put in the formatted string
        :param kwargs: Dictionary to put instead of named variables in formatted string
        :return: dictionary of received JSON
        """
        r = requests.get(self.create_url(method, *args, **kwargs))
        if not r.ok:
            raise Exception()  # TODO Better Exception
        return json.loads(r.content.decode())['data']


class FlyPoolAPI(PoolAPI):
    """
    API for FlyPool
    """
    def __init__(self):
        super().__init__('https://api-zcash.flypool.org')


class EtherMineETCAPI(PoolAPI):
    """
        API for EtherMineETC
    """
    def __init__(self):
        super().__init__('https://api-etc.ethermine.org')


class EtherMineAPI(PoolAPI):
    """
        API for EtherMine
    """
    def __init__(self):
        super().__init__('https://api.ethermine.org')


class EtherPoolAPI(PoolAPI):
    """
        API for EtherPool
    """
    def __init__(self):
        super().__init__('http://api.ethpool.org')


class API:
    """
    Have factory method to load the relevant API for your purpose
    """
    @staticmethod
    def get_instance(pool):
        """
        Create an instance of your requested pool
        Now supported pools;
            - fly-pool
            - ether-mine-etc
            - ether-mine
            - ether-pool
        :param pool: Name of the pool you need
        :return: Instance of PoolAPI can be used for connecting the pool API
        """
        pools = {
            'fly-pool': FlyPoolAPI,
            'ether-mine-etc': EtherMineETCAPI,
            'ether-mine': EtherMineAPI,
            'ether-pool': EtherPoolAPI
        }

        if pool in pools.keys():
            return pools[pool]()
        return PoolAPI(pool)
