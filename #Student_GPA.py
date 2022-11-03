#Jordy Jordan
#Student_GPA
#01/11/2022
#This program will recieve a name and a gpa input and then it will check whether or not that person should be on Dean's List or the Honor Roll.

#The user enters a last name or quits the program
lastname = input("Enter the last name or type 'ZZZ' to quit: ")

#Now the user enters the loop in which multiple names can be tested 
while lastname != "ZZZ":

    #The user enters a first name
    firstname = input("Enter your first name: ")

    #The user enters a GPA, and it can be a float number
    gpa = float(input("Enter your GPA: "))

    #The program checks if the gpa is 3.5 or bigger
    if gpa >= 3.5:
        #If so, it will display the last name and the last name together with the Dean's List
        print (firstname + ", " +  lastname + " made it to the Dean's List with a GPA of " + str(gpa) +".\n")

    #If the GPA is 3.25 or bigger
    elif gpa >= 3.25:
        #If so, it will display the last name and the last name together with the Honor Roll 
        print (firstname + ", " + lastname + " made it to the Honor Roll with a GPA of " + str(gpa) +".\n")
    
    #If not any of these then it will diplay say that the person cannot be on the Dean's List or the Honor Roll.
    else:
        print (firstname + ", " + lastname + " does not qualify for either the Dean's List or the Honor Roll, with a GPA of " + str(gpa) +".\n")

    lastname = input("Enter the last name or type 'ZZZ' to quit: ")
