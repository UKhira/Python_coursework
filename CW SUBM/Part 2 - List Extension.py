#Part 1 - Main Version
import re
defer_credit = 0 
fail_credit = 0
pass_credit = 0
maintance = 'y'
student_count = 0
results_range = (0, 20, 40, 60, 80, 100, 120)
iter_1 = iter_2 = iter_3 = iter_4 = 0
list_excluded = []
list_retriever = []
list_module = []
list_progress = []

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
    list_progress.extend([pass_credit,defer_credit,fail_credit])
        

def trailer_add_mark():
    print("Progress (module trailer)")
    list_module.extend([pass_credit,defer_credit,fail_credit])
            

def exclude_add_mark():
    print("Exclude")
    list_excluded.extend([pass_credit,defer_credit,fail_credit])
                

def retriever_add_mark():
    print("Do not progress - module retriever")
    list_retriever.extend([pass_credit,defer_credit,fail_credit])        
        
while maintance == 'y' and maintance != 'q' :
# check credit(pass,defer,fail) and verify entered value is an integer
    try :
        credit_pass_input();

        credit_defer_input();

        credit_fail_input();

        total_check();
            
        if pass_credit == 120 and defer_credit == fail_credit == 0:
            progress_add_mark();
        elif pass_credit == 100 and defer_credit in(0, 20) and fail_credit in (0, 20):
            trailer_add_mark();
        elif pass_credit in (0, 20, 40) and defer_credit in (0, 20, 40) and fail_credit in (80, 100, 120) :
            exclude_add_mark();
        else:
            retriever_add_mark();
              
        student_count = student_count + 1
        maintance = input("Enter 'y' to continue or 'q' to quit and view results : ")      
        
    except ValueError:
        print("Integer required")

    if maintance == 'y' :
            continue;
    elif maintance == 'q' :
            #Part 2 - Lists (extensions)

            print("\nPart 2")

            while iter_1 < len(list_progress):          
                print("\nProgress - ", end = ' ')
                for count_list in (list_progress[iter_1:iter_1+2]) :
                    print(count_list, end=', ')
                else:
                    print(count_list, end=' ')   #for leaving final element without a comma
                iter_1 = iter_1 + 3

            while iter_2 < len(list_module):
                print("\nModule trailer - ", end =' ')
                for count_list in (list_module[iter_2:iter_2+2]) :
                    print(count_list, end=', ')
                else:
                    print(count_list, end=' ')
                iter_2 = iter_2 + 3

            while iter_3 < len(list_retriever):
                print("\nModule retriever - ", end = ' ')
                for count_list in (list_retriever[iter_3:iter_3+2]) :
                    print(count_list, end=', ')
                else:
                    print(count_list, end=' ')
                iter_3 = iter_3 + 3
                
            while iter_4 < len(list_excluded):
                print("\nExclude - ", end = ' ')
                for count_list in (list_excluded[iter_4:iter_4+2]) :
                    print(count_list, end=', ')
                else:
                    print(count_list, end=' ')
                iter_4 = iter_4 + 3
    else :
        print("Invalid Input Try Again") 
        break;