#Remove duplicates in array
arr = [1, -2, 2, 3, 1, 4, 5, -3, 6]
seen = set()
result = []
for i in arr:
    if abs(i) not in seen:
        seen.add(abs(i))
        result.append(i)
print(result)
