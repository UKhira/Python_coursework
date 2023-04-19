#Part 4 : Dictionary (Seperate Program)
marks = {}                      #Dictionary to save Marks
maintance = 'y'                #variable value for continue/end program
results_range = (0,20,40,60,80,100,120)          #variable for result range
pass_credit = defer_credit = fail_credit = 0


def Purpose_of_Program():               #display purpose of program using docstring
    '''This is a program created to predict progression outcomes at the end of each academic year in a certain University  
    And this is its Fourth Part with Dictionary as Seperate Program'''

def credit_pass_input():                     #let user to input credit at pass, verify it within result range
    global pass_credit, results_range
    pass_credit = int(input("Please enter your credit at pass : "))
    while pass_credit not in (results_range):
        print("Out of Range")
        pass_credit = int(input("Please enter your credit at pass : "))     #if it isn't within range prompt till user input valid range
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

help(Purpose_of_Program)             #to display docstring at the start(to explain user, what is this program made for)
        
while maintance=='y':
    student_id = input("Enter student ID: ")            #ask user to input student ID

    try:
                
        credit_pass_input();

        credit_defer_input();          
          
        credit_fail_input();

        if pass_credit + defer_credit + fail_credit == 120:                                 #total validation

            if pass_credit == 120 and defer_credit == fail_credit == 0:                     #Progress credit
                status = "Progress -"
                        
            elif pass_credit == 100 and defer_credit in(0, 20) and fail_credit in (0, 20):          #Trailer credit
                status = "Progress (module trailer) -"
                       
            elif pass_credit in (0, 20, 40) and defer_credit in (0, 20, 40) and fail_credit in (80, 100, 120) :     #Exclude credit
                status = "Exclude -"
                        
            else:                                   #Retriever Credit
                status = "Module Retriever -"               
                        
            print(status)                               #Display outcome for each marks(at first)
                        
            marks[student_id] = status, pass_credit, defer_credit, fail_credit          #save values to dictionary

            maintance = input("Enter 'y' to continue adding credits, or 'q' to Quit and view result: ")                   #ask user want to continue/abort

        else:
            print("Total Incorrect")
            credit_pass_input();
            credit_defer_input();
            credit_fail_input();


    except ValueError:                      #Integer Validation
        print("Integer Required")

if maintance == 'q':
    for dic_items in marks.items():             #Access items on dictionary
        print(dic_items)

else :
    print("Invalid Input")

