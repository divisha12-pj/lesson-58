#Check if the given number is an Armstrong number or not.
a=int(input("enter number"))
sum=0
temp=a
while temp>0 :
    digit=temp % 10
    sum=sum+digit**3
    temp=temp//10
print(sum)
if a == sum:
    print(a ,"is an armstrong number")
else:
    print(a,"is not an armstrong number")

