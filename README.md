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
1024        64              1              81.77023712183156
2048        32              1              81.8036809815951
4096        16              1              76.92692307692307
512         128             1              79.3375644585482
256         256             1              76.25238276782311
1024        32              2              84.85787017394993
1024        16              4              85.98882201203783
512         64              2              84.07313997477932
256         64              4              82.20715166461159
64          64              16             69.93356643356644
----------  --------------  -------------  -----------------
```
