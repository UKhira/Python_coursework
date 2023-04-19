maintance = 'y'
c_pass = c_fail = c_defer = 0
count_progress = count_trailer = count_retriever = count_excluded = 0
student_count = 0
results_range = (0, 20, 40, 60, 80, 100, 120)
l_result = "" 
iter_1 = iter_2 = iter_3 = iter_4 = 0
l_excluded = []
l_retriever = []
l_module = []
l_progress = [] 
# def credit_function():
    # if c_pass == 120 and c_defer == 0 and c_fail == 0:
    #     l_progress =  "{0} {1} {2}".format(c_pass, c_defer,c_fail) 
    # elif c_pass == 100 and c_defer in(0, 20) and c_fail in (0, 20):
    #     l_module =  "{0} {1} {2}".format(c_pass, c_defer,c_fail) 
    # elif c_pass in (0, 20, 40) and c_defer in (0, 20, 40) and c_fail in (80, 100, 120) :
    #     l_excluded =  "{0} {1} {2}".format(c_pass, c_defer,c_fail) 
    # elif c_pass in (0,20,40,60,80) and c_defer in (0,20,40,60,80,120) and c_fail in (0,20,40,60):
    #     l_retriever =  "{0} {1} {2}".format(c_pass, c_defer,c_fail) 
    # else: 
    #     None
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
                        # credit_function()
                    else :
                        # for a in (l_result):
                            if c_pass == 120 and c_defer == 0 and c_fail == 0:
                                # l_result = "{0}, {1}, {2}".format(c_pass, c_defer,c_fail) 
                                l_progress.extend([c_pass,c_defer,c_fail])
                            elif c_pass == 100 and c_defer in(0, 20) and c_fail in (0, 20):
                                # l_result = "{0}, {1}, {2}".format(c_pass, c_defer,c_fail) 
                                l_module.extend([c_pass,c_defer,c_fail])
                                # l_module =  "{0}, {1}, {2}".format(c_pass, c_defer,c_fail) 
                            elif c_pass in (0, 20, 40) and c_defer in (0, 20, 40) and c_fail in (80, 100, 120) :
                                # l_result = "{0}, {1}, {2}".format(c_pass, c_defer,c_fail) 
                                l_excluded.extend([c_pass,c_defer,c_fail])
                                # l_excluded =  "{0}, {1}, {2}".format(c_pass, c_defer,c_fail) 
                            elif c_pass in (0,20,40,60,80) and c_defer in (0,20,40,60,80,120) and c_fail in (0,20,40,60):
                                # l_result = "{0}, {1}, {2}".format(c_pass, c_defer,c_fail) 
                                l_retriever.extend([c_pass,c_defer,c_fail])
                                # l_retriever =  "{0}, {1}, {2}".format(c_pass, c_defer,c_fail) 
                            else: 
                                None
                        # if c_pass == 120 and c_defer == c_fail == 0:
                        #     print("Progress")
                        #     count_progress = count_progress + 1
                        # elif c_pass == 100 and c_defer in(0, 20) and c_fail in (0, 20):
                        #     print("Progress (module trailer)")
                        #     count_trailer = count_trailer + 1
                        # elif c_pass in (0, 20, 40) and c_defer in (0, 20, 40) and c_fail in (80, 100, 120) :
                        #     print("Exclude")
                        #     count_excluded = count_excluded + 1
                        # else :
                        #     print("Do not progress - module retriever")
                        #     count_retriever = count_retriever + 1
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
      #   print('')
      #   print("-----------------------------------------------------------------")
      #   print("Histogram")
      #   print("Progress ",count_progress," : " ,end ='')
      #   for asterik_pro in range (0, count_progress):
      #       print("*" ,end ='')
      #   print("\nTrailer  ",count_trailer," : ",end='')
      #   for asterik_tra in range(0,count_trailer):
      #       print("*",end='')
      #   print("\nRetriever",count_retriever," : ",end='')
      #   for asterik_ret in range (0,count_retriever):
      #       print("*",end='')
      #   print("\nExcluded ",count_excluded," : ",end='')
      #   for asterik_exc in range (0,count_excluded):
      #       print("*",end='')
      #   print("\n""\n",student_count,"outcomes in total\n-----------------------------------------------------------------")
        while iter_1 <= len(l_progress):
            l_result = "{0}, {1}, {2}".format(c_pass, c_defer,c_fail)
            print("Progress = ",l_result)
            iter_1 = iter_1+2
        while iter_2 <= len(l_module):
            l_result = "{0}, {1}, {2}".format(c_pass, c_defer,c_fail)
            print("Progress (Module trailer) - ",l_module)
            iter_2 = iter_2+3
        # while iter_2 <= len(l_retriever):
        #     l_result = "{0}, {1}, {2}".format(c_pass, c_defer,c_fail)
        #     print("Module retriver - ",l_retriever)
        # while iter_2 <= len(l_excluded):
        #     l_result = "{0}, {1}, {2}".format(c_pass, c_defer,c_fail)
        #     print("Exclude - ",l_excluded)
    
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