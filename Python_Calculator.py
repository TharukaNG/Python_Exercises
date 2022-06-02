def Addition(a,b):
    print(a, "+", b, "=", a+b)

def Substraction(a,b):
    print(a, "-", b, "=", a-b)

def Division(a,b):
    try:
        print(a, "/", b, "=", a/b)
    except:
        print("float division by zero")
        print(a,"/",b,"= None")


def Multiplication(a,b):
    print(a, "*", b, "=", a*b)

def Power(a,b):
    print(a, "^", b, "=", a^b)

def Remainder(a,b):
    print(a, "%", b, "=", a%b)

while True  :
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)

    if(choice == "#"):
        print("Done. Terminating")
        exit()

    if(choice not in ('+','-','*','/','^','%','#')):
        print("Unrecognized operation")

    elif(choice in ('+','-','*','/','^','%')):

        num_1 = input("Enter first number: ")
        print(num_1)

        if(num_1 == '#'):
            print("Done. Terminating")
            exit()
        else:           
            try:
                num1 = float(num_1)
            except:
                continue#print("Not a valid number,please enter again")

        num_2 = input("Enter second number: ")
        print(num_2)

        if(num_2 == '#'):
            print("Done. Terminating")
            exit()
        else: 
            try:
                num2 = float(num_2)
            except:
                continue#print("Not a valid number,please enter again")
        
        if(choice == "+"):
            Addition(num1,num2)
            #exit()

        elif(choice == "-"):
            Substraction(num1,num2)
            #exit()

        elif(choice == "*"):
            Multiplication(num1,num2)
            #exit()

        elif(choice == "/"):
            Division(num1,num2)
            #exit()

        elif(choice == "^"):
            Power(num1,num2)
            #exit()

        elif(choice == "%"):
            Remainder(num1,num2)
            #exit()
