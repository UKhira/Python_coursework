#Part 2 - List Extension
import re
defer_credit = 0            #variable to save credit at defer
fail_credit = 0             #variable to save credit at fail
pass_credit = 0             #varable to save credit at pass
maintance = 'y'             #variable for continue/end program
results_range = (0, 20, 40, 60, 80, 100, 120)            #variable to validate whether credits are in range or not
iter_1 = iter_2 = iter_3 = iter_4 = 0           #for the iteration process of progress, trailer, retriever, exclude(in order)
list_excluded = []              #list for save exclude result
list_retriever = []             #list for save retriever result
list_module = []                #list for save trailer result
list_progress = []              #list for save progress result

def Purpose_of_Program():                #display purpose of program using docstring
    '''This is a program created to predict progression outcomes at the end of each academic year in a certain University  
    And this is its 2nd Part with List as extension'''

def credit_pass_input():                #let user to input credit at pass, verify it within result range
    global pass_credit, results_range
    pass_credit = int(input("Please enter your credit at pass : "))
    while pass_credit not in (results_range):
        print("Out of Range")
        pass_credit = int(input("Please enter your credit at pass : "))
    return pass_credit
        
        
def credit_defer_input():               #let user to input credit at defer, verify it within result range
    global defer_credit,results_range
    defer_credit = int(input("Please enter your credit at defer : "))  
    while defer_credit not in results_range:
        print("Out of Range")
        defer_credit = int(input("Please enter your credit at defer : ")) 
    return defer_credit      
       
        
def credit_fail_input():                #let user to input credit at fail, verify it within result range
    global fail_credit,results_range
    fail_credit = int(input("Please enter your credit at fail : "))   
    while fail_credit not in results_range:
        print("Out of Range")
        fail_credit = int(input("Please enter your credit at fail : "))  
    return fail_credit

        
def total_check():                      #check whether the total is correct (=120), unless ask user to input again
    global pass_credit,defer_credit,fail_credit
    while pass_credit + defer_credit + fail_credit != 120:
        print("Total Incorrect")
        credit_pass_input();
        credit_defer_input();
        credit_fail_input();


def progress_add_mark():                           #print "Progress" if given condition satisfies and save results to progress list
    print("Progress")
    list_progress.extend([pass_credit,',',defer_credit,',',fail_credit])
        

def trailer_add_mark():                            #print "Progress (module trailer)" if given condition satisfies and save results to trailer list
    print("Progress (module trailer)")
    list_module.extend([pass_credit,',',defer_credit,',',fail_credit])
            

def exclude_add_mark():                            #print "Exclude" if given condition satisfies and save results to exclude list
    print("Exclude")
    list_excluded.extend([pass_credit,',',defer_credit,',',fail_credit])
                

def retriever_add_mark():                           #print "Do not Progress - module retriever" if given condition satisfies and save results to retriever list
    print("Do not progress - module retriever")
    list_retriever.extend([pass_credit,',',defer_credit,',',fail_credit])  

help(Purpose_of_Program)                #to display docstring at the start(to explain user, what is this program made for)
        
while maintance == 'y' and maintance != 'q' :   #continue process
# check credit(pass,defer,fail) and verify entered value is an integer
    try :
        #calling user defined functions
        credit_pass_input();

        credit_defer_input();

        credit_fail_input();

        total_check();
            
        #check and save prediction for each results
        if pass_credit == 120 and defer_credit == fail_credit == 0:
            progress_add_mark();
        elif pass_credit == 100 and defer_credit in(0, 20) and fail_credit in (0, 20):
            trailer_add_mark();
        elif pass_credit in (0, 20, 40) and defer_credit in (0, 20, 40) and fail_credit in (80, 100, 120) :
            exclude_add_mark();
        else:
            retriever_add_mark();
              
        maintance = input("Enter 'y' to continue adding credits or 'q' to quit and view results : ")       #ask whether user want to continue or abort
        
    except ValueError:              #if value not is an integer
        print("Integer required")

    if maintance == 'y' :               #continue program
            continue;
    elif maintance == 'q' :             #quit program
            #Part 2 - Lists (extensions)

            print("\nPart 2")

            while iter_1 < len(list_progress):                  #print stored data on progress list
                print("\nProgress         - ", end = '')
                for count_list in (list_progress[iter_1:iter_1+5]) :    #pass_credit,fail_credit,defer_credit(3) + 2 commas(2) = 5
                    print(count_list, end=' ')
                iter_1 = iter_1 + 5

            while iter_2 < len(list_module):                    #print stored data on progress list
                print("\nModule trailer   - ", end =' ')
                for count_list in (list_module[iter_2:iter_2+5]) :      #pass_credit,fail_credit,defer_credit(3) + 2 commas(2) = 5
                    print(count_list, end=' ')
                iter_2 = iter_2 + 5

            while iter_3 < len(list_retriever):                 #print stored data on retriever list
                print("\nModule retriever - ", end = ' ')
                for count_list in (list_retriever[iter_3:iter_3+5]) :    #pass_credit,fail_credit,defer_credit(3) + 2 commas(2) = 5
                    print(count_list, end=' ')
                iter_3 = iter_3 + 5
                
            while iter_4 < len(list_excluded):                  #print stored data on exclude list
                print("\nExclude          - ", end = ' ')
                for count_list in (list_excluded[iter_4:iter_4+5]) :     #pass_credit,fail_credit,defer_credit(3) + 2 commas(2) = 5
                    print(count_list, end=' ')
                iter_4 = iter_4 + 5
    else :
        print("Invalid Input Try Again") 