#Attempted this as seperate program, without previously used functions and methods

#Part 4 : Dictionary (Seperate Program)
marks = {}                      #Dictionary to save Marks
maintance = 'y'                #variable value for continue/end program
result_range = (0,20,40,60,80,100,120)          #variable for result range

while maintance=='y':
    student_id = input("Enter student ID: ")            #ask user to input student ID

    try:
        pass_credit = int(input("Enter Credit at Pass: "))     #ask user to input pass credit
        if pass_credit in result_range:                        #range validation
            defer_credit = int(input("Enter Credit at Defer: "))        #ask user to input defer credit
            
            if defer_credit in result_range:                            #range validation
                fail_credit = int(input("Enter Credit at Fail: "))      #ask user to input fail credit
                
                if fail_credit in result_range:                         #range validation

                    if pass_credit + defer_credit + fail_credit == 120:            #total validation

                        if pass_credit == 120 and defer_credit == fail_credit == 0:     #Progress credit
                            status = "Progress -"
                        
                        elif pass_credit == 100 and defer_credit in(0, 20) and fail_credit in (0, 20):          #Trailer credit
                            status = "Progress (module trailer) -"
                       
                        elif pass_credit in (0, 20, 40) and defer_credit in (0, 20, 40) and fail_credit in (80, 100, 120) :     #Exclude credit
                            status = "Exclude -"
                        
                        else:                                   #Retriever Credit
                            status = "Module Retriever -"               
                        
                        print(status)                               #Display outcome for each marks(at first)
                        
                        marks[student_id] = status, pass_credit, defer_credit, fail_credit          #save values to dictionary

                        maintance = input("Enter 'y' to continue, 'q' to Quit: ")                   #ask user want to continue/abort

                    else:
                        print("Total Incorrect")
                else:
                    print("Out of Range")
            else:
                print("Out of Range")
        else:
            print("Out of Range")

    except ValueError:                      #Integer Validation
        print("Integer Required")

if maintance == 'q':
    for dic_items in marks.items():             #Access items on dictionary
        print(dic_items)

else :
    print("Invalid Input")

