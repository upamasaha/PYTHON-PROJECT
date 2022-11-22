num=int(input("Enter a number:"))
arms=num
length=len(str(num))
sum1=0
while num!=0:
    rem=num%10
    sum1=sum1+rem**length
    num=num//10
if arms==sum1:
    print("Armstrong Number")
else:
    print("It's not an armstrong Number")
