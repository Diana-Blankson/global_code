def calculate():

    string=input("Choose an operator:1 add  2 subtract  3 multiply  4 divide ") 
    if string == "1":
     x=input('Enter the first number')
     y = input('Enter the second number')
     num1 = x
     num2 = y
     result =int(num1) +int(num2)
     print(result)

    elif string == "2":
     x=input('Enter the first number')
     y=input('Enter the second number')
     num1 = x
     num2 = y
     result =int(num1) - int(num2)
     print(result)



    elif string == "3":
     x=input('Enter the first number')
     y=input('Enter the second number')
     num1 = x
     num2 = y
     result =int(num1) / int(num2)
     print(result)

    elif string == "4":
     x=input('Enter the first number')
     y=input('Enter the second number')
     num1 = x
     num2 = y
     result =int(num1) * int(num2)
     print(result)
calculate()



