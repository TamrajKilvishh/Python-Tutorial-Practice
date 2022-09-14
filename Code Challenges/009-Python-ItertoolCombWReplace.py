# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

alpha, gamma = [int(base) if base.isdigit() else base for base in input().split()]

for i in combinations_with_replacement(sorted(alpha), gamma):
    print("".join(i))
