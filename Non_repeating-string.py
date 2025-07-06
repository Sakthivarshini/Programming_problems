#Find First Non-Repeating Character in a String
name = input()
result =""

for i in name:
    if i not in result:
        result += i

for i in result:
    if name.count(i) ==1:
        print(i)
        break
