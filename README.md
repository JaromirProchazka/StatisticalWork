Result:

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

Basic Cache Done
Raising Line count, falling Block size - DONE
Raising Block size, falling Line count - DONE
Raising Associativity, falling Block size - DONE
Raising Associativity, falling Line count - DONE
Large Associativity against Line count - DONE

----------  --------------  -------------  -----------------
Line Count  Block size [B]  Associativity  Lambda
32          64              32             60.49334587982255
64          1024            1              68.77731927250497
64          64              16             72.7347664457734
256         256             1              74.22233217878937
512         128             1              77.60131057078806
1024        64              1              78.87992988606486
4096        16              1              79.18528945979237
16384       4               1              79.32487220165697
2048        32              1              79.4789826916284
512         64              2              80.86433063791554
1024        32              2              82.23866959064327
256         64              4              82.31388329979879
512         16              8              84.00410677618069
1024        16              4              84.33470764617691
----------  --------------  -------------  -----------------
```
