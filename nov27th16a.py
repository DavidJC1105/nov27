# Question 16(a)
# Name and School:
#David Cummins
import random
x = 1
while x>0:
    s_name=input("Enter your surname:      ")    
    f_name=input("Enter your first name:      ")  
    print("Hello", f_name, s_name)
    age = input("Enter your age")
    age = int(age)
    vaccine = ""
    if age>12:
        if age<49:
            vaccine = "MRNA"
    if age>50:
        vaccine = "ADENO"
    print("Hello", f_name, s_name, "You are ",age)
    eir = input("Enter your eircode")
    abc = int(eir[-1])
    enrol = input("Do you agree to enrol in a vaccine trial?\nType Yes or No")
    enrol = enrol.lower()
    vaclist = ["MRNA","ADENO","Vaccine3"]
    if enrol == "yes":
        print("You will recieve the ",random.choice(vaclist)," vaccine")
    else:
        print(f_name,"you will recieve the",vaccine," vaccine")
    if abc%2 == 0:
        print("You must attend Eastwood for your vaccine")
    else:
        print("You must attend Northfield for your vaccine")
    q = input("If you have finished entering peoples deatils type \n'END', otherwise press return")
    q = q.lower()
    if q == "end":
        break


list1 = [4,5,9,8,10,17,99,77]
yes = len(list1)
if yes%2==0:
    up = (((yes/2)+1)%10)
    up = int(up)
    down = ((yes/2)%10)
    down = int(down)
    ups = list1[up-1]
    downs = list1[down-1]
    value = (ups+downs)/2
    value = int(value)
    print("The median of this list is ",value)
else:
    middle = ((yes/2)+1)%10
    middle = int(middle)
    value = list1[middle-1]
    print("The median of this is list ",value)