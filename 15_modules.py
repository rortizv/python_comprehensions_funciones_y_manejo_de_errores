import sys
#print(sys.path)

import time
timestamp = time.time()
local_time = time.localtime(timestamp)
result = time.asctime(local_time)
print(result)


# Cuántas veces se repite cada item en una lista
import collections
numbers = [1, 1, 2, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 10]
counter = collections.Counter(numbers)
print(counter)