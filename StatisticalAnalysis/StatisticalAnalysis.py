import sys
# setting path
from StatisticalAnalysis.logger import _StatLogger
sys.path.append('../StatisticalSemestralWork')
from CacheSimulator.CacheProgram import CacheProgram
from util.CacheAddress import CacheAdress
from typing import Self
from math import sqrt


class Analysis:
    def __init__(self) -> None:
        self._cache: CacheProgram = CacheProgram()
        self._n: int = 100_000
        self._cache_size_power: int = 16
        self._log: _StatLogger = _StatLogger()

        # self.Xn: list = list()
        self.En: float = 0 
    
    def reformat_cache(self, line_count_power:int = 10, block_size_power:int = 6, associativity_power:int = 0) -> Self:
        """The size of our cache in 1<<16, so the parameters must add up to that."""
        self._cache: CacheProgram = CacheProgram(self._cache_size_power, line_count_power, block_size_power, associativity_power)
        return self
    
    def _set_n(self, new_n: int) -> Self:
        self._n = new_n
        return self
    
    def set_n(self, max_differentce: float, max_likelyhood: float) -> Self:
        """Uses the chebyshev inequality to compute the n, so that the Likelihood that the measured En from the actuall one is less than {max_differentce} is less than {max_likelyhood}. Than the n is set."""
        epsilon: int = 10
        n: int = ((150 / (max_differentce * sqrt(max_likelyhood))) ** 2) + epsilon
        return self._set_n(int(n))
    

    def _make_experiment(self) -> float:
        """Returns the lambda for the Exponential distribution measured."""
        acum: int = 0
        for _ in range(self._n):
            x = self._cache.acess_until_miss()
            acum += x
        
        self.En = acum / self._n
        return 1 / self.En
    
    def experiment(self) -> None:
        """Returns the lambda for the Exponential distribution measured and returns a string of loged result."""
        res: float = self._make_experiment()
        self._log.add_row(self._cache.line_count, self._cache.block_size, self._cache.associativity, res)

    def log_results(self):
        """Logs all results and cleans the data."""
        self._log.log()
        self._log.clear_rows()
        

    


