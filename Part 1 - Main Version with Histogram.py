#Part 1 - Main Version
import re
defer_credit = 0        #variable to save credit at defer
fail_credit = 0         #variable to save credit at fail
pass_credit = 0         #varable to save credit at pass
maintance = 'y'         #variable for continue/end program
count_progress = count_trailer = count_retriever = count_excluded = 0       #variables to save Progress, Trailer, Retriever, Exclude result counts
student_count = 0           #variable to save student count(to check how many results)
results_range = (0, 20, 40, 60, 80, 100, 120)       #variable to validate whether credits are in range or not

def Purpose_of_Program():               #display purpose of program using docstring
    '''This is a program created to predict progression outcomes at the end of each academic year in a certain University  
    And this is its Main Part with Histogram'''

def credit_pass_input():                #let user to input credit at pass, verify it within result range
    global pass_credit, results_range
    pass_credit = int(input("Please enter your credit at pass : "))
    while pass_credit not in (results_range):
        print("Out of Range")
        pass_credit = int(input("Please enter your credit at pass : "))     #if it isn't within range prompt till user input valid range
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


def progress_add_mark():                #save credits under "Progress", and increase progress count by one for each result saved under progress             
    global count_progress
    print("Progress")
    count_progress = count_progress + 1
    return(count_progress)
        

def trailer_add_mark():                #save credits under "Progress (module trailer)", and increase trailer count by one for each result saved under trailer
    global count_trailer
    print("Progress (module trailer)")
    count_trailer = count_trailer + 1
    return(count_trailer)
            

def exclude_add_mark():                #save credits under "Exclude", and increase exclude count by one for each result saved under exclude
    global count_excluded
    print("Exclude")
    count_excluded = count_excluded + 1
    return count_excluded
                

def retriever_add_mark():               #save credits under "Do not progress - module retriever", and increase retriever count by one for each result saved under retriever
    global count_retriever
    print("Do not progress - module retriever")
    count_retriever = count_retriever + 1
    return(count_retriever)
        
help(Purpose_of_Program)                #to display docstring at the start(to explain user, what is this program made for)
        
while maintance == 'y' and maintance != 'q' :       #continue process
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
              
        student_count = student_count + 1
        maintance = input("Enter 'y' to continue adding credits or 'q' to quit and view results : ")        #ask whether user want to continue or abort  
        
    except ValueError:              #if value not is an integer
        print("Integer required")

    if maintance == 'y' :           #continue program
            continue;
    elif maintance == 'q' :         #quit program
    #Histogram starts here
            print('')
            print("-----------------------------------------------------------------")
            print("Histogram")

            #(Asterik count=Student count)
            print("\nProgress ",count_progress," : " ,end ='')
            for asterik_progress in range (0, count_progress):      #Asteriks for progress count 
                print("*" ,end ='')

            print("\nTrailer  ",count_trailer," : ",end='')
            for asterik_trailer in range(0,count_trailer):          #Asteriks for trailer count
                print("*",end='')

            print("\nRetriever",count_retriever," : ",end='')
            for asterik_retriever in range (0,count_retriever):      #Asteriks for retriever count
                print("*",end='')

            print("\nExcluded ",count_excluded," : ",end='')
            for asterik_exclude in range (0,count_excluded):        #Asteriks for exclude count
                print("*",end='')

            print("\n""\n",student_count,"outcomes in total\n-----------------------------------------------------------------")        #print number of total outcomes

    else :
        print("Invalid Input Try Again") 
        