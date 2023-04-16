#Part 1 - Main Version
import re
c_defer = 0 
c_fail = 0
c_pass = 0
maintance = 'y'
validator = True
count_progress = count_trailer = count_retriever = count_excluded = 0
student_count = 0
results_range = (0, 20, 40, 60, 80, 100, 120)
iter_1 = iter_2 = iter_3 = iter_4 = 0
l_excluded = []
l_retriever = []
l_module = []
l_progress = []

def credit_pass_input():
    global c_pass, results_range
    c_pass = int(input("Please enter your credit at pass : "))
    while c_pass not in (results_range):
        print("Out of Range")
        c_pass = int(input("Please enter your credit at pass : "))
    return c_pass
        
        
def credit_defer_input():
    global c_defer,results_range
    c_defer = int(input("Please enter your credit at defer : "))  
    while c_defer not in results_range:
        print("Out of Range")
        c_defer = int(input("Please enter your credit at defer : ")) 
    return c_defer      
       
        
def credit_fail_input():
    global c_fail,results_range
    c_fail = int(input("Please enter your credit at fail : "))   
    while c_fail not in results_range:
        print("Out of Range")
        c_fail = int(input("Please enter your credit at fail : "))  
    return c_fail
        
def total_check():
    global c_pass,c_defer,c_fail
    while c_pass + c_defer + c_fail != 120:
        print("Total Incorrect")
        credit_pass_input();
        credit_defer_input();
        credit_fail_input();


def progress_add_mark():
    global count_progress
    print("Progress")
    l_progress.extend([c_pass,c_defer,c_fail])
    count_progress = count_progress + 1
    return(count_progress)
        

def trailer_add_mark():
    global count_trailer
    print("Progress (module trailer)")
    l_module.extend([c_pass,c_defer,c_fail])
    count_trailer = count_trailer + 1
    return(count_trailer)
            

def exclude_add_mark():
    global count_excluded
    print("Exclude")
    l_excluded.extend([c_pass,c_defer,c_fail])
    count_excluded = count_excluded + 1
    return count_excluded
                

def retriever_add_mark():
    global count_retriever
    print("Do not progress - module retriever")
    l_retriever.extend([c_pass,c_defer,c_fail])
    count_retriever = count_retriever + 1
    return(count_retriever)
        
        
while maintance == 'y' and maintance != 'q' :
# check credit(pass,defer,fail) and verify entered value is an integer
    try :
        credit_pass_input();

        credit_defer_input();

        credit_fail_input();

        total_check();
            
        if c_pass == 120 and c_defer == c_fail == 0:
            progress_add_mark();
        elif c_pass == 100 and c_defer in(0, 20) and c_fail in (0, 20):
            trailer_add_mark();
        elif c_pass in (0, 20, 40) and c_defer in (0, 20, 40) and c_fail in (80, 100, 120) :
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
    else :
        print("Invalid Input Try Again") 
        break;  

          
        