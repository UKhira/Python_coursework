maintance = 'y'
c_pass = c_fail = c_defer = 0
count_progress = count_trailer = count_retriever = count_excluded = 0
student_count = 0
while maintance == 'y' and maintance != 'q' :
# check credit(pass,defer,fail) and verify entered value is an integer
    try :
        c_pass = int(input("Please enter your credit at pass : "))
        if c_pass in (0, 20, 40, 60, 80, 100, 120):
            None
        else :
            print("Out of Range")
            break;
            
        c_defer = int(input("Please enter your credit at defer : "))
        if c_defer in (0, 20, 40, 60, 80, 100, 120):
            None
        else:
            print("Out of Range")
            break;
        c_fail = int(input("Please enter your credit at fail : "))
        if c_fail in (0, 20, 40, 60, 80, 100, 120):
            None
        else:
            print("Out of Range")
            break;
        if c_pass + c_defer + c_fail != 120:
            print("Total Incorrect")
            break;
        else:
            None
        if c_pass == 120 and c_defer == c_fail == 0:
            print("Progress")
            count_progress = count_progress + 1
        elif c_pass == 100 and c_defer == 0 or 20 and c_fail == 0 or 20:
            print("Progress (module trailer)")
            count_trailer = count_trailer + 1
        elif c_pass == 0 or 20 or 40 and c_defer == 0 or 20 or 40 and c_fail == 80 or 100 or 120 :
            print("Exclude")
            count_excluded = count_excluded + 1
        else :
            print("Do not progress - module retriever")
            count_retriever = count_retriever + 1
        student_count = student_count + 1
    except ValueError:
        print("Integer required")
    maintance = input("Enter 'y' to continue or 'q' to quit and view results : ")
#prediction starts here
    if maintance == 'y' :
        continue;
    elif maintance == 'q' :
        print("Histogram,\n,Progress = ",count_progress,"\nTrailer : ",count_trailer,"\nRetriever = ",count_retriever,"\nExcluded : ",count_excluded)
        break;
        