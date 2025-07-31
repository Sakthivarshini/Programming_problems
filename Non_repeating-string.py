def first_non_repeating_string():
    s = input("Enter the string: ")
    count = {}
    for i in s:
        if i.isalpha():
            i_lower = i.lower()
            count[i_lower] = count.get(i,0)+1
            
    for i in s:
        if i.isalpha():
            i_lower = i.lower()
            if count[i_lower] == 1:
                print("First non-repeating character is ",i)
                break


if __name__ =="__main__":
    first_non_repeating_string()
