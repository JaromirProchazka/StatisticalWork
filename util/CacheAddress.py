import sys
# setting path
sys.path.append('../StatisticalSemestralWork')
# from Caches import Cache

class CacheAdress:
    def __init__(self, _adress: int, cache) -> None:
        if _adress < 0 or _adress >= 1 << 32:
            raise IndexError("This number isn't a Valid Adress! '{adress}' < 1 or '{adress}' >= 2^32(=4_294_967_296)!")
        
        self.adress = _adress

        self._offset_length = cache._line_size_power
        self._index_length = cache._line_count_power
        self._tag_length = 32 - cache._line_size_power - cache._line_count_power

        self.tag = self._get_tag(_adress)
        self.index = self._get_index(_adress)
        self.offset = self._get_offset(_adress)
    
    def inc_index(self) -> None:
        if self.index >= (1 << self._index_length) - 1:
            return
        self.index += 1
        self.adress += 1 << (self._offset_length + 1)
        
    def inc_tag(self) -> None:
        if self.tag >= 1 << self._tag_length:
            return
        self.tag += 1
        self.adress += 1 << (self._offset_length + self._index_length + 1)

    def nul_tag(self) -> None:
        self.tag = 0
        self.adress &= (1 << (self._offset_length + self._index_length)) - 1 
    
    def _get_tag(self, adress: int) -> int:
        return self._cut_right(adress, self._offset_length + self._index_length)
    
    def _get_index(self, adress: int) -> int:
        index_plus_offset = self._cut_left(adress, self._index_length + self._offset_length)
        index = self._cut_right(index_plus_offset, self._offset_length)

        return index

    def _get_offset(self, adress: int):
        return self._cut_left(adress, self._offset_length)

    
    def _cut_left(self, adress: int, left_start_pos: int) -> int:
        mask = (1 << left_start_pos) - 1   
        return adress & mask

    def _cut_right(self, adress: int, right_end_pos: int) -> int:
        return adress >> right_end_pos