import os
from time import sleep

import random


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
    btn_top = "┌────────────────────────────┐\n"
    btn_middle = "│ Press enter to continue... │\n"
    btn_bottom = "└────────────────────────────┘"
    input(btn_top + btn_middle + btn_bottom)
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


# Set global variables
deck = []
human_hand = []
human_books = 0
computer_hand = []
stockpile_list = []
books = []
active_player = "human"
opponent = "computer"


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
    btn_top = "┌───────────────────────────────┐\n"
    btn_middle = "│ Press enter for game rules... │\n"
    btn_bottom = "└───────────────────────────────┘"
    input(btn_top + btn_middle + btn_bottom)
    
    # Test output
    print("\n*** Function running: new_game() ***\n")
    sleep(0.5)
    clear_screen()
    game_rules()
    game_instructions()


def build_deck():
    """
    - Create suits
    - Create ranks
    - Add ranks & suits to deck
    - UTF codes:
        -   Spades: \u2660
        -    Clubs: \u2663
        -   Hearts: \u2665
        - Diamonds: \u2666
    """

    suit_list = ["\u2660", "\u2663", "\u2665", "\u2666"]
    rank_list = [
        "A", "2", "3", "4", "5", "6", "7",
        "8", "9", "10", "J", "Q", "K"
    ]

    for suit in suit_list:
        for rank in rank_list:
            deck.append(rank + suit)
    # Test output
    # print(f"\nOriginal deck:\n {deck}")


def shuffle_deck():
    """
    - Shuffle the deck
    """
    global shuffled_deck
    shuffled_deck = []
    random.shuffle(deck)

    for card in deck:
        shuffled_deck.append(card)

    # Test output
    # print(f"\nShuffled deck:\n {shuffled_deck}")
    return shuffled_deck


def deck_card_count():
    """
    - Count the amount of cards in the shuffled deck
    """
    global deck_count
    deck_count = len(shuffled_deck)


def select_card_from_deck():
    """
    - Select card from shuffled deck
    """

    global selected_card
    selected_card = ""
    selected_card = shuffled_deck[0]

    return selected_card


def add_card_to_hand():
    """
    - Add card to hand
    """

    deck_card_count()

    if deck_count % 2 != 1:
        human_hand.append(selected_card)
    else:
        computer_hand.append(selected_card)


def remove_card_from_deck():
    """
    - Remove selected card from shuffled deck
    """
    shuffled_deck.remove(selected_card)


def deal_cards():
    """
    - Add 7 cards to computer's hand
    - Add 7 cards to player's hand
    - Add remainder to the stockpile
    """
    
    # Test output
    print("\n*** Function running: deal_cards() ***\n")

    global stockpile_list
    deck_card_count()

    # Test output
    # sleep(1)
    # print(f"\nDeck count before deal: {deck_count}")

    # Deal player hands
    while deck_count != 38:
        select_card_from_deck()
        add_card_to_hand()
        remove_card_from_deck()
        deck_card_count()

        # Add remaing 38 cards to stockpile
        if deck_count == 38:
            stockpile_list.extend(shuffled_deck)

    # Test output
    # sleep(1)
    # print(f"\n------------------\nSelected card: {selected_card}\n------------------\n")
    # print(f"\nDeck count after deal: {deck_count}\n")
    # print(f"\nShuffled deck after deal:\n {shuffled_deck}\n")
    print(f"\n------------------------------------------------------------\n")
    print(f"Human hand({len(human_hand)}):", end=" ")
    print(*human_hand)
    print(f"\nHuman books: {human_books}")
    print(f"\nComputer hand({len(computer_hand)}):", end=" ")
    print(*computer_hand)
    print(f"\n------------------------------------------------------------")
    print(f"\nStockpile({len(stockpile_list)}):\n")
    print(*stockpile_list, end=" ")
       

human_requested_card = ""


def check_hand():
    """
    - Check hand for requested card otherwise
      draw a card from the stockpile
    """

    # Test output
    print("\n*** Function running: check_hand() ***\n")

    match = [card for card in computer_hand if human_requested_card in card]
    print("\nMatch:", end=" ")
    print(*match)
    if match:
        human_hand.extend(match)
        check_for_books()
    else:
        print(f"The {opponent} doesn't have that card.")
        sleep(0.5)
        draw_from_stockpile()

    for card in match:
        computer_hand.remove(card)
            
    print(f"\n------------------------------------------------------------\n")
    print(f"Human hand({len(human_hand)}):", end=" ")
    print(*human_hand)
    print(f"\nHuman books: {human_books}")
    print(f"\nComputer hand({len(computer_hand)}):", end=" ")
    print(*computer_hand)
    print(f"\n------------------------------------------------------------")

    play_game_round()

    
def draw_from_stockpile():
    """
    - Draw a card from the stockpile
    - Add card to player's hand
    """
    # Test output
    print("\n*** Function running: draw_from_stockpile() ***\n")
    
    print(f"Drawing a card from the stockpile...")
    selected_card = stockpile_list[0]
    human_hand.append(selected_card)
    stockpile_list.remove(selected_card)

    check_for_books()

    # stock_pile()



def play_game_round():
    """
    Keep track of:
     - Human hand
     - Computer hand
     - Human books
     - Computer books
     - Stockpile
     - Card requests
     """
    
    # Test output
    print("\n*** Function running: play_game_round() ***\n")

    global human_requested_card
    stock_pile()
    human_input = input("\nWhich card would you like to request? ")
    human_requested_card = human_input.upper()
    print(f"\nYou requested: {human_requested_card}")
    check_hand()


def human_table():
    """
    - # Cards in hand
    - Ranks & suits
    - Contains books (4 of equal rank)?
    """

    print("\n*** Function running: human_table() ***\n")
    print(f"Human hand: {human_hand}")


def computer_table():
    """
    - # Cards in hand
    - Ranks & suits
    - Contains books (4 of equal rank)?
    """

    # Test output
    print("\n*** Function running: computer_table() ***\n")
    print(f"Computer hand: {computer_hand}")


def check_for_books():
    """
    - Check if the active player has a book (4 of equal rank)
      after each round
    """
    
    # Test output
    print("\n*** Function running: check_for_books() ***\n")
    # sleep(1)
    
    global human_books
    duplicate_ranks = [card for card in human_hand if human_requested_card in card]

    if duplicate_ranks:
        print(f"Duplicates({len(duplicate_ranks)}):", end=" ")
        print(*duplicate_ranks)

    if len(duplicate_ranks) == 4:
        
        for card in duplicate_ranks:
            human_hand.remove(card)
        human_books += 1
    
    # sleep(0.5)


def player_books():
    """
    - # Books
    - Which player has how many books
    """

    # Test output
    print("\n*** Function running: player_books() ***\n")


def stock_pile():
    """
    - # Cards left
    - Rank and suit of cards left
    """
    
    # Test output
    print("\n*** Function running: stock_pile() ***\n")

    print(f"\nStockpile({len(stockpile_list)}):\n")
    print(*stockpile_list, end=" ")

    if stockpile_list == [] and computer_hand == []:
        game_end()


def input_validation():
    """
    Check for:
     - Format
     - Case
     - Range
     """

    # Test output
    print("\n*** Function running: input_validation() ***\n")


def randomiser():
    """
    - Pick random card
    - Check if card is available
    """

    # Test output
    print("Function running: randomiser()")


def switch_player():
    """
    Switch active player after turn has finished
    """
    global active_player
    if active_player == "human":
        active_player = "computer"
        opponent = "human"
        print("It is the computer's turn to play")
    else:
        active_player = "human"
        opponent = "computer"

    # Test output
    print("\n*** Function running: switch_player() ***\n")
    print(f"\nActive player: {active_player}")


def game_end():
    """
    - Game ends when either player's hand AND
      the stockpile are empty
    """
    
    # Test output
    print("\n*** Function running: game_end() ***\n")

    print("End of game")


def play_again():
    """
    - Reset all
    - Exclude rules & instructions
    """

    # Test output
    print("\n*** Function running: play_again() ***\n")


def main():
    """
    Runs all program functions
    """

    new_game()
    game_rules()
    play_game_round()
    human_hand()
    player_books()
    stock_pile()
    input_validation()
    randomiser()
    switch_player()
    play_again()


# main()
# new_game()
build_deck()
shuffle_deck()
deal_cards()
# switch_player()
print(f"\n\nActive player: {active_player}")
play_game_round()
