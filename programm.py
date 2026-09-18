#program 1
#display personal details using variables
#getting the input from user 
name = input()
age =int(input())
height = float(input())
print(name)
print(age)
print(height)

#progeam 2
#personlized greeting
name = input()
print(F"hello,{name}!")
#program 3
#add two number read as string
#taken the input as a string
a=input()
b=input()
#converting the string into integer
a=int(a)
b=int(b)
#find the sum
total=a+b
#print the result
print(total)
#program 4 
#float to integer conversion
#float:number with decimal value
#int:whole numbers without any decimal or fractional value
#reading a float value from the user
n=float(input())
#print the float value
print(n)
#convert the float into interger:decimal point values will be remove
new=int(n)
#print the result
print(new)
#program 5
#sum using arithmetic operator
#reading 2 integers from the user
a=int(input())
b=int(input())
#finding the sum and printing the result
print(a+b)
#program 6
#area of a rectangle
#reading input from the user
length=float(input())
breadth=float(input())
#calculating the area of a rectangle
area = length*breadth
#print the result
print(area)

#program 7:quotient and remainder
#user input
a=int(input())
b=int(input())
#find the quotient
q=a/b
#find the remainder
r=a%b 
#print the result
print(q)
print(r)
#program 8:power calculation 
#reading user input
base=int(input())
exponent=int(input())
#calculate the power of and print the result
print(base**exponent)

#progem 9:average of three numbers
#taking 3 integer number from the user
n1=int(input())
n2=int(input())
n3=int(input())
#find the total
total=n1+n2+n3
#find the average
avg=total/3#division operator /-->always gives the resultas a float
#print the average
print(avg)
#program 10:greater than comparision
#read 2 integer number from user
a=int(input())
b=int(input())
#check wether the 1st number is greater than the 2nd number
print(a>b)
#program 11:equality check
#check whether bothe the number are same or not 
#if the number are same -ture
#if the number are different -flase
#reading the input from the user
n1=int(input())
n2=int(input())
print(n1==n2)
#program 12:both numbems positive check
#if the number is greater than 0
#logical and -->if all the combining are ture,result is ture
#reading the input from the user
n1=int(input())
n2=int(input())
print(n1>0 and n2>0)
#program 13:at least one even number
#even number is divisible by 2(without any reminder)
#logical or -->if any one of the combiningsss condition is ture,then the resilt is ture
#arithmetic operators
#/-->division-result is in from of decimal value
example:13/2=6
#//-->floor division -retult is in form of integer 
example:13/2=6
#%-->modulo-result is the reminder of the division operation
example:13/2=1
#reading the input from the user
n1 = int(input())
n2 = int(input())
print(n1%2==0 or n2%2==0)
#program 14:logical not on a condition 
#logocal not-->reverse the result
#ture-->flase
#flase-->ture
#reading the input from the user
number=int(input())
print(not(number>0))
#program 15:augmented assignment operations
#read a number from the user 
a=int(input()) #20
a=a+5 #a = 20+5-->25
a=a*2 #a = 25*2-->50
a=a-3 #a = 50-3-->47
print(a)
#program 16:exchange valuse of two variables
#reading thr input from the user
a=int(input())
b=int(input())
#logic 1-using temp vaeiable
temp=a
a=b
b=temp
print(a)
print(b)
#logic 2:without using temp (3rd variable)
a=a+b
b=a-b
a=a-b
print(a)
print(b)
#logic 3:without using temp (3rd variable)
a=a^b
b=a^b
a=a^b
print(a)
print(b)

#logic 4:without using temp (3rd variable)
#problem:if cannot handle 0
a=a*b
b=a/b
a=a/b
print(a)
print(b)
#logic 5:using python's special
#simplest way
a,b=b,a
print(a)
print(b)
#program 17:calculate simple interest
#formula:(principle*rate*time)/100
#user inputs
principle=float(input())#loam amount
rate=float(input())#rate of interest
time=float(input())#repayment time
#calculate interest
si=(principle*rate*time/100)
#print the result
print(si)
#program 18:temperature conversion (celsius to fahrenheit)
#foemula:f=(c*9/5)+32
#read the temperature in celsius
c=float(input())
#convert the celsius to fahrenheit
f=(c*9/5)+32
print(f)
#progeam 19:check divisibility by 3 and 5
n=int(input())
print(n%3==0 and n%5==0)
#program 20:sum of digits of a two-digit number
number=int(input()) #number=48
tens=number//10  #tens=48//10=4
units=number%10  #units=48%10=8
total =tens+units #total=4+8=12
print(total)




