import math

comparetable = [0, math.nan, True, False, "", None]

for i in range(len(comparetable)):
    for j in range(len(comparetable)):
        print(f"{comparetable[i]} == {comparetable[j]}: {comparetable[i] == comparetable[j]}")
    print()
