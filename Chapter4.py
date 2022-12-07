import globalVariable

def Chapter4_intro():
    '''
    Chapter 4 introduction
    Describe scene of Chapter 4
    '''
    print("This is Chapter4 Intro: You love your job as a nail salon owner. \n"
          "Chapter4 Scene: You love your job because it allows you to be creative, interact with client "
          "and the best part is that your are your own boss.")

def Happy():
    print("Are you happy with your new career?")
    answer= input("Press y if you are happy with your new career. ")
    if answer == "y":
        print("return to action module")
        return True
    else:
        print("return to chapter 1") #return to chapter 1
        return False
def Extracash():
    print("Enter nail design competition for extra cash and exposure to business")
    answer = input("Press y enter nail design competitions ")
    if answer == "y":
        print("Go to Growing module") #move to option 3 in chapter 4 options.
        move = Growing()
        return True
    else:
        print("return to action module")
        return False
def Growing():
    print("You are overwhelmed with how much business you have. Do you want to hire an employee?")
    answer = input("Press y to hire employee ")
    if answer == "y":
        print("Okay, continue to Chapter 5") #Go to chapter 5.
        globalVariable.flagChapter5 = True
        return True
    else:
        print("return to action module")
        return False

def main():
    Chapter4_intro()
    print("There are three options that you can choose.")
    print("1. Happy with business      ")
    print("2. Earn Extra cash          ")
    print("3. Business is growing fast ")
    move  = False
    while True:
        option = input("Which option do you take (1-3) ")
        if option == '1':
           Happy()
        elif option == '2':
           move = Extracash()
        elif option == '3':
           move = Growing()
        else:
           print("Invalid option, Choose again")
        if move == True:
            break
    globalVariable.flagChapter4 = False

if __name__ == "__main__":
    main()