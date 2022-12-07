import globalVariable
import Chapter1

def Chapter3_intro():
    '''
    Chapter 3 introduction
    Describe scene of Chapter 3
    '''
    print("This is Chapter3 Intro: You decide to open a nail salon. \n"
          "Chapter3 Scene: You start executing your business plan and meet with a realtor who shows you "
          "potential business locations.")

def regretdecision():
    print("Your regret your decision to open your own business.")
    answer = input("Press y ask your boss for your old job back ")
    if answer == "y":
        print("Okay, return to chapter 1") #Go back to chapter 1, and return to chapter 3
        Chapter1.main()
        print("Start Chapter 3 again")
        print("There are three options that you can choose.")
        print("1. Get old job back            ")
        print("2. Take on tasks               ")
        print("3. View locations for business ")
    else:
        print("return to action module")
        return False
def task():
    print("There are two options that you can choose.")
    print("1. Get loan for business  ")
    print("2. Go to nail school ")
    move  = False
    while True:
        option = input("Which option do you take (1 or 2) ")
        if option == '1':
           task()
        elif option == '2':
            print("return to action module")# will return you to chapter 3 options
            print("There are three options that you can choose.")
            print("1. Get old job back            ")
            print("2. Take on tasks               ")
            print("3. View locations for business ")
            return False
        if move == True:
            break
def realtor():
    print("Meet with your realtor to view possible space locations")
    answer = input("Press y to rent the space ")
    if answer == "y":
        print("Okay, continue to Chapter 4") #move to chapter 4
        globalVariable.flagChapter4 = True
        return True
    else:
        print("return to action module")
        return False

def main():
    Chapter3_intro()
    print("There are three options that you can choose.")
    print("1. Get old job back            ")
    print("2. Take on tasks               ")
    print("3. View locations for business ")
    move  = False
    while True:
        option = input("Which option do you take (1-3) ")
        if option == '1':
           regretdecision()
        elif option == '2':
           move = task()
        elif option == '3':
            move = realtor()
        else:
            print("Invalid option, Choose again")
        if move == True:
            break
    globalVariable.flagChapter3 = False

if __name__ == "__main__":
    main()