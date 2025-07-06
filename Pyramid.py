height = int(input())

for i in range(height):
    #print spaces
    for j in range(height-i-1):
        print(" ", end="")

    #print stars
    for k in range(2*i+1):
        print("*",end="")
    print()
