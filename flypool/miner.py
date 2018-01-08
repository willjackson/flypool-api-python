from .pool import *


class Miner:
    """
    Information and statistics of a miner the coin network
    """
    def __init__(self, api, miner_address):
        """
        Information and statistics of a miner the coin network
        :param api: string or PoolAPI instance showing the API for arbitrary pool
        :param miner_address: The miner's address mining with
        """
        self.miner_address = miner_address

        if isinstance(api, str):
            self.api = API.get_instance(api)
        elif isinstance(api, PoolAPI):
            self.api = api
        else:
            raise Exception()  # TODO better exception

    def history(self):
        """
        History of the miner
        Output Sample:
        [{
            "time": 1506520428,
            "reportedHashrate": 0,
            "currentHashrate": 136200.00000000003,
            "validShares": 10215,
            "invalidShares": 8,
            "staleShares": 0,
            "averageHashrate": 129953.37931034483,
            "activeWorkers": 69
        }, ...]
        """
        method = '/miner/{miner_address}/history'
        return self.api.json_response(method, miner_address=self.miner_address)

    def status(self):
        """
        Current status of the miner
        Sample Output:
        {
            "time": 1506606061,
            "lastSeen": 1506606154,
            "reportedHashrate": 0,
            "currentHashrate": 137306.66666666666,
            "validShares": 5149,
            "invalidShares": 0,
            "staleShares": 0,
            "averageHashrate": 135016.43678160926,
            "activeWorkers": 71,
            "unpaid": 9596476,
            "unconfirmed": 36480366,
            "coinsPerMin": 0.0014212991674269694,
            "usdPerMin": 0.4331835602483917,
            "btcPerMin": 0.00010301576365510675
        }
        """
        method = '/miner/{miner_address}/currentStats'
        return self.api.json_response(method, miner_address=self.miner_address)

    def now(self):
        """
        Same as the status() function
        """
        return self.status()

    def hash_rate(self):
        """
        Current and average hash-rate of the miner
        """
        now = self.status()
        return {
            'current_rate': now['currentHashrate'],
            'average_rate': now['averageHashrate']
        }

    def valid_shares(self):
        """
        Amount of valid shares of the miner
        """
        return self.now()['validShares']

    def invalid_shares(self):
        """
            Amount of invalid shares of the miner
        """
        return self.now()['invalidShares']

    def stale_shares(self):
        """
            Amount of stale shares of the miner
        """
        return self.now()['staleShares']

    def per_min(self):
        """
        Amount of miner's mining rate per minute
        """
        now = self.now()
        return {
            'btc': now['btcPerMin'],
            'usd': now['usdPerMin'],
            'coins': now['coinsPerMin']
        }

    def balance(self):
        """
        Balance for the miner
        Amount of unpaid and unconfirmed coins for the miner
        :return:
        """
        now = self.now()
        return {
            'unpaid': now['unpaid'],
            'unconfirmed': now['unconfirmed'],
        }

    def active_workers_counts(self):
        """
        Number of active workers in the pool
        """
        return self.now()['activeWorkers']

    def workers(self):
        """
        List of miner workers
        Output Sample:
        [{
            "worker": "1060gg01",
            "time": 1506606550,
            "lastSeen": 1506606488,
            "reportedHashrate": 0,
            "currentHashrate": 1813.3333333333333,
            "validShares": 68,
            "invalidShares": 0,
            "staleShares": 0,
            "averageHashrate": 1640.4444444444443
        }, ...]
        """
        method = '/miner/{miner_address}/workers'
        return self.api.json_response(method, miner_address=self.miner_address)

    def worker_history(self, worker_name):
        """
        History for the selected worker of the miner
        :param worker_name: Name of the miner's worker
        Output Sample:
        [{
            "time": 1506563908,
            "reportedHashrate": 0,
            "currentHashrate": 1346.6666666666667,
            "validShares": 101,
            "invalidShares": 0,
            "staleShares": 0,
            "averageHashrate": 1127.485380116959
        }, ...]
        """
        method = '/miner/{miner_address}/worker/{worker_name}/history'
        return self.api.json_response(method,
                                      miner_address=self.miner_address,
                                      worker_name=worker_name)

    def worker_status(self, worker_name):
        """
        Current status of the mentioned worker
        :param worker_name: Name of the worker needs to monitor
        Output Sample:
        {
            "time": 1506606550,
            "lastSeen": 1506606514,
            "reportedHashrate": 0,
            "currentHashrate": 933.3333333333334,
            "validShares": 35,
            "invalidShares": 0,
            "staleShares": 0,
            "averageHashrate": 1103.3333333333333
        }
        """
        method = '/miner/{miner_address}/worker/{worker_name}/currentStats'
        return self.api.json_response(method,
                                      miner_address=self.miner_address,
                                      worker_name=worker_name)

    def payouts(self):
        """
        List of payouts to the Miner
        Output Sample:
        [{
            "start": 192234,
            "end": 192397,
            "amount": 50258832,
            "txHash": "1caaebfee1749f4bb4f077258a18fda129f12ae619d06825076249b5ab76f0f0",
            "paidOn": 1506603658
        }, ...]
        """
        method = '/miner/{miner_address}/payouts'
        return self.api.json_response(method, miner_address=self.miner_address)

    def rounds(self):
        """
        Array of rounds sorted by block number DESC, limited to the last 1000 rounds
        """
        method = '/miner/{miner_address}/rounds'
        return self.api.json_response(method, miner_address=self.miner_address)

    def settings(self):
        """
        Settings of the Miner
        :return: dictionary of Email, IP address, ... of the Miner
        Output Sample:
        {
            "email": "***gcom@nate.com",
            "monitor": 1,
            "minPayout": 50000000,
            "ip": "*.*.*.112"
        }
        """
        method = '/miner/{miner_address}/settings'
        return self.api.json_response(method, miner_address=self.miner_address)