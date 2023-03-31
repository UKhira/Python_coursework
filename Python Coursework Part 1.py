maintance = 'y'
c_pass = c_fail = c_defer = 0
count_progress = count_trailer = count_retriever = count_excluded = 0
student_count = 0
while maintance == 'y' and maintance != 'q' :
# check credit(pass,defer,fail) and verify entered value is an integer
    try :
        c_pass = int(input("Please enter your credit at pass : "))
        if c_pass in (0, 20, 40, 60, 80, 100, 120):
            c_defer = int(input("Please enter your credit at defer : "))
            if c_defer in (0, 20, 40, 60, 80, 100, 120):
                c_fail = int(input("Please enter your credit at fail : "))
                if c_fail in (0, 20, 40, 60, 80, 100, 120):
                    if c_pass + c_defer + c_fail != 120:
                        print("Total Incorrect") 
                    else :
                        if c_pass == 120 and c_defer == c_fail == 0:
                            print("Progress")
                            count_progress = count_progress + 1
                        elif c_pass == 100 and c_defer in(0, 20) and c_fail in (0, 20):
                            print("Progress (module trailer)")
                            count_trailer = count_trailer + 1
                        elif c_pass in (0, 20, 40) and c_defer in (0, 20, 40) and c_fail in (80, 100, 120) :
                            print("Exclude")
                            count_excluded = count_excluded + 1
                        else :
                            print("Do not progress - module retriever")
                            count_retriever = count_retriever + 1
                        student_count = student_count + 1
                        maintance = input("Enter 'y' to continue or 'q' to quit and view results : ")                                   
                else :
                    print("Out of Range")
            else:
                print("Out of Range")
        else:
            print("Out of Range")
    except ValueError:
        print("Integer required")
#prediction starts here
    if maintance == 'y' :
        continue;
    elif maintance == 'q' :
#Histogram starts here
        print('')
        print("-----------------------------------------------------------------")
        print("Histogram")
        print("Progress ",count_progress," : " ,end ='')
        for asterik_pro in range (0, count_progress):
            print("*" ,end ='')
        print("\nTrailer  ",count_trailer," : ",end='')
        for asterik_tra in range(0,count_trailer):
            print("*",end='')
        print("\nRetriever",count_retriever," : ",end='')
        for asterik_ret in range (0,count_retriever):
            print("*",end='')
        print("\nExcluded ",count_excluded," : ",end='')
        for asterik_exc in range (0,count_excluded):
            print("*",end='')
        print("\n""\n",student_count,"outcomes in total\n-----------------------------------------------------------------")
        break;
    
    
#This part was made for to test and adjust spacing   
#Original :-     
# Progress  1  : *
# Trailer 2  : **
# Retriever  0  :
# Excluded  0  :

#adjusted :
# Progress  1  : *
# Trailer   2  : **
# Retriever 0  :
# Excluded  0  :