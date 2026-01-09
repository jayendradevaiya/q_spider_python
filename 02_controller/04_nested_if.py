#  check  if a given character is vowel or not
"""
n =input("Enter character:")
if 'A'<= n <='Z' or 'a'<= n <='z':
    if n in 'AEIOUaeiou':
        print(f"{n} is vowel")
    else:
        print(f"{n} is not a vowel")
else:
    print(f"{n} is not uppercase or lowercase")
    
"""

#  login into instagram by entering currect username and pass
"""
user = "jay_21"
pW = "Jay@21"
username = input("enter your username :")
password = input("enter your password :")

if username in user:
    if password in pW:
        print(f"{username} is logged")
    else:
        print("enter currect password")
else:
    print("enter valid username")
        """
        
#  find greatest among 3 number using nested if
"""
n1 =int(input("Enter number 1 :"))
n2 =int(input("Enter number 2 :"))
n3 =int(input("Enter number 3 :"))

if n1>n2:
    if n1>n3:
        print(f"{n1} is greatest")
    else:
        print(f"{n3} is greatest")
else:
    if n2>n3:
        print(f"{n2} is greatest")
    else:
        print(f"{n3} is greatest")
        
"""

#  find greatest among 4 number using nested if


"""
n1 =int(input("Enter number 1 :"))
n2 =int(input("Enter number 2 :"))
n3 =int(input("Enter number 3 :"))
n4 =int(input("Enter number 4 :"))

if n1>n2:
    if n1>n3:
        if n1>n4:
            print(f"{n1} is greatest")
        else:
            print(f"{n4} is greatest")
    else:
        print(f"{n3} is greatest")
else:
    if n2>n3:
        if n2>n4:
            print(f"{n2} is greatest")
        else:
            print(f"{n4} is greatest")  
    else:
        if n3>n4:
            print(f"{n3} is greatest")
        else:
            print(f"{n4} is greatest")
"""

