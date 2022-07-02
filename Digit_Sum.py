#Take a number user input and find sum of digits of this number.

n=int(input("Enter a number:"))
sum=0
while n!=0:
    sum=sum+(n%10)
    n=n//10
print("Sum of digit of number:")
print(sum)