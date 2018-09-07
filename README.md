# Test_Qz
Python-Qz

Sample Commands

Overlapping Lines
1. python overlap.py [15,20] [20,25]

Find if strings are gt, lt or equal
2. python string\_gt\_ls.py 1.2.3 3.2.1 (One assumption here is that the zero value is not ignored and hence the values with zero in it becomes zero)

Least Recently Used cache with time expiration
3. python LRU.py

>> python lru_cache.py
   Cache now
   [('key', 'value')]
   value
   Cache after 5 seconds
   [('key', 'value')]
   Cache after insertion of two more entries
   [('key', 'value'), ('one', 'one'), ('two', 'two')]
   Cache after ten seconds
   [('one', 'one'), ('two', 'two')]

