print("------------- ------  --------Online Exam System Useing Python ---------- ------- ------")
user="Admin"
password="Admin@1234"
no=input("Are you want to  Join the exam  :  ")
if no == "no":
    print("please select yes for Countineu For Exam ")

elif no =="yes":
    print("-------------")
    print("continue your exam : ")
    print("-------------")
    say=input("Enter your Username : ")
    say1=input("Enter Password : ")
    print("-------------")
    if(say == user and say1 ==password):
        select=input("please select subject math1 or python : ")
        if(select == "math1"):
            print("Question number 1 ")
            print("-------------")
            print("1 HCF of 8 ,9 ,25 is ")
            print("Your Option is ")
            print("(a) 8")
            print("(b) 9")
            print("(c) 25")
            print("(d) 1")
            print("-------------")
            ans=input("select Your Option ")
            print("-------------")
            if(ans == "d"):
                print("Selected Answer is ",ans," is Correct")
                print("-------------")
                print("Admin Your Result is Pass")
            else:
                print("Selected Answer is ",ans," is InCorrect")
                print("-------------")
                print("Admin Your Result is Fail")
        elif(select == "python" ):
             print("1. Who developed Python Programming Language?")
             print("Your Option is ")
             print("(a) a) Wick van Rossum")
             print("(b) Rasmus Lerdorf")
             print("(c) Guido van Rossum")
             print("(d) Niene Stom")
             print("-------------")
             answer=input("select Your Option ")
             if(answer =="c"):
                 print("Selected Answer is ",answer," is Correct")
                 print("-------------")
                 print("Admin Your Result is Pass")
             else:
                  print("-------------")
                  print("Selected Answer is ",answer," is InCorrect")
                  print("-------------")
                  print("Admin Your Result is Fail")
             
        else:
             print("select only math1 and Python")
            
             
            
                 
                            
        
    else:
        print("please Enter valid username and password")
else:
    print("please enter yes or no only ")
