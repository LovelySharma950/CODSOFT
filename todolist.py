def task():
    task = [] #empty list 
    print ("-----WELCOME TO THE MANAGEMENT APP------")

    total_task = int(input("Enter how many task you want to add="))
    for i in range(1,total_task+1):
        task_name= input(f"Enter task {i}=") #enter task 3=
        task.append(task_name)
    print(f"Today's tasks are\n{task}")
    while True:
        operation=int(input("Enter 1-Add\n2-update\n3-Delete\n4-view\n5-Exit/Stop\n"))

        #For creating new task
        if operation ==1:
            add=input("Enter task you want to add=")
            task.append(add)
            print(f" Task{add} has been successfully added....")

        #For updating existing task
        elif  operation == 2:
            updated_val=input("Enter the task name you want to update =")
            if updated_val in task:
                up=input("Enter new task=")
                ind=task.index(updated_val) #2
                task[ind] = up
                print(f"updated task {up}")

        #For deletion of task
        elif operation ==3:
            del_val=input("Which task you want to delete =")
            if del_val in task:
                ind = task.index(del_val)
                del task[ind]
                print(f"Task {del_val} has been deleted....")

        #For viewing all tasks
        elif operation == 4:
                print(f" Total Task= {task}")

        #For Closing the program
        elif operation == 5:
                print("Closing  the program....")
                break
        else:
            print("Invalid Input")

task()



            
                   









