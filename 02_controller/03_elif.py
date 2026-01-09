# 1st program 

#  how many digit given
"""
n = int(input("Enter number:"))

if (-10) <n <(10):
    print("1 digit")
    
elif (-99 <=n < -9) or (9< n <100) :
    print("2 digit")
    
elif(-999 <= n < -99) or (99<n<=999):
    print("3 digit")
    
else:
    print("greater then 3 digit")

"""

#  given character is uppercase or lowercase or  digit or spacial
"""
n =input("Enter character:")
if 'A'<=n<='Z':
    print("Upper Case")
elif 'a'<=n<='z':
    print("lower Case")
elif '0'<=n<='9':
    print("digit")
else:
    print("spacial")
"""
    
#   write a program to check greatest  among 3 number
"""
n1 =int(input("Enter number:"))
n2 =int(input("Enter number:"))
n3 =int(input("Enter number:"))
if n1>n2 and n1>n3:
    print(f"{n1} is greatest")
elif n2>n1 and n2>n3:
    print(f"{n2} is greatest")
else:
    print(f"{n3} is greatest")
    
"""

#  find smallest among 4 number using elif
"""
n1 =int(input("Enter number 1:"))
n2 =int(input("Enter number 2:"))
n3 =int(input("Enter number 3:"))
n4 =int(input("Enter number 4:"))
if n1<n2 and n1<n3 and n1<n4:
    print(f"{n1} is smallest")
if n2<n1 and n2<n3 and n2<n4:
    print(f"{n2} is smallest")
if n3<n2 and n3<n1 and n3<n4:
    print(f"{n3} is smallest")
if n4<n2 and n4<n3 and n4<n1:
    print(f"{n4} is smallest")
else:
    print(f"no one is lowest")
"""

# given number is positive or negative or zero
"""
n =int(input("Enter number:"))
if n>0 :
    print("number is positive")
if n<0 :
    print("number is negative")
else :
    print("number is zero")
    
    """
    
#  accept number  and number divisible by 3 and 5 then print("FizzBuzz") if only 3 then print("Fizz") else 5 then print("FizzBuzz")

n =int(input("Enter number:"))
if n %3==0 and n%5==0 :
    print(f"FizzBuzz")
elif n %3==0 :
    print(f"Fizz")  
elif n%5==0 :
    print(f"Buzz")
else:
    print("wrong number")