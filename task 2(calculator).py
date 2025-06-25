num1=float(input("Enter the first number:"))
num2=float(input("enter the second number:"))
while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.modulo")
    print("6.EXIT")
    choice=input("whats you choice?")
    
    if choice=="1":
        result=num1+num2
        print("Result=",result)
        
    elif choice=="2":
        result=num1-num2
        print("Result = ",result)
        
    elif choice=="3":
        result=num1*num2
        print("Result = ",result)
        
    elif choice=="4":
        if num2 !=0:
            result=num1/num2
            print("Result = ",result)
        else:
            print("Division can't be done by Zero")
        
    elif choice=="5":
        if num2!=0:
            result=num1%num2
            print("Result = ",result)
        else:
            print("modulo cannot be done by Zero")
        
    elif choice=="6":
        print("EXIT")
        
    else:
        print("seems like its a invalid option")
    