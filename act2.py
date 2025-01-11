def print_factor(num):
    print("factors of ",num,"are ")
    for i in range(1,num+1):
        if num%i==0:
            print(i)
        
number =int(input("enter number"))
print_factor(number)