from flypool.api import API, PoolAPI


class Pool:
    """
    A Pool with all it features and information
    """
    def __init__(self, api):
        """
        Creates new connection to your arbitrary Pool
        :param api: Name of the Pool or a PoolAPI instance
        """
        if isinstance(api, str):
            self.api = API.get_instance(api)
        elif isinstance(api, PoolAPI):
            self.api = api
        else:
            raise Exception()  # TODO better exception

    def stats(self):
        """
        Basic Pool Statistics
        :return: List of latest mined blocks, top miners, number of miners, pool hash rate, and the coin price.
        Sample Output:
        "minedBlocks": [
            {
                "number": 192468,
                "miner": "t1c3yo3zHDtS9BJTGbZStgLnkqZiodwy3sL",
                "time": 1506594861
            },
            .
            .
            .
            {
                "number": 192451,
                "miner": "t1MH7cwkdL62mwXeJV9uqoVAFVJXz4QwdP4",
                "time": 1506590574
            }
        ],
        "topMiners": [
            {
                "miner": "t1fJuHWrfcWnYMYyP9VAF96vRnvND2NziMG",
                "hashRate": 1143586.6666666665
            },
            .
            .
            .
            {
                "miner": "t1cVHQf5EqfTP4GarxMjNs7QWyYrivrYFa2",
                "hashRate": 522533.33333333326
            }
        ],
        "poolStats": {
            "hashRate": 197057795.72500134,
            "miners": 46231,
            "workers": 125426,
            "blocksPerHour": 12.58
        },
        "price": {
            "usd": 298.67,
            "btc": 0.07202
        }
        """
        method = '/poolStats'

        response = self.api.json_response(method)
        return response

    def price(self):
        """
        The coin current price
        """
        return self.stats()['price']

    def top_miners(self):
        """
        The pool top miners
        """
        return self.stats()['topMiners']

    def pool_stats(self):
        """
        Statistics of the pool: hash rate, number of miners, ...
        """
        return self.pool_stats()['poolStats']

    def latest_mined_blocks(self):
        """
        Latest mined blocks in pool
        """
        return self.pool_stats()['minedBlocks']

    def blocks_history(self):
        """
        Array of server hashrate ordered by time ASC
        Output Sample:
        [{
            "time": 1506513567,
            "nbrBlocks": 5,
            "difficulty": 6267480
        },
        .
        .
        .
        {
            "time": 1506597768,
            "nbrBlocks": 3,
            "difficulty": 6049396
        }]
        """
        method = '/blocks/history'

        return self.api.json_response(method)

    def network_stats(self):
        """
        Hardness, hash rate, etc from the coin network
        Output Sample:
        {
            "time": 1506605973,
            "blockTime": 172.425,
            "difficulty": 6140509,
            "hashrate": 327255799,
            "usd": 304.78,
            "btc": 0.07248
        }
        """
        method = '/networkStats'

        return self.api.json_response(method)

    def servers(self):
        """
        Array of server hashrate ordered by time ASC
        """
        method = '/servers/history'

        return self.api.json_response(method)
