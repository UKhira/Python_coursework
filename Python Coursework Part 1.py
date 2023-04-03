#Part 1 - Main Version
maintance = 'y'
c_pass = c_fail = c_defer = 0
count_progress = count_trailer = count_retriever = count_excluded = 0
student_count = 0
results_range = (0, 20, 40, 60, 80, 100, 120)
iter_1 = iter_2 = iter_3 = iter_4 = 0
l_excluded = []
l_retriever = []
l_module = []
l_progress = []
while maintance == 'y' and maintance != 'q' :
# check credit(pass,defer,fail) and verify entered value is an integer
    try :
        c_pass = int(input("Please enter your credit at pass : "))
        if c_pass in results_range:
            c_defer = int(input("Please enter your credit at defer : "))
            if c_defer in results_range:
                c_fail = int(input("Please enter your credit at fail : "))
                if c_fail in results_range:
                    if c_pass + c_defer + c_fail != 120:
                        print("Total Incorrect") 
                    else :
                        if c_pass == 120 and c_defer == c_fail == 0:
                            print("Progress")
                            l_progress.extend([c_pass,c_defer,c_fail])
                            count_progress = count_progress + 1
                        elif c_pass == 100 and c_defer in(0, 20) and c_fail in (0, 20):
                            print("Progress (module trailer)")
                            l_module.extend([c_pass,c_defer,c_fail])
                            count_trailer = count_trailer + 1
                        elif c_pass in (0, 20, 40) and c_defer in (0, 20, 40) and c_fail in (80, 100, 120) :
                            print("Exclude")
                            l_excluded.extend([c_pass,c_defer,c_fail])
                            count_excluded = count_excluded + 1
                        else :
                            print("Do not progress - module retriever")
                            l_retriever.extend([c_pass,c_defer,c_fail])
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

#Part 2 - Lists (extensions)
# Newly added lines in above - 7,8,9,10,11,26,30,34,38
        print("\nPart 2\n")
        while iter_1 < len(l_progress):          
            print("\nProgress - ", end = ' ')
            for count_list in (l_progress[iter_1:iter_1+3]) :
                print(count_list, end=', ')
            iter_1 = iter_1 + 3
        while iter_2 < len(l_module):
            print("\nModule trailer - ", end =' ')
            for count_list in (l_module[iter_2:iter_2+3]) :
                print(count_list, end=', ')
            iter_2 = iter_2 + 3
        while iter_3 < len(l_retriever):
            print("\nModule retriever - ", end = ' ')
            for count_list in (l_retriever[iter_3:iter_3+3]) :
                print(count_list, end=', ')
            iter_3 = iter_3 + 3
        while iter_4 < len(l_excluded):
            print("\nExclude - ", end = ' ')
            for count_list in (l_excluded[iter_4:iter_4+3]) :
                print(count_list, end=', ')
            iter_4 = iter_4 + 3
        break;