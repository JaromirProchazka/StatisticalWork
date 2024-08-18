import tests.TestRunner
import tests
from StatisticalAnalysis.StatisticalAnalysis import Analysis
import os



def ON_DEBUG_JOB(DEBUGING: bool = True, ON_DEBUG_MOD_RUN: bool = True):
    if ON_DEBUG_MOD_RUN and os.getenv('DEBUG', 'false').lower() == 'true':
        DEBUGING = True
    if DEBUGING:
        tests.TestRunner.Run()


def main() -> None:
    print('Start')
    ON_DEBUG_JOB()
    print()

    stat: Analysis = Analysis()
    stat.set_n(1.0, 0.05).experiment()
    print('Basic Cache Done')

    stat.reformat_cache(line_count_power=11, block_size_power=5, associativity_power=0).experiment()
    stat.reformat_cache(line_count_power=12, block_size_power=4, associativity_power=0).experiment()
    stat.reformat_cache(line_count_power=14, block_size_power=2, associativity_power=0).experiment()
    print('Raising Line count, falling Block size - DONE')

    stat.reformat_cache(line_count_power=9, block_size_power=7, associativity_power=0).experiment()
    stat.reformat_cache(line_count_power=8, block_size_power=8, associativity_power=0).experiment()
    stat.reformat_cache(line_count_power=6, block_size_power=10, associativity_power=0).experiment()
    print('Raising Block size, falling Line count - DONE')

    stat.reformat_cache(line_count_power=10, block_size_power=5, associativity_power=1).experiment()
    stat.reformat_cache(line_count_power=10, block_size_power=4, associativity_power=2).experiment()
    stat.reformat_cache(line_count_power=9, block_size_power=4, associativity_power=3).experiment()
    print('Raising Associativity, falling Block size - DONE')

    stat.reformat_cache(line_count_power=9, block_size_power=6, associativity_power=1).experiment()
    stat.reformat_cache(line_count_power=8, block_size_power=6, associativity_power=2).experiment()
    stat.reformat_cache(line_count_power=6, block_size_power=6, associativity_power=4).experiment()
    print('Raising Associativity, falling Line count - DONE')

    stat.reformat_cache(line_count_power=5, block_size_power=6, associativity_power=5).experiment()
    print('Large Associativity against Line count - DONE')
    # sstat.reformat_cache(line_count_power=10, block_size_power=4, associativity_power=4).experiment()
    # pprint('Fully associative - DONE')

    print()
    stat.log_results()





if __name__ == '__main__':
    main()