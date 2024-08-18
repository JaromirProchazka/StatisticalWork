from enum import Enum
from util.FixedArrray import FixedSizeArray
from random import randint


class _CacheField_State(Enum):
    VALID = 1
    INVALID = 2
    NOT_PRESENT = 3

class CacheAcess_State(Enum):
    HIT = 5
    MISS = 6


class _CacheField:
    """The data field in Cache. On tag of value 0, it is an empty data field."""
    def __init__(self, _tag: int = 0, line_length: int = 1024, _valid: bool = False) -> None:
        self.valid = _valid
        self.tag = _tag
    
    def validate(self) -> None:
        self.valid = True

class _CacheLine:
    def __init__(self, associativity: int = 1) -> None:
        if associativity <= 0:
            raise IndexError("Associativity must be greater than 0. It is '" + associativity + "'!")
        self.fields: FixedSizeArray = FixedSizeArray(associativity, _CacheField)
    
    def look_for(self, tag: int) -> _CacheField_State:
        for field in self.fields.array:
            if field.tag == tag:
                if field.valid:
                    return _CacheField_State.VALID
                else:
                    return _CacheField_State.INVALID
        else:
            return _CacheField_State.NOT_PRESENT
    
    def insert_on_not_present(self, tag: int) -> None:
        for field in self.fields.array:
            if not field.valid:
                field.tag = tag
                field.validate()
                break
        else:
            overwriten_i = randint(0, self.fields.size - 1)
            self.fields.array[overwriten_i].tag = tag
            self.fields.array[overwriten_i].validate()
            return
            
class Cache:
    from util.CacheAddress import CacheAdress

    def __init__(self, _cache_size_power: int = 16, _line_size_power: int = 6, _line_count_power: int = 10, _associativity: int = 1) -> None:
        self._cache_size_power: int = _cache_size_power
        self._line_size_power: int = _line_size_power
        self._line_count_power: int = _line_count_power
        self._associativity: int = _associativity

        cache_size: int = 1 << _cache_size_power
        line_size: int = 1 << _line_size_power
        line_count: int = 1 << _line_count_power

        if cache_size != line_size * _associativity * line_count:
            raise ValueError("The Cache parameters doesn't result in Cache of the wanted size! cache_size:'{cache_size}' != cache_line_size:'{cache_line_size} * associativity:'{associativity}' * cache_line_count:'{cache_line_count}'!")

        self._line_count = line_count
        self._lines = [_CacheLine(_associativity)] * line_count
    
    def get_or_loadget(self, adress: CacheAdress) -> CacheAcess_State:
        line = self._lines[adress.index]
        status: _CacheField_State = line.look_for(adress.tag)

        if status == _CacheField_State.VALID:
            return CacheAcess_State.HIT
        elif status == _CacheField_State.NOT_PRESENT:
            # LOADING
            line.insert_on_not_present(adress.tag)
            return CacheAcess_State.MISS
        else:
            return CacheAcess_State.MISS
        

