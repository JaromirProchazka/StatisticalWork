from Caches import Cache, CacheAcess_State
from util.CacheAddress import CacheAdress
from random import randint, choice


class CacheProgram: 
    """What we want is to measure cash misses on acesses. We don't want to count as a Miss, when we try to read data, which are acessed for the first time (Fill). Therefor the Miss will be an acess to cache to adress which we know was at least once in history filled and which results in not finding the data."""
    def __init__(self, _cash_size_power:int = 16, _line_count_power:int = 10, block_size_power:int = 6, _associativity_power:int = 0) -> None:
        self.line_count = 1 << _line_count_power
        self.block_size = 1 << block_size_power
        
        self.index_bit_count:int = _line_count_power
        self.offset_bit_count:int = block_size_power >> _associativity_power
        self.associativity:int = 1 << _associativity_power

        self.cache = Cache(_cash_size_power, block_size_power >> _associativity_power, _line_count_power, 1 << _associativity_power)
        self.acessed: set = set()
        self.filled: bool = False

    def acess_until_miss(self) -> int:
        """Fills the cash completaly and retruns an average number of acesses before the first miss."""
        if not self.filled:
            self._fill()
            self.filled = True

        count: int = 0
        stat: CacheAcess_State = None

        while stat != CacheAcess_State.MISS:
            a = choice(list(self.acessed))
            stat = self._do_acess(CacheAdress(a, self.cache))
            if stat == CacheAcess_State.HIT:
                count += 1

        return count

    def _random_adress(self) -> int:
        return randint(1, 1 << 32)
    
    def _do_acess(self, adress: CacheAdress) -> CacheAcess_State:
        self.acessed.add(adress.adress)
        return self.cache.get_or_loadget(adress)
    
    def _base_fill(self) -> None:
        """Simply fills the cache completaly and deterministicaly."""
        a = CacheAdress(0, self.cache)
        for _ in range(self.line_count - 1):
            a.inc_index()
            for _ in range(self.associativity):
                a.inc_tag()
                self._do_acess(a)
            a.nul_tag()

    def _fill(self) -> None:
        """First fills the cache deterministicaly and than does some more random acesses."""
        self._base_fill()

        number_of_random_acesses = self.line_count * self.associativity * 4
        for _ in range(number_of_random_acesses):
            a = self._random_adress()
            self._do_acess(CacheAdress(a, self.cache))