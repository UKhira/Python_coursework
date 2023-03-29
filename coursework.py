maintance = 'y'
c_pass = c_fail = c_defer = 0
while maintance == 'y' and maintance != 'q' :
# check credit(pass,defer,fail) and verify entered value is an integer
    try :
        c_pass = int(input("Please enter your credit at pass : "))
        if c_pass in (0, 20, 40, 60, 80, 100, 120):
            None
        else :
            print("Out of Range")
            break;
            
        c_defer = int(input("Please enter your credit at defer : "))
        if c_defer in (0, 20, 40, 60, 80, 100, 120):
            None
        else:
            print("Out of Range")
            break;
        c_fail = int(input("Please enter your credit at fail : "))
        if c_fail in (0, 20, 40, 60, 80, 100, 120):
            None
        else:
            print("Out of Range")
            break;
        if c_pass + c_defer + c_fail != 120:
            print("Total Incorrect")
            break;
        else:
            continue;
    except ValueError:
        print("Integer required")
    maintance = input("Enter 'y' to continue or 'q' to quit and view results : ")
    if maintance != 'y' or maintance != 'q' :
        print("Invalid input please enter 'y' to continue or 'q' to quit")
    