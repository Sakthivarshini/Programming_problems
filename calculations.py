def calculations():
#Enter the input eg: 1+2
    exp = input("Enter the calculation: ")
    for i in "+-*/":
        if i in exp:
            try:
                num1,num2 = map(int,exp.split(i))
                result = eval(f"{num1}{i}{num2}")
                print(result)
            except Exception:
                print('Invalid input')
            return
    print("Invalid Operator, Please use one the operators: +-*/")

if __name__ =="__main__":
    calculations()
