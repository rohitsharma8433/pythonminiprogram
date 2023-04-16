print("-------------Student Report Card ----------")
name=input("Enter your Name")
school=input("Enter Your School Name ")
java=int(input("Enter your java Marks"))
c=int(input("Enter your c++ Marks"))
jsp=int(input("Enter your jsp Marks"))
Python=int(input("Enter your Python Marks"))
javascript=int(input("Enter your javascript Marks"))
go=int(input("Enter your go Marks"))

print("-------------Your Datails ----------")
print(name)
print(school)

if java <= 34:
    print (java,"/100","Grade F")

elif java <= 44:
    print (java,"/100","Grade C")
    
elif java <= 59:
    print (java,"/100","Grade B")

elif java <= 89:
    print (java,"/100","Grade A")
else:
    print (java,"/100","Grade A++")


if c <= 34:
    print (c,"/100","Grade F")

elif c <= 44:
    print (c,"/100","Grade C")
    
elif c <= 59:
    print (c,"/100","Grade B")

elif c <= 89:
    print (c,"/100","Grade A")
else:
    print (c,"/100","Grade A++")
    
    

if jsp <= 34:
    print (jsp,"/100","Grade F")

elif jsp <= 44:
    print (jsp,"/100","Grade C")
    
elif jsp <= 59:
    print (jsp,"/100","Grade B")

elif jsp <= 89:
    print (jsp,"/100","Grade A")
else:
    print (jsp,"/100","Grade A++")
    
    

if Python <= 34:
    print (Python,"/100","Grade F")

elif Python <= 44:
    print (Python,"/100","Grade C")
    
elif Python <= 59:
    print (Python,"/100","Grade B")

elif Python <= 89:
    print (Python,"/100","Grade A")
else:
    print (Python,"/100","Grade A++")
    
    

if javascript <= 34:
    print (javascript,"/100","Grade F")

elif javascript <= 44:
    print (javascript,"/100","Grade C")
    
elif javascript <= 59:
    print (javascript,"/100","Grade B")

elif javascript <= 89:
    print (javascript,"/100","Grade A")
else:
    print (javascript,"/100","Grade A++")
    
    

if go <= 34:
    print (go,"/100","Grade F")

elif go <= 44:
    print (go,"/100","Grade C")
    
elif go <= 59:
    print (go,"/100","Grade B")

elif go <= 89:
    print (go,"/100","Grade A")
else:
    print (go,"/100","Grade A++")
    
    
total= java+c+jsp+Python+javascript+go
print("Your total marks is :",total)
percent=total*100/600
print("your Percentage is",percent,"%")

if total <= 204:
    print ("Your Final Grade is : F")

elif total <= 270:
    print ("Your Final Grade is : C")
    
elif total <= 354:
    print ("Your Final Grade is : B")

elif total <= 534:
    print ("Your Final Grade is : A")
elif total <= 600:
    print ("Your Final Grade is : A++")

    
    
