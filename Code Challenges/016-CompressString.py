# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

stringS = input()

grouping = groupby(stringS)
for i, j in grouping:
    print(tuple:=(len(list(j)), int(i)), end=" ")
