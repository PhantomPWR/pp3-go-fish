

def new_game():
    """
    Display game rules & instructions
    Reset # books
    Deal hands
    Set stockpile
    """

    # Clear screen
    # print(chr(27) + "[2J")
    print(chr(27) + "[2]")
    print("Go Fish!")

    print("Function running: new_game()")
    game_rules()


def game_rules():
    """
    - Game rules
    - Instructions on how to play
    """

    rules = """
The Pack
--------
- The game is played using a 52-card pack

Object of the Game
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

    instructions = """
1. You start
    """

    print("-" * 80)
    print(rules)
    print("-" * 80)

    print("-" * 35)
    print(instructions)
    print("-" * 35)

    print("Function running: game_rules()")


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


#main()
new_game()
