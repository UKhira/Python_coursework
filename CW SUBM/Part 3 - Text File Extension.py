#Part 3 - Text File (extension)
defer_credit = 0        #variable to save credit at defer
fail_credit = 0         #variable to save credit at fail
pass_credit = 0         #variable to save credit at pass
maintance = 'y'         #variable for continue/end program
results_range = (0, 20, 40, 60, 80, 100, 120)       #variable to validate whether credits are in range or not

def Purpose_of_Program():               #display purpose of program using docstring
    '''This is a program created to predict progression outcomes at the end of each academic year in a certain University  
    And this is its Third Part with Text File as extension'''

file = open("credit.txt", 'w+')                 #create a(If doesn't exists)/or open the existing text file to store data

#by using w+ it will store current data to text file, user can look into if he/she needed, and by the time program execute again it will remove current data and store new data

def credit_pass_input():                     #let user to input credit at pass, verify it within result range
    global pass_credit, results_range
    pass_credit = int(input("Please enter your credit at pass : "))
    while pass_credit not in (results_range):
        print("Out of Range")
        pass_credit = int(input("Please enter your credit at pass : "))
    return pass_credit
        
        
def credit_defer_input():                   #let user to input credit at defer, verify it within result range
    global defer_credit,results_range
    defer_credit = int(input("Please enter your credit at defer : "))  
    while defer_credit not in results_range:
        print("Out of Range")
        defer_credit = int(input("Please enter your credit at defer : ")) 
    return defer_credit      
       
        
def credit_fail_input():                    #let user to input credit at fail, verify it within result range
    global fail_credit,results_range
    fail_credit = int(input("Please enter your credit at fail : "))   
    while fail_credit not in results_range:
        print("Out of Range")
        fail_credit = int(input("Please enter your credit at fail : "))  
    return fail_credit
        
def total_check():                              #check whether the total is correct (=120), unless ask user to input again
    global pass_credit,defer_credit,fail_credit
    while pass_credit + defer_credit + fail_credit != 120:
        print("Total Incorrect")
        credit_pass_input();
        credit_defer_input();
        credit_fail_input();


def progress_add_mark():            #print "Progress" if given condition satisfies and save results in text file under "Progress"
    print("Progress")
    file.write("%s = %s\n" %("Progress                           ",credit_store))
    
        

def trailer_add_mark():             #print "Progress (module trailer)" if given condition satisfies and save results in text file under "Progress (module trailer)"
    print("Progress (module trailer)")
    file.write("%s = %s\n" %("Progress (module trailer)          ",credit_store))
            

def exclude_add_mark():             #print "Exclude" if given condition satisfies and save results in text file under "Exclude"
    print("Exclude")
    file.write("%s = %s\n" %("Exclude                            ",credit_store))
                

def retriever_add_mark():           #print "Do not progress - module retriever" if given condition satisfies and save results in text file under "Do not Progress - module retriever"
    print("Do not Progress - module retrievever")
    file.write("%s = %s\n" %("Do not progress - module retriever ",credit_store))   

help(Purpose_of_Program)             #to display docstring at the start(to explain user, what is this program made for)
        
while maintance == 'y' and maintance != 'q' :           #continue process
# check credit(pass,defer,fail) and verify entered value is an integer
    try :
        #calling user defined functions
        credit_pass_input();

        credit_defer_input();

        credit_fail_input();

        total_check();

        #define which data to save under credit_store variable 
        credit_store = (pass_credit, defer_credit, fail_credit)
            
        #check and save prediction for each results
        if pass_credit == 120 and defer_credit == fail_credit == 0:
            progress_add_mark();
        elif pass_credit == 100 and defer_credit in(0, 20) and fail_credit in (0, 20):
            trailer_add_mark();
        elif pass_credit in (0, 20, 40) and defer_credit in (0, 20, 40) and fail_credit in (80, 100, 120) :
            exclude_add_mark();
        else:
            retriever_add_mark();

        maintance = input("Enter 'y' to continue adding credits or 'q' to quit and view results : ")      #ask whether user want to continue or abort
        
    except ValueError:                  #if value not is an integer
        print("Integer required")

    if maintance == 'y' :
            continue;
    elif maintance == 'q' :
            #Part 3 - Text File (extensions)
            file.close()                #save data and close file

            with open ("credit.txt") as file:               #open file again as read mode
                print('\nPart 3:-\n')                       #print stored data line by line
                for line in file:
                    print(line.strip())

    else :
        print("Invalid Input Try Again") 
