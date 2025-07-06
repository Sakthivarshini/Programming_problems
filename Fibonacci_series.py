#Fibonacci series
terms = int(input("Enter no.of terms"))
n1 = 0
n2 = 1
count =0

while count < terms:
    print(n1, end=' ')
    n = n1 + n2
    n1 = n2
    n2 = n
    count += 1
