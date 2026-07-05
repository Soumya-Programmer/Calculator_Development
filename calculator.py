def main ():
    x= int(input("What X ?"))
    y= int(input("What Y ?"))
    print("Operation to perform")
    z=input(" + , - , * , % , /")
    match z:
        case"+":
            addition(x,y)
        case "-":
            substraction(x,y)
        case "*":
            multiplication(x,y)
        case "/":
            division(x,y)
        case "%":
            modulus(x,y)
        case _:
            print("Error! \n Plz ,enter a Correct a Symbol.")
             
def addition(a,b):
    print("Addition :",a+b)
def substraction(a,b):
    print("Subtraction :",a-b)
def multiplication(a,b):
    print("Multiplication :",a*b)
def division(a,b):
    if (b!=0):
        z=a/b
        print("Quotient :",f"{z:4f}")
def modulus(a,b):
    if(b!=0):
        z=a%b
        print("Remainder :",z)

main()        