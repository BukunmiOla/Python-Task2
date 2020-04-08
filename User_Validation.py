#This program gets User data
#It suggests password or get user password if not satisfied with the suggested password
#It saves each user's details in a container

# Import libraries
import string
import random

#Global variables declaration
user_id=0
user_data={}
container ={}
start = True  #This represent the status of the process. True = start, False=finish

#The function below gets the user's details by Input and save it in the dictionary called user_data.
#At the end, it returns the dictionary.
def get_detail():
    
    first_name = input("Enter fist name here: ")
    last_name = input("Enter last name here: ")
    name = first_name+" "+ last_name
    user_data["Name"] = name
    email = input("Enter email here: ")
    correct_email = check_email(email)          #jump to the function check_email()
    while correct_email==False:
        print ("The email address you entered is INVALID! Please try again.")
        email = input("\nEnter email here: ")
        correct_email = check_email(email)
    else:
        user_data["Email"] = email

    return user_data

#This function checks the validity of the email supplied 
def check_email(email):
    
    com = email.endswith(".com") #This will check if the email ends with .com
    at = '@' in email            #this will check if the email contains the character @
    
    if com == True and at == True:
        correct_email=True
    else:
        correct_email=False
        
    return correct_email


#The function below generates a Suggested password using the details provided
#At the end, it returns the suggested password
def suggest_password(user_data):
    
    first_2_letters_of_first_name = user_data["Name"][0:2]
    last_2_letters_of_last_name = user_data["Name"][-2:]
    five_random_letters = ''.join(random.choice(string.ascii_letters)for i in range(5))

    suggested_password= first_2_letters_of_first_name+last_2_letters_of_last_name+five_random_letters

    return(suggested_password)



#This is main process of the program
while start == True:
    
    #Introductory part of the program
    print ("\n\nHi! Welcome to HNG tech, It's good to have you here.")
    print ("\nI'm Bukunnmi, and I'll be setting up an account for you on the company's network.")
    print ("\nPlease relax while I take you through the process and do make sure to supply the correct information, Thank you.\n")

    get_detail()  #Get the user details


    suggested_password = suggest_password(user_data) #Fetch the suggested password
    
    
    #Display the password
    print ("\nThe password suggested for you is: "+suggested_password)
    
    #Get feedback about the password
    satisfaction=0  #This will capture the user's input on password satisfaction. 0=void, 1=Yes and 2=No
    
    while satisfaction == 0:
        response=input("Are you satisfied with the password? Enter 'Y' for yes or 'N' for no: ")
        if response=='Y' or response=='y':
            satisfaction=1  
            
        elif response=='N' or response=='n':
            satisfaction=2  

        else:
            print ("WRONG INPUT! Please Enter 'Y' for yes or 'N' for no\n")

    else:
        if satisfaction==1:
            user_data["Password"] = suggested_password
            print("\nUser details: "+str(user_data))

        else :
            print("\nOkay, Note that your password should be at least 7 characters")
            user_password=input("\nPlease enter your preferred password: ")
        
            while len(user_password)<7:
                print("PASSWORD TOO SMALL! \n Note that password should be at least 7 characters long")
                user_password=input("\nPlease enter your  preferred password: ")
            else:
                user_data["Password: "] = user_password
                print("\nUser details: "+str(user_data))

    user_id+=1
    container[user_id] = user_data
    user_data={}
    
    print ("User details is successfully saved. Thanks for your time.")
    status = input("\nEnter 'Y' to create a new record or any other key to quit: ")
    if status == 'Y' or status == 'y':
        start = True
    else:
        start = False

print ("Thank You! Below are the details of every registered user.\n")
user_id+=1
for i in range (1,user_id):
    print (container[i])
