import os

from time import sleep

import random


class GoFish:
    """
    - Runs the entire game
    """
    def clear_screen(self):
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

    def game_rules(self):
        """
        - Explain the game rules
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
        - The remaining cards are placed face down
          on the table to form the stockpile

        """

        rules_pt2 = """
        Playing the Game
        ----------------
        1. You start by requesting a card from the computer
        2. If the computer has one or more of the card you requested, it will
           be added to your hand and you get another turn
        3. If the computer doesn't have the card(s) you requested, you draw a
           card from the stockpile
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
        GoFish().clear_screen()
        print(rules_pt2)
        print("=" * 80)

    def game_instructions(self):

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

    def new_game(self):
        """
        - Display game rules & instructions
        - Reset # books
        - Deal hands
        - Set stockpile
        """

        game.clear_screen()
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
        game.clear_screen()
        game.game_rules()
        game.game_instructions()


# Set global variables
deck = []
human_hand = []
human_books = 0
computer_hand = []
computer_books = 0
stockpile_list = []
player_hand = []
books = []
requested_card = ""
book_check_trigger = ""


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
    global card_to_deal
    card_to_deal = shuffled_deck[0]

    return card_to_deal


def add_card_to_hand():
    """
    - Add card to hand
    """

    deck_card_count()

    if deck_count % 2 != 1:
        human_hand.append(card_to_deal)
    else:
        computer_hand.append(card_to_deal)


def remove_card_from_deck():
    """
    - Remove selected card from shuffled deck
    """
    shuffled_deck.remove(card_to_deal)


def deal_cards():
    """
    - Add 7 cards to computer's hand
    - Add 7 cards to player's hand
    - Add remainder to the stockpile
    """
    
    # Test output
    # print("\n*** Function running: deal_cards() ***\n")

    global stockpile_list
    deck_card_count()

    # Deal player hands
    while deck_count != 38:
        select_card_from_deck()
        add_card_to_hand()
        remove_card_from_deck()
        deck_card_count()

        # Add remaing 38 cards to stockpile
        if deck_count == 38:
            stockpile_list.extend(shuffled_deck)
    
    # Group ranks together for readability
    human_hand.sort()

    print(f"\n------------------------------------------------------------\n")
    print(f"Active player: {active_player}\n\n")
    # print(f"Opponent: {opponent}\n\n")
    # print(f"Human hand({len(human_hand)}):", end=" ")
    print(f"Human hand:", end=" ")
    print(*human_hand)
    print(f"\nHuman books: {human_books}")
    # print(f"\nComputer hand({len(computer_hand)}):", end=" ")
    # print(*computer_hand)
    print(f"\nComputer books: {computer_books}")
    print(f"\n------------------------------------------------------------")
    # print(f"\nStockpile({len(stockpile_list)}):\n")
    # print(*stockpile_list, end=" ")
       

def check_hand(active_player, opponent, requested_card, book_check_trigger):
    """
    - Check hand for requested card otherwise
      draw a card from the stockpile
    """
    # global book_check_trigger
    # book_check_trigger = requested_card

    # Test output
    print("\n*** Function running: check_hand() ***\n")
    print(f"\n====== book_check_trigger from check_hand(): {book_check_trigger}")

    if active_player == "human":
        player_hand = human_hand
        opponent_hand = computer_hand
    else:
        player_hand = computer_hand
        opponent_hand = human_hand
    
    match = [card for card in opponent_hand if requested_card in card]

    # Test output
    # print("\nMatch:", end=" ")
    # print(*match)

    singular_plural = ""
    if len(match) == 1:
        singular_plural = "card"
    else:
        singular_plural = "cards"

    if match:
        print(f"The {opponent} is handing over {len(match)} {singular_plural}.")
        player_hand.extend(match)
        check_for_books(active_player, book_check_trigger)
    else:
        print(f"\n=== The {opponent} doesn't have that card. ===\n")
        sleep(0.5)
        draw_from_stockpile(active_player, opponent)

    for card in match:
        opponent_hand.remove(card)

    player_hand.sort()

    # check_for_books(active_player, book_check_trigger)

    # play_game_round(active_player, opponent, book_check_trigger)
    play_game_round(active_player, opponent)

    
def draw_from_stockpile(active_player, opponent):
    """
    - Draw a card from the stockpile
    - Add card to active player's hand
    """

    # Test output
    # print("\n*** Function running: draw_from_stockpile() ***\n")
    
    print("\n=== Drawing a card from the stockpile... ===\n")
    drawn_card = stockpile_list[0]
    book_check_trigger = drawn_card[:1]
    
    if active_player == "human":
        print(f"\n=== Human drew: {drawn_card}")
        human_hand.append(drawn_card)
        print("\n=== Adding card to human hand ===\n")
        print(f"\n====== book_check_trigger from draw_from_stockpile(): {book_check_trigger}")
    else:
        print(f"\n=== Computer drew: {drawn_card}")
        computer_hand.append(drawn_card)
        print("\n=== Adding card to computer hand ===\n")
        print(f"\n====== book_check_trigger from draw_from_stockpile(): {book_check_trigger}")

    
    if stockpile_list == [] and computer_hand == []:
        game_end()
    else:
        stockpile_list.remove(drawn_card)
    
    # book_check_trigger = drawn_card[:1]
    check_for_books(active_player, book_check_trigger)
    switch_player(active_player, opponent)


def switch_player(active_player, opponent):
    """
    Switch active player after turn has finished
    """
    # global active_player
    # global opponent

    print(f"Active player (switch_player start):  {active_player}")


    if active_player == "human":
        active_player = "computer"
        opponent = "human"
        print("=== It is the computer's turn to play ===")

    # elif active_player == "computer":
    else:
        active_player = "human"
        opponent = "computer"
        print("=== It is your turn to play ===")


    # Test output
    # print("\n*** Function running: switch_player() ***\n")
    # print("\n=== Checking for books ===\n")

    print(f"Active player (switch_player end):  {active_player}")
    # play_game_round(active_player, opponent, book_check_trigger)
    play_game_round(active_player, opponent)
    


def play_game_round(active_player, opponent):
    """
    Keep track of:
     - Human hand
     - Computer hand
     - Human books
     - Computer books
     - Stockpile
     - Card requests
     """
    
    # check_for_books(active_player, book_check_trigger)

    global requested_card
    stock_pile()

    print(f"\n------------------------------------------------------------\n")
    print(f"Active player: {active_player}\n\n")
    # print(f"Opponent: {opponent}\n\n")
    print(f"Human hand:", end=" ")
    print(*human_hand)
    print(f"\n\n    Human books: {human_books}                     Computer books: {computer_books}")
    # print(f"\nComputer hand({len(computer_hand)}):", end=" ")
    # print(*computer_hand)
    # print(f"\nComputer books: {computer_books}")
    print(f"\n------------------------------------------------------------")
    # print(f"\nStockpile({len(stockpile_list)}):\n")
    # print(*stockpile_list, end=" ")


    # Group ranks together for readability
    human_hand.sort()

    if active_player == "human":
        human_input = input("\nWhich card would you like to request? ")
        requested_card = human_input.upper()
        print(f"\nYou requested: {requested_card}")
        book_check_trigger = requested_card

    else:
        if len(computer_hand) >= 1:
            random_card = random.choice(computer_hand)
        else:
            random_card = random.choice(deck)
        requested_card = random_card[:-1]
        book_check_trigger = requested_card
        print(f"\nThe computer requested: {requested_card}\n")
        sleep(2)

    # book_check_trigger = requested_card

    # Test output
    print(f"\n ====== book_check_trigger from play_game_round() outside if...else statement: {book_check_trigger} ======\n")

    check_hand(active_player, opponent, requested_card, book_check_trigger)

    check_for_books(active_player, book_check_trigger)


def check_for_books(active_player, book_check_trigger):
    """
    - Check if the active player has a book (4 of equal rank)
      after each round
    """
    
    # Test output
    print("\n*** Function running: check_for_books() ***\n")
    print(f"Active player: {active_player}")
    # sleep(1)
    
    global player_hand
    global player_books
    global human_books
    global computer_books

    if active_player == "human":
        player_books = human_books
        player_hand = human_hand

        # Test output
        print("\n=== Checking for human books ===\n")
        print("Player hand is:", end=" ")
        print(*player_hand)
        print(f"\n=== Human book_check_trigger: {book_check_trigger} ===\n")

    elif active_player == "computer":
        player_books = computer_books
        player_hand = computer_hand
        print(f"\n=== Computer book_check_trigger: {book_check_trigger} ===\n")

        # Test output
        print("\n=== Checking for computer books ===\n")
        print("Player hand is:", end=" ")
        print(*player_hand)

    # Test output
    print(f"\n ====== book_check_trigger from check_for_books(): {book_check_trigger} ======\n")

    duplicate_ranks = [card for card in player_hand if book_check_trigger in card]

    # Test output
    if duplicate_ranks:
        print(f"Duplicates({len(duplicate_ranks)}):", end=" ")
        print(*duplicate_ranks)

    if len(duplicate_ranks) == 4:
        
        for card in duplicate_ranks:
            player_hand.remove(card)
        
        if active_player == "human":
            human_books += 1
        elif active_player == "computer":
            computer_books += 1
    return
    
    # sleep(0.5)


def stock_pile():
    """
    - # Cards left
    - Rank and suit of cards left
    """
    
    # Test output
    # print("\n*** Function running: stock_pile() ***\n")

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


def game_end():
    """
    - Game ends when either player's hand AND
      the stockpile are empty
    """
    
    # Test output
    print("\n*** Function running: game_end() ***\n")

    print("\n====== End of game ======\n")
    
    anounce_winner()
    play_again()


def anounce_winner():
    """
    - Display final scores
    - Anounce the winner
    """

    global human_books
    global computer_books

    # Test input
    # human_books = 6
    # computer_books = 7
    
    # Display winner/draw message
    if human_books > computer_books:
        message = ("\n*** Congratulations - You are the winner! ***\n")
    else:
        message = ("\n   *** Sorry - you lost this one! ***\n")

    # Display final scores
    print("*" * 45)
    print(message.upper())
    print("\n--------------- FINAL SCORES ----------------\n")
    print(f"    You: {human_books} books", end="        ")
    print(f"Computer: {computer_books} books\n")
    print("*" * 45)

    # Ask to play again
    play_again_input = input("\nDo you want to play again? Y/N ")

    if play_again_input.upper() == "Y":
        play_again()
    else:
        print("*** BYE! ***")
        sleep(5)
        quit()

    


def play_again():
    """
    - Reset all
    - Exclude rules & instructions
    """

    # Test output
    print("\n*** Function running: play_again() ***\n")

    # TEMP CLEAR SCREEN
    # Linux & OSX
    if os.name == "posix":
        os.system("clear")

    # Windows
    else:
        os.system("cls")

    global human_books
    global computer_books
    global deck
    human_books = 0
    computer_books = 0
    deck = []

    build_deck()
    shuffle_deck()
    deal_cards()
    play_game_round(active_player, opponent)

    




def main():
    """
    - Runs the main program functions
    """

# game = GoFish()

# game.new_game()


    # new_game()
    # game_rules()
    # play_game_round()
    # human_hand()
    # player_books()
    # stock_pile()
    # input_validation()
    # randomiser()
    # switch_player()
    # play_again()


# main()
# new_game()

active_player = "human"
opponent = "computer"

build_deck()
shuffle_deck()
deal_cards()
# play_game_round(active_player, opponent, book_check_trigger)
play_game_round(active_player, opponent)
# anounce_winner()
