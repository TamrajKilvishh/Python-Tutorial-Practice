import re
# Enter your code here. Read input from STDIN. Print output to STDOUT

S = input().strip()

pattern = r"(?<=[bcdfghjklmnpqrstvwxyz])([aeiou]{2,})(?=[bcdfghjklmnpqrstvwxyz])"


result = re.findall(pattern, S, re.IGNORECASE)

if result:
    for i in result:
        print(i)

else:
    print(-1)
