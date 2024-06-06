# Start of the game
print("Welcome...to your dreams!")

"""
The startGame() is the whole entire game that runs on the method.
Also includes all the choices that the user wants.
"""
def startGame():
    # Beginning of the story
    print(('You awoke from your slumber. '
           'You realized that living in the castle made you bored.'
           'You decided to visit the king. The king has a task for you.'
           'To bring the diamond crystal.'
           'Out of pure boredom, you decided to take on this quest.\n'))
    
    # Ask the user which path to choose
    print("On your way to the diamond crystal there are five paths to choose.")

    choiceChosen = False # To end the loop and prevent iterating again.

    # To let the user pick the five choices if they press an invalid number
    while not choiceChosen:
        choice = int(input("Which choice will you choose? 1, 2, 3, 4, or 5? "))

        # To check which choice the user enters
        match choice:
            case 1:
                print("You die due an entire tree falling on you.")
                choiceChosen = True
            
            case 2:
                print(('You found the diamond crystal but became corrupted with' 
                       ' its powers and decided to steal it for yourself.'))
                choiceChosen = True

            case 3:
                print(('You found the diamond crystal but contemplated your'
                       'life choices and how you were treated poorly by ' 
                       'the king. You steal the power of the diamond crystal' 
                       'and live somewhere else'))
                choiceChosen = True

            case 4:
                print("You return the diamond crystal back to the king.")
                choiceChosen = True

            case 5:
                print(('You do not want anyone, including yourself, '
                       'to have power. You destroyed it leaving your'
                       ' fate unknown.'))
                choiceChosen = True

            case _:
                print("That is not a choice. Please try again.")
                continue

"""
The main() is where all the code runs and begins. To organize the code and
not make the code messy.
"""
def main():
    gameStart = True # For the loop when user wants to change name again

    # Let the user have a chance to name their character again
    while gameStart:
        name = input("What is your name, young one? ")

        print(f'Ah, so your name is {name}. That is an interesting name.')
        verifyName = input("Is that the name you want? Enter either Y or N: ")

        # Give the user ability to choose if they want to change their name
        match verifyName:
            case 'N' | 'n':
                continue
            case "Y" | 'y':
                print("All right. Time to begin your adventure. \n")
                gameStart = False
            case _:
                print("That is an invalid choice. Going to assume name change.")
                continue
    
    startGame() # Runs the entire game after character naming

main() # To run the character naming part