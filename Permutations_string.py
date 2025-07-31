from itertools import permutations
s= input("Enter the string: ")
perm = set()
for i in permutations(s):
    p = ''.join(i)
    perm.add(p)
for p in perm:
    print(p)
