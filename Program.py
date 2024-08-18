from Caches import Cache, CacheAcess_State
from CacheProgram import CacheProgram
import tests.TestRunner
from util.CacheAddress import CacheAdress
import tests

import os



def ON_DEBUG_JOB(DEBUGING: bool = True, ON_DEBUG_MOD_RUN: bool = True):
    if ON_DEBUG_MOD_RUN and os.getenv('DEBUG', 'false').lower() == 'true':
        DEBUGING = True
    if DEBUGING:
        tests.TestRunner.Run()


def main() -> None:
    ON_DEBUG_JOB()

    program = CacheProgram()
    arr: list = list()
    acum: int = 0
    iter = 100000
    for _ in range(iter):
        x = program.acess_until_miss()
        # print(x)
        # arr.append(x)
        acum += x
    
    print("acum: " + str(acum))
    print(acum / iter)

    print("Hello world")





if __name__ == '__main__':
    main()