import os
from time import sleep


def clear_screen():
    """
    Detect operating system and run relevant
    clear screen command
    """
    # Linux & OSX
    if os.name == "posix":
        os.system("clear")

    # Windows
    else:
        os.system("cls")


def game_rules():
    """
    - Game rules
    """

    rules_pt1 = """
RULES OF THE GAME
-----------------

The Pack
--------
- The game is played using a 52-card pack

Object of the Game
------------------
- The goal is to win the most books of cards
- A book is 4 cards of equal rank, eg.
    3\u2660 3\u2663 3\u2665 3\u2666, J\u2660 J\u2663 J\u2665 J\u2666, etc

The Players
-----------
- In this version of Go Fish!, you are playing against the computer

The Deal
--------
- Each player starts with 7 cards
- The remaing cards are placed face down
  on the table to form the stockpile

    """
    rules_pt2 = """
Playing the Game
----------------
1. You start by requesting a card from the computer
2. If the computer has the card you requested, it will be added to
   your hand and you get another turn
3. If the computer doesn't have the card you requested, you draw a card
    from the stockpile
4. Now it's the computer's turn

Game End
--------
The game ends when either:
- All 13 books have been won between the two players
- A player has an empty hand and there are no cards left in
  the stockpile

    """
    print("-" * 80)
    print(rules_pt1)
    input("┌────────────────────────────┐\n│ Press enter to continue... │\n└────────────────────────────┘")
    sleep(0.5)
    clear_screen()
    print(rules_pt2)
    print("=" * 80)


def game_instructions():
    """
    - Game instructions
    """

    instructions = """
INSTRUCTIONS
------------

1. Enter your name
2. Enter the card you wish to request from the computer
3. For number ranks, you enter 2 to 10
4. For Jack, Queen, King & Ace, enter either the full name or
   the first letter, e.g. Q or Queen
5. If you need to review the rules & instructions during the game,
   enter either "H" or "Help"
6. After the game has ended, enter either:
   - "Y" to play again or
   - "N" to exit the game
    """

    print(instructions)
    print("-" * 80)


def new_game():
    """
    - Display game rules & instructions
    - Reset # books
    - Deal hands
    - Set stockpile
    """

    clear_screen()
    sleep(0.5)
    print("Go Fish!")
    print("\u2588")
    input("┌───────────────────────────────┐\n│ Press enter for game rules... │\n└───────────────────────────────┘")
    print("Function running: new_game()")
    sleep(0.5)
    clear_screen()
    game_rules()
    game_instructions()





def play_game():
    """
    Keep track of:
     - Player 1 hand
     - Player 2 hand
     - Player 1 books
     - Player 2 books
     - Stockpile
     - Card requests
     """

    print("Function running: play_game()")


def player_hand():
    """
    - # Cards in hand
    - Ranks & suits
    - Contains books (4-of-a-kind)?
    """

    print("Function running: player_hand()")


def player_books():
    """
    - # Books
    - Which player has how many books
    """

    print("Function running: player_books()")


def stock_pile():
    """
    - # Cards left
    - Rank and suit of cards left
    """

    print("Function running: stock_pile()")


def input_validation():
    """
    Check for:
     - Format
     - Case
     - Range
     """

    print("Function running: input_validation()")


def randomiser():
    """
    - Pick random card
    - Check if card is available
    """

    print("Function running: randomiser()")


def switch_player():
    """
    Switch active player after turn has finished
    """

    print("Function running: switch_player()")


def play_again():
    """
    - Reset all
    - Exclude rules & instructions
    """
    print("Function running: play_again()")


def main():
    """
    Runs all program functions
    """

    new_game()
    game_rules()
    play_game()
    player_hand()
    player_books()
    stock_pile()
    input_validation()
    randomiser()
    switch_player()
    play_again()


# main()
new_game()
