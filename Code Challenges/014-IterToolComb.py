# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

r,sz = [int(r) if r.isdigit() else r for r in input().split()]

final = []
for i in range(1,sz+1):
    final.extend(combinations(sorted(r), i))
for i in final:
    print("".join(i))
