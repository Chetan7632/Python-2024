
from typing import Counter

def counter(list):
    dup = Counter(list)
    for num in integers:
        if dup[num] > 1:
            return True
        else:
            return False


integers = []
for i in range(6):
    integers.append(int(input(f"Enter interger {i}: ")))

flag = counter(integers)
if flag:
    print("Duplicate")
else:
    print("Unique")
