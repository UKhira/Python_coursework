#Part 3 - Text File (extension)
defer_credit = 0 
fail_credit = 0
pass_credit = 0
maintance = 'y'
results_range = (0, 20, 40, 60, 80, 100, 120)

file = open("credit.txt", 'w+')

def credit_pass_input():
    global pass_credit, results_range
    pass_credit = int(input("Please enter your credit at pass : "))
    while pass_credit not in (results_range):
        print("Out of Range")
        pass_credit = int(input("Please enter your credit at pass : "))
    return pass_credit
        
        
def credit_defer_input():
    global defer_credit,results_range
    defer_credit = int(input("Please enter your credit at defer : "))  
    while defer_credit not in results_range:
        print("Out of Range")
        defer_credit = int(input("Please enter your credit at defer : ")) 
    return defer_credit      
       
        
def credit_fail_input():
    global fail_credit,results_range
    fail_credit = int(input("Please enter your credit at fail : "))   
    while fail_credit not in results_range:
        print("Out of Range")
        fail_credit = int(input("Please enter your credit at fail : "))  
    return fail_credit
        
def total_check():
    global pass_credit,defer_credit,fail_credit
    while pass_credit + defer_credit + fail_credit != 120:
        print("Total Incorrect")
        credit_pass_input();
        credit_defer_input();
        credit_fail_input();


def progress_add_mark():
    print("Progress")
    file.write("%s = %s\n" %("Progress " ,credit_store))
    
        

def trailer_add_mark():
    print("Progress (module trailer)")
    file.write("%s = %s\n" %("Progress (module trailer) ",credit_store))
            

def exclude_add_mark():
    print("Exclude")
    file.write("%s = %s\n" %("Exclude ",credit_store))
                

def retriever_add_mark():
    print("Do not Progress - module retrievever")
    file.write("%s = %s\n" %("Do not progress - module retriever ",credit_store))      
        
while maintance == 'y' and maintance != 'q' :
# check credit(pass,defer,fail) and verify entered value is an integer
    try :
        credit_pass_input();

        credit_defer_input();

        credit_fail_input();

        total_check();

        credit_store = (pass_credit, defer_credit, fail_credit)
            
        if pass_credit == 120 and defer_credit == fail_credit == 0:
            progress_add_mark();
        elif pass_credit == 100 and defer_credit in(0, 20) and fail_credit in (0, 20):
            trailer_add_mark();
        elif pass_credit in (0, 20, 40) and defer_credit in (0, 20, 40) and fail_credit in (80, 100, 120) :
            exclude_add_mark();
        else:
            retriever_add_mark();

        maintance = input("Enter 'y' to continue or 'q' to quit and view results : ")      
        
    except ValueError:
        print("Integer required")

    if maintance == 'y' :
            continue;
    elif maintance == 'q' :
            #Part 2 - Lists (extensions)
            file.close()

            with open ("credit.txt") as file:
                print('\nPart 3:-\n')
                for line in file:
                    print(line.strip())

    else :
        print("Invalid Input Try Again") 
        break;
