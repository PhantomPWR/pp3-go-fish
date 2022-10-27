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
    print("Function running: new_game()")
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
    sleep(1)
    # print(f"\n------------------\nSelected card: {selected_card}\n------------------\n")
    print(f"\n------------------------------------------------------------\nHuman hand({len(human_hand)}): {human_hand}")
    print(f"\nComputer hand({len(computer_hand)}): {computer_hand}\n------------------------------------------------------------")
    # print(f"\nDeck count after deal: {deck_count}\n")
    # print(f"\nShuffled deck after deal:\n {shuffled_deck}\n")
    print(f"\nStockpile:\n {stockpile_list}\n")
       

human_requested_card = ""


def check_hand():
    """
    - Check hand for requested card
    """

    for card in computer_hand:

        match_list = []
        match = card[:1]

        if human_requested_card == match:
            match_list.append(match)
            print(f"Match list: {match_list}")
            human_hand.append(card)
            computer_hand.remove(card)
            print(f"\n------------------------------------------------------------\nHuman hand({len(human_hand)}): {human_hand}")
            print(f"\nComputer hand({len(computer_hand)}): {computer_hand}\n------------------------------------------------------------")
            play_game_round()
        else:
            print(f"The {opponent} doesn't have that card.")




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
    
    print("Function running: play_game_round()")
    global human_requested_card
    human_requested_card = input("Which card would you like to request? ")

    print(f"You requested: {human_requested_card}")
    check_hand()


def human_table():
    """
    - # Cards in hand
    - Ranks & suits
    - Contains books (4-of-a-kind)?
    """

    print("Function running: human_hand()")
    print(f"Human hand: {human_hand}")


def computer_table():
    """
    - # Cards in hand
    - Ranks & suits
    - Contains books (4-of-a-kind)?
    """

    print("Function running: human_hand()")
    print(f"Computer hand: {computer_hand}")


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
    global active_player
    if active_player == "human":
        active_player = "computer"
        opponent = "human"
        print("It is the computer's turn to play")
    else:
        active_player = "human"
        opponent = "computer"
    print("Function running: switch_player()")
    print(f"Active player: {active_player}")


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
switch_player()
play_game_round()
