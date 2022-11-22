#Factorial of 5:
def f1(num):
    return 1 if (num==1 or num==0) else num*f1(num-1);
        
num=5
print("The Factorial of 5 :",f1(num))
