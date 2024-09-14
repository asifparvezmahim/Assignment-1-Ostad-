def addition(num1,num2):
    result=float(num1+num2)
    result=f"{result:.2f}"
    return result


def subtract(num1,num2):
    result = float(num1-num2)
    result=f"{result:.2f}"
    return result

def multiply(num1,num2):
    result = float(num1*num2)
    result=f"{result:.2f}"
    return result

def division(num1,num2):
     try:
          result=float(num1/num2)
          result=f"{result:.2f}"
          return result
     except ZeroDivisionError as e:
          print("Error Type: ",e)
          print("User Guide: Second value cannot be 0")

def modulus(num1,num2):
        try:
            result=float(num1%num2)
            result=f"{result:.2f}"
            return result
        except ZeroDivisionError as e:
             print("Error Type: ",e)
             print("User Guide: Second value cannot be 0")
     



print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

user_input=int(input("Enter Choice: 1/2/3/4/5 : "))

if user_input==1:
    first_number = input("Enter First Number: ")
    second_number = input("Enter Second Number: ")
    try:
        first_number=float(first_number)
        second_number=float(second_number)
        result=addition(first_number,second_number)
        print(first_number ,"+", second_number,"=",result)
    except:
         print("Error: Enter Numeric Input")
         

elif user_input==2:
    first_number = input("Enter First Number: ")
    second_number = input("Enter Second Number: ")
    try:
        first_number=float(first_number)
        second_number=float(second_number)
        result=subtract(first_number,second_number)
        print(first_number ,"-", second_number,"=",result)
    except:
         print("Error: Enter Numeric Input")

elif user_input==3:
    first_number = input("Enter First Number: ")
    second_number = input("Enter Second Number: ")
    try:
        first_number=float(first_number)
        second_number=float(second_number)
        result=multiply(first_number,second_number)
        print(first_number ,"X", second_number,"=",result)
    except:    
        print("Error: Enter Numeric Input")

    
elif user_input==4:
        first_number = input("Enter First Number: ")
        second_number = input("Enter Second Number: ")
        try:
            first_number=float(first_number)
            second_number=float(second_number)
            result=division(first_number,second_number)
            if result!=None:
                 print(first_number ,"/", second_number,"=",result)
        except:
             print("Error: Enter Numeric Input")
             
             

elif user_input==5:
        first_number = input("Enter First Number: ")
        second_number = input("Enter Second Number: ")
        try:
            first_number=float(first_number)
            second_number=float(second_number)
            result=modulus(first_number,second_number)
            if result!=None:
                  print(first_number ,"%", second_number,"=",result)
        except:
             print("Error: Enter Numeric Input")

else:
     print("Input Valid Number")
