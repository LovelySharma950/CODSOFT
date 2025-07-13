def calc():
    print ("-----WELCOME TO THE Calculator APP------")
    num1 = int(input("Enter number 1: ")) 
    num2 = int(input("Enter number 2: ")) 

    while True:
        operation=int(input("Enter 1-Addition\n2-Subtraction\n3-Multiplication\n4-Division\n5-Continue\n6-Exit/Stop\n"))
        if operation ==1:
            soln = num1 + num2
            print(f"The addition is: {soln}")

        elif  operation == 2:
            soln = num1 - num2
            print(f"The subtraction is: {soln}")
        elif operation ==3:
            soln = num1 * num2
            print(f"The multiplication is: {soln}")
        elif operation == 4:
            soln = num1 / num2
            print(f"The division is: {soln}")

        elif operation == 5:
             num3 = int(input("Enter new number: "))
             num1 = soln
             num2 = num3
             operation

        elif operation == 6:
                print("Closing  the program....")
                break
        else:
            print("Invalid Input")

calc()



            
                   









