#take the roman numeral from the user and change it to an integer
def roman_to_int(a):
    roman={"I":1,'L':50,'X':10,'M':1000,'C':100,'D' :500}
    int_form=0

    for i in range(len(a)):

       if i+1<len(a) and roman[a[i]]<roman[a[i+1]]:
        int_form-=roman[a[i]]
       else:
          int_form+=roman[a[i]]
    return int_form
a=input("enter number")
print("inters form of ",a,"is",roman_to_int(a))
       