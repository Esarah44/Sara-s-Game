import globalVariable
import Chapter1
import Chapter3

def Chapter2_intro():
    '''
    Chapter 2 introduction
    Describe scene of Chapter 2
    '''
    print("This is Chapter2 Intro: The next day you wake up feeling free and inspired to start your own business. \n "
          "Chapter2 Scene: You are at home and jot down ideas of potential businesses that you can start.")

def returnjob():
    print("Your boss calls you and ask you to return to work. Would you like to return?")
    answer = input("Press y to return to work ")
    if answer == "y":
        print("Okay, go back to your 9-5 job ")#return to Chapter 1
        Chapter1.main()
        print("Start Chapter 2 again")
        print("There are three options that you can choose.")
        print("1. Return to job  ")
        print("2. Talk to Family ")
        print("3. Open business  ")
        return True
    else:
        print("return to action module")
        return False
def family():
    print("You talk to your family about your decision to quit. Does your family support your decision to start your own business?")
    answer = input("Press y if your family is being supportive ")
    if answer == "y":
        print("Start open your own business module")
        move = business()
        Chapter3.main()
        return False
    else:
        print("return to action module") #move to option 3 (Open Business)
        return False
def business():
    print("Would you like to open your own nail salon?")
    answer = input("Press y open your own nail salon ")
    if answer == "y":
        print("Okay, continue to Chapter 3") #move to chapter 3
        globalVariable.flagChapter3 = True
        return True
    else:
        print("return to action module")
        return False

def main():
    Chapter2_intro()
    print("There are three options that you can choose.")
    print("1. Return to job  ")
    print("2. Talk to Family ")
    print("3. Open business  ")
    move  = False
    while True:
        option = input("Which option do you take (1-3) ")
        if option == '1':
           returnjob()
        elif option == '2':
           move = family()
        elif option == '3':
            move = business()
        else:
            print("Invalid option, Choose again")
        if move == True:
            break
    globalVariable.flagChapter2 = False

if __name__ == "__main__":
    main()