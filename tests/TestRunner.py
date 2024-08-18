import sys
# setting path
sys.path.append('../StatisticalSemestralWork')
from CashSimulator.Caches import Cache, CacheAcess_State
from util.CacheAddress import CacheAdress

class _CashAdressTests:
    def __init__(self) -> None:
        pass
    
    def test__correct_segments(self) -> None:
        c = Cache(16, 5, 10, 2)
        adress = 0b11101110111011101_1101101101_10101
        a = CacheAdress(adress, c)

        if a.offset != 0b10101:
            raise ValueError("Offset should be 0b10101 but is {a.offset}!")
        if a.index != 0b1101101101:
            raise ValueError("Index should be 0b1101101101 but is {a.index}!")
        if a.tag != 0b11101110111011101:
            raise ValueError("Index should be 0b11101110111011101 but is {a.tag}!")
        
        print("test__correct_segments DONE")

    def test__incremetns(self):
        c = Cache(16, 5, 10, 2)
        adress = 0b11101110111011100_1101101100_10101
        expected_adress = 0b11101110111011101_1101101101_10101
        expected_adress_next = 0b00000000000000000_1101101101_10101
        expected_tag_next = 0b00000000000000000
        expected_index = 0b1101101101
        expected_tag = 0b11101110111011101
        expected_offset = 0b10101
        a = CacheAdress(adress, c)

        a.inc_index()
        a.inc_tag()

        if a.adress != expected_adress and a.tag != expected_tag and a.index != expected_index and a.offset != expected_offset:
            raise Exception("Adress parts Increments doesn't work!")
        
        a.nul_tag()

        if a.adress != expected_adress_next and a.tag != expected_tag_next and a.index != expected_index and a.offset != expected_offset:
            raise Exception("Nullifying tag doesn't work!")
        
        print("test__incremetns DONE")


class _CacheTests:
    def __init__(self) -> None:
        pass

    def test__simple_write(self) -> None:
        c = Cache()
        adress = 0b1111_1111_1111_1111_1111_1111_1111_1111
        a = CacheAdress(adress, c)

        if c.get_or_loadget(a) != CacheAcess_State.MISS:
            ValueError("On first access it should have Missed!")
        
        if c.get_or_loadget(a) != CacheAcess_State.HIT:
            raise ValueError("On second acess to the same adress, the valid data should have been found!")
        
        if c.get_or_loadget(a) != CacheAcess_State.HIT:
            raise ValueError("On third acess to the same adress, the HIT shouldn't change validity!")
        
        print("test__simple_write DONE")
    
    def test__error_on_cache_attributes_not_adding_up(self) -> None:
        # Correct:
        c: Cache = Cache(16, 6, 9, 2)
        err: bool = False 

        # Examples of incorrect:
        try:
            c = Cache(16, 3, 9, 4)
        except:
            err = True
        if not err:
            raise ValueError('Attributes do not add up. Should have thrown an Error! Associativity can not be larger than Block size!')
        err = False

        try:
            c = Cache(17, 6, 10, 1)
        except:
            err = True
        if not err:
            raise ValueError('Attributes do not add up. Should have thrown an Error!')
        err = False

        try:
            c = Cache(16, 6, 10, 2)
        except:
            err = True
        if not err:
            raise ValueError('Attributes do not add up. Should have thrown an Error!')
        err = False

        try:
            c = Cache(16, 6, 9, 1)
        except:
            err = True
        if not err:
            raise ValueError('Attributes do not add up. Should have thrown an Error!')
        err = False

        try:
            c = Cache(16, 7, 10, 1)
        except:
            err = True
        if not err:
            raise ValueError('Attributes do not add up. Should have thrown an Error!')
        err = False

        print("test__error_on_cache_attributes_not_adding_up DONE")

    
    def test__on_line_full(self) -> None:
        c = Cache(16, 5, 10, 2)
        adress1 = 0b11111111111111111_1111111111_11111
        adress2 = 0b11111111111111110_1111111111_11111
        adress3 = 0b11111111111111100_1111111111_11111

        a1 = CacheAdress(adress1, c)
        a2 = CacheAdress(adress2, c)
        a3 = CacheAdress(adress3, c)

        if c.get_or_loadget(a1) != CacheAcess_State.MISS:
            ValueError("On first access it should have Missed!")
        
        if c.get_or_loadget(a2) != CacheAcess_State.MISS:
            ValueError("On second access it should have Missed!")

        if c.get_or_loadget(a1) != CacheAcess_State.HIT:
            raise ValueError("On third acess to the same adress, the valid data should have been found!")
        
        if c.get_or_loadget(a3) != CacheAcess_State.MISS:
            raise ValueError("On forth acess to the not yet used and the line being FULL, the data should have not been found!")
        
        if c.get_or_loadget(a3) != CacheAcess_State.HIT:
            raise ValueError("On fifth acess to the reseantly added data to the full line, the valid data should replace some other and should have have been found!")
        
        if c.get_or_loadget(a2) != CacheAcess_State.MISS and c.get_or_loadget(a1) != CacheAcess_State.MISS:
            raise ValueError("On sixth acess to one of the added data at the start of the program, since the the line was full with those two data and than one of tham should have been overwriten, at least one of these should be now a miss!")

        print("test__on_line_full DONE")


def Run() -> None:
    ct: _CacheTests = _CacheTests()
    at: _CashAdressTests = _CashAdressTests()

    print(">> Cache Adress Parsing Tests")
    at.test__correct_segments()
    at.test__incremetns()

    print(">> Cache Working Tests")
    ct.test__error_on_cache_attributes_not_adding_up()
    ct.test__simple_write()
    ct.test__on_line_full()

    print(">> Tests FINISHED :)")


if __name__ == '__main__':
    Run()