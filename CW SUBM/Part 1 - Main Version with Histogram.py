#Part 1 - Main Version
import re
defer_credit = 0 
fail_credit = 0
pass_credit = 0
maintance = 'y'
count_progress = count_trailer = count_retriever = count_excluded = 0
student_count = 0
results_range = (0, 20, 40, 60, 80, 100, 120)
iter_1 = iter_2 = iter_3 = iter_4 = 0

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
    global count_progress
    print("Progress")
    count_progress = count_progress + 1
    return(count_progress)
        

def trailer_add_mark():
    global count_trailer
    print("Progress (module trailer)")
    count_trailer = count_trailer + 1
    return(count_trailer)
            

def exclude_add_mark():
    global count_excluded
    print("Exclude")
    count_excluded = count_excluded + 1
    return count_excluded
                

def retriever_add_mark():
    global count_retriever
    print("Do not progress - module retriever")
    count_retriever = count_retriever + 1
    return(count_retriever)
        
        
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
    #Histogram starts here
            print('')
            print("-----------------------------------------------------------------")
            print("Histogram")

            print("\nProgress ",count_progress," : " ,end ='')
            for asterik_progress in range (0, count_progress):
                print("*" ,end ='')

            print("\nTrailer  ",count_trailer," : ",end='')
            for asterik_trailer in range(0,count_trailer):
                print("*",end='')

            print("\nRetriever",count_retriever," : ",end='')
            for asterik_retriever in range (0,count_retriever):
                print("*",end='')

            print("\nExcluded ",count_excluded," : ",end='')
            for asterik_exclude in range (0,count_excluded):
                print("*",end='')

            print("\n""\n",student_count,"outcomes in total\n-----------------------------------------------------------------")

    else :
        print("Invalid Input Try Again") 
        break;