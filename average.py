"""import statistics

print(statistics.mean([100,90,80]))
print(statistics.median([100,90,80]))
print(statistics.mode([100,90,80]))"""

"""import sys
try:

    print("hello,my name is", sys.argv[1])
except IndexError:
    print("too few arguments")"""

import sys

if len(sys.argv) <2:
    sys.exit("too many argiments")
for arg in sys.argv[1:]:
    print("hello,my name is",arg)