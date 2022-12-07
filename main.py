import Chapter1
import Chapter2
import Chapter3
import Chapter4
import Chapter5
import globalVariable

# This is main module for real-life text based game

def game_intro():
    '''This function prints game introduction.'''
    print("Welcome! This game is about a young career person working as a software developer and looking "
          "to make a career change into something more creative. \n"
          "The object of this game is to make a career change and open own business and make your business grow.")

def main():
    globalVariable.flagChapter1 = True
    game_intro()
    player_name = input("Enter your name:")
    answer = input("Hi {}, will you start this game? (y/n)".format(player_name))
    if answer.upper() == 'Y':
        if globalVariable.flagChapter1 == True:
            print("Calling the chapter 1 module")
            Chapter1.main()
        if globalVariable.flagChapter2 == True:
            print("Calling the chapter 2 module")
            Chapter2.main()
        if globalVariable.flagChapter3 == True:
            print("Calling the chapter 3 module")
            Chapter3.main()
        if globalVariable.flagChapter4 == True:
            print("Calling the chapter 4 module")
            Chapter4.main()
        if globalVariable.flagChapter5 == True:
            print("Calling the chapter 5 module")
            Chapter5.main()
    else:
        print("You are exiting this game.")
        #print("Now you return to main.")
        quit()
main()