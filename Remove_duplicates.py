#Remove duplicates in array
arr = [1,2,3,1,4,5,3,6]

result = []
for i in arr:
    if i not in result:
        result.append(i)
print(result)
