#Count of vowels
vowels = "aeiouAEIOU"

name = input("Enter the string")
count = 0
for i in name:
    if i in vowels:
        count += 1
print(count)
