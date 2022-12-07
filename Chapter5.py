import globalVariable
import Chapter1

def Chapter5_intro():
    '''
    Chapter 5 introduction
    Describe scene of Chapter 5
    '''
    print("This is Chapter5 Intro: Your business has been going great and you want to hired a part-time employee. \n"
          "Chapter5 Scene: You realize that your business is doing great and that you need help to be able to take "
          "on more appointments, \nso you decide to post a job position for a part-time employee.")

def Interviews():
    print("You start to interview nail technician")
    answer= input("Press y if you want to hire the nail technician ")
    if answer == "y":
        print("Go to invest tasks") # go to option 2 in chapter 5.
        move = Invest()
        return True
    else:
        print("return to action module")
        return False
def Invest():
    print("Your business is growing faster than ever. Do you want to invest more money into the business?")
    answer = input("Press y if you want to invest money ")
    if answer == "y":
        print("Congratulations, you have a successful business. \nEnd Game") #This option will end the game.
        return True
    else:
        print("return to action module")
        return False
def Donothire():
    print("You don't hire help and you can't keep up with the growing business. Do you want to shut "
          "own your business?")
    answer = input("Press y if you want to close your business ")
    if answer == "y":
        print("Okay, continue to Chapter 1") #this will bring you back to chapter 1.
        Chapter1.main()
        return True
    else:
        print("return to action module")
        return False

def main():
    Chapter5_intro()
    print("There are three options that you can choose.")
    print("1. Set up interviews       ")
    print("2. Invest more money       ")
    print("3. Do not hire technician  ")
    move  = False
    while True:
        option = input("Which option do you take (1-3) ")
        if option == '1':
           move = Interviews()
        elif option == '2':
           move = Invest()
        elif option == '3':
           move = Donothire()
        else:
           print("Invalid option, Choose again")
        if move == True:
            break
    globalVariable.flagChapter5 = False

if __name__ == "__main__":
    main()