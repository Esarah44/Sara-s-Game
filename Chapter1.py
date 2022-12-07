#import Chapter2
import globalVariable

def Chapter1_intro():
    '''
    Chapter 1 introduction
    Describe scene of Chapter 1
    '''
    print("This is Chapter1 Intro: It was another long day at your 9-5 office job doing work you don't very much "
          "enjoy and with the worse boss you have ever had. \n"
          "Chapter1 Scene: You are about to end your day and go home when your boss calls you into their office "
          "to give you an ear full about why a project hasn't been completed \nby the unachievable deadline.")
#You will then see three options.
def Overtime():
    print("Would you like to work overtime to complete the project?")
    answer = input("Press y to work overtime ") # Y = Yes
    if answer == "y":
        print("Okay, continue to work overtime ")
        return False
    else:
        return True

def Quit():
    print("Would you like to quit your job?")
    answer = input("Press y to quit job ") # Y = Yes
    if answer == "y":
        print("Go home to contemplate your next career move")
        print("Chapter1 ends")
        globalVariable.flagChapter2= True
        return True
    else:
        print("Okay, continue working your 9-5 job")
        return False

def main():
    Chapter1_intro()
    print("There are two options that you can choose.")
    print("1. Work overtime ")
    print("2. Quit job      ")

    while True:
        option = input("Which option do you take (1-2) ")
        if option == '1':
            move = Overtime()
        elif option == '2':
            move = Quit() #move to chapter 2
        else:
            print("Invalid option, Choose again")
        if move == True:
            break
    globalVariable.flagChapter1 = False

if __name__ == "__main__":
    main()

