# Statistical Semestral Work - Cache Analysis

## Program Description

We use a Simulator of Hardware processor caches of constant size of 2^16 to **approximate its number of HIT until first MISS using Exponential Distribution**. We can than set it's the line count, size of a data block and associativity. (Cache takes an address and parses if to tag-index-offset, than the line is retrieved by index. There is a number of blocks in the line where each is marked with a tag. The number of blocks in a line is the associativity. The offset denotes the size of blocks.)

What we than measure in the Analysis is the Probabilistic Distribution of the number of in a certain way random cache accesses HITs before the first MISS. So one Event for the sequence of accesses like `HIT, HIT, HIT, MISS` is 3. For that we need the Mean, which we will approximate by repeating the experiment `n` times.

In the Program.py, we first compute `n` with `Analysis.set_n` method which result in is **Result** section after the `Number of iterations of the experiment:` tag. Than we can use (default is provided) `Analysis.reformat_cache` which creates new Cache of given parameters. The `Analysis.experiment` method which runs the experiment n-times and to the resulting table, it writes the row with the cache parameters and the resulting lambda which describes the Exponential distribution: Exp(lambda).

## Cache Experiment

A Cache is a number an array of Lines, where each line an array of Blocks. Each block has the Tag it stares and a Valid bit of the stored information. On access we index the line, where we try to find the correct tag. If the tag is found and Block is Valid, we have HIT, otherwise MISS.

When the empty cache is created, we must ensure that the MISS isn't created by the fact, that the address is accessed for the first time. For that reason, we first fill the cache with some uniformly random addresses, such that each Block is Fild in and Valid. After that the Experiment can start. We generate random 32bit number using the uniformly random generator and we use it as the address to access. If the access is cached (HIT), we make new random access until the last one is not cached (MISS). We repeat this whole process `n` times.

## Statistical Analysis

The detailed explanation can be found in the **proofs.pdf** file.

We basically first compute the number of iterations using the Chebyshev inequality in the `Analysis.set_n` where the `max_differentce` parameter denotes the maximal difference between the aproximation of the Mean and the actual one. The `max_likelyhood` parameter denotes the likelihood that the difference is less than `max_differentce`. In the code, we use:

```
# with definition:
def set_n(self, max_differentce: float, max_likelyhood: float) -> Self:
        """Uses the Chebyshev inequality to compute the n, so that the Likelihood that the measured En from the actual one is less than {max_differentce} is less than {max_likelyhood}. Than the n is set."""
        epsilon: int = 10
        n: int = ((100 / (max_differentce * sqrt(max_likelyhood))) ** 2) + epsilon
        print(f"Number of iterations of the experiment: {int(n)}")
        return self._set_n(int(n))

stat.set_n(max_differentce=0.5, max_likelyhood=0.05)
```

Than once we have the well approximated Mean, we use the Method of Moments to approximate the lambda for the Exp(lambda) distribution.

## Dataset

We make Simulate Caches for many parameters:

```
stat.experiment()
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
```

# Result:

```
Start
>> Cache Adress Parsing Tests
test__correct_segments DONE
test__incremetns DONE
>> Cache Working Tests
test__error_on_cache_attributes_not_adding_up DONE
test__simple_write DONE
test__on_line_full DONE
>> Tests FINISHED :)

Number of iterations of the experiment: 800010
Basic Cache Done
Raising Line count, falling Block size - DONE
Raising Block size, falling Line count - DONE
Raising Associativity, falling Block size - DONE
Raising Associativity, falling Line count - DONE
Large Associativity against Line count - DONE

----------  --------------  -------------  ------------------
Line Count  Block size [B]  Associativity  Lambda
32          64              32             59.706694529442494
64          1024            1              67.46015684290413
64          64              16             71.23230344581961
256         256             1              76.96844333269193
512         128             1              77.87501216781855
2048        32              1              78.59416445623341
16384       4               1              79.40545905707197
4096        16              1              79.86522911051213
1024        64              1              80.22563176895306
256         64              4              81.75881451200817
512         64              2              82.18717896034518
1024        32              2              83.51706858753523
1024        16              4              83.84091385453783
512         16              8              84.69299174253652
----------  --------------  -------------  ------------------
```
