import os

from time import sleep

import random


class GoFish:
    """
    - Runs the entire game
    """

    def __init__(self):
        self.shuffled_deck = []
        self.human_hand = []
        self.human_books = 0
        self.player_books = 0
        self.computer_hand = []
        self.computer_books = 0
        self.duplicate_ranks = []
        self.stockpile_list = []
        self.player_hand = []
        self.requested_card = ""
        self.book_check_trigger = ""
        self.active_player = ""
        self.opponent = ""

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

        self.clear_screen()
        sleep(0.5)
        print("Go Fish!")
        print("\u2588")
        btn_top = "┌───────────────────────────────┐\n"
        btn_middle = "│ Press enter for game rules... │\n"
        btn_bottom = "└───────────────────────────────┘"
        input(btn_top + btn_middle + btn_bottom)

        self.clear_screen()
        self.game_rules()
        self.game_instructions()
        self.game_start()

    def game_start(self):
        """
        - Start the game once the human player is ready
        """

        start_game_input = input("When your're ready to play, press <ENTER>:\n")
        if start_game_input == "":
            self.build_deck()
        else:
            print("Input not recognised. Please press <ENTER>")
            self.game_start()

        self.build_deck()

    def build_deck(self):
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
        original_deck = []
        for suit in suit_list:
            for rank in rank_list:
                original_deck.append(rank + suit)

        # Shuffle the deck
        shuffled_deck = []
        random.shuffle(original_deck)

        for card in original_deck:
            shuffled_deck.append(card)

        # Deal cards
        self.deal_cards(shuffled_deck)

    def deal_cards(self, shuffled_deck):
        """
        - Add 7 cards to computer's hand
        - Add 7 cards to player's hand
        - Add remainder to the stockpile
        """

        # stockpile_list = []
        counter = 1
        while counter <= 14:
            deck_count = len(shuffled_deck)
            card_to_deal = shuffled_deck[0]

            # Deal even cards to computer hand
            if deck_count % 2 == 0:
                self.player_hand = self.computer_hand

            # Deal odd cards to human hand
            else:
                self.player_hand = self.human_hand
            
            # Add dealt card to relevant player's hand
            self.player_hand.append(card_to_deal)

            # Remove dealt card from deck
            shuffled_deck.remove(card_to_deal)
            counter += 1
        
        # After dealing player hands,
        # add remaining cards to stockpile
        self.stockpile_list.extend(shuffled_deck)

        # Group cards together by rank for readability
        self.human_hand.sort()

        active_player = "human"
        opponent = "computer"
        human_hand = self.human_hand
        computer_hand = self.computer_hand
        human_books = self.human_books
        computer_books = self.computer_books
        book_check_trigger = random.choice(self.player_hand)
        
        # self.check_for_books(active_player, book_check_trigger, human_books, computer_books)
        # Check for books, in case a player was dealt
        # 4 cards of equal rank
        self.check_for_books(active_player, book_check_trigger)

        # self.play_game_round(active_player, opponent, stockpile_list,
        #                      human_hand, computer_hand,
        #                      human_books, computer_books)
        self.play_game_round(active_player, opponent,
                             human_books, computer_books)

    def draw_from_stockpile(self, active_player, opponent, stockpile_list,
                            human_books, computer_books):
        """
        - Draw a card from the stockpile
        - Add card to active player's hand
        """
        
        self.human_books = human_books
        self.computer_books = computer_books

        # Test output
        print("\n*** Function running: draw_from_stockpile() ***\n")
        print(f"stockpile_list: {stockpile_list}")

        print("\n=== Drawing a card from the stockpile... ===\n")
        if self.stockpile_list == [] and self.player_hand == []:
            self.game_end()
        else:
            drawn_card = stockpile_list[0]

        # Test output
        print(f"Card drawn from stockpile: {drawn_card}")

        book_check_trigger = drawn_card[:1]
        
        if active_player == "human":
            print(f"\n=== Human drew: {drawn_card}")
            self.human_hand.append(drawn_card)
            print("\n=== Adding card to human hand ===\n")
            print(f"\n====== book_check_trigger from draw_from_stockpile(): {book_check_trigger}")
        else:
            print(f"\n=== Computer drew: {drawn_card}")
            self.computer_hand.append(drawn_card)
            print("\n=== Adding card to computer hand ===\n")
            print(f"\n====== book_check_trigger from draw_from_stockpile(): {book_check_trigger}")
    
        # End the game if both the stockpile and a player's hand are empty
        if stockpile_list == [] and self.player_hand == []:
            self.game_end()
        else:
            stockpile_list.remove(drawn_card)
        
        # self.check_for_books(active_player, book_check_trigger, human_books, computer_books)
        self.check_for_books(active_player, book_check_trigger)
        self.switch_player(active_player, opponent)

    def switch_player(self, active_player, opponent):
        """
        Switch active player after turn has finished
        """

        print(f"Active player (switch_player start):  {active_player}")

        # stockpile_list = self.stockpile_list
        # human_hand = self.human_hand
        # computer_hand = self.computer_hand
        human_books = self.human_books
        computer_books = self.computer_books

        if active_player == "human":
            active_player = "computer"
            opponent = "human"
            print("=== It is the computer's turn to play ===")

        else:
            active_player = "human"
            opponent = "computer"
            print("=== It is your turn to play ===")

        # Test output
        print(f"Active player (switch_player end):  {active_player}")

        # self.play_game_round(active_player, opponent, stockpile_list,
        #                      human_hand, computer_hand,
        #                      human_books, computer_books)
        self.play_game_round(active_player, opponent,
                             human_books, computer_books)

    # def play_game_round(self, active_player, opponent, stockpile_list,
    #                     human_hand, computer_hand,
    #                     human_books, computer_books):
    def play_game_round(self, active_player, opponent,
                        human_books, computer_books):
        """
        Keep track of:
        - Human hand
        - Computer hand
        - Human books
        - Computer books
        - Stockpile
        - Card requests
        """

        # self.human_books = human_books
        # self.computer_books = computer_books

        # Test output
        print("*** play_game_round START\n")
        print(f"Human books: {self.human_books}")
        print(f"Computer books: {self.computer_books}\n")


        # Display scoreboard
        self.score_board(active_player)

        # Group ranks together for readability
        self.human_hand.sort()

        if active_player == "human":
            human_input = input("\nWhich card would you like to request? ")
            requested_card = human_input.upper()
            print(f"\nYou requested: {requested_card}")
            book_check_trigger = requested_card

        else:
            if len(self.computer_hand) >= 1:
                random_card = random.choice(self.computer_hand)
            else:
                random_card = str(random.choice([2, 10]))
            requested_card = random_card[:-1]
            book_check_trigger = requested_card
            print(f"\nThe computer requested: {requested_card}\n")
            sleep(2)

        book_check_trigger = requested_card

        self.check_hand(active_player, opponent,
                        requested_card, book_check_trigger,
                        human_books, computer_books)

        self.check_for_books(active_player, book_check_trigger)

    def check_hand(self, active_player, opponent, requested_card, 
                   book_check_trigger, human_books, computer_books):
        """
        - Check hand for requested card otherwise
        draw a card from the stockpile
        """
        
        # human_hand = self.human_hand
        # computer_hand = self.computer_hand
        human_books = self.human_books
        computer_books = self.computer_books

        stockpile_list = self.stockpile_list

        if active_player == "human":
            self.player_hand = self.human_hand
            self.opponent_hand = self.computer_hand
        else:
            self.player_hand = self.computer_hand
            self.opponent_hand = self.human_hand
        
        match = [card for card in self.opponent_hand if requested_card in card]

        singular_plural = ""
        if len(match) == 1:
            singular_plural = "card"
        else:
            singular_plural = "cards"

        if match:
            print(f"The {opponent} is handing over {len(match)} {singular_plural}.")
            self.player_hand.extend(match)
            # self.check_for_books(active_player, book_check_trigger, human_books, computer_books)
            self.check_for_books(active_player, book_check_trigger)
        else:
            print(f"\n=== The {opponent} doesn't have that card. ===\n")
            sleep(0.5)
            # self.draw_from_stockpile(active_player, opponent, stockpile_list)
            self.draw_from_stockpile(active_player, opponent, stockpile_list,
                                     human_books, computer_books)

        for card in match:
            self.opponent_hand.remove(card)

        self.player_hand.sort()

        # self.play_game_round(active_player, opponent, stockpile_list,
        #                      human_hand, computer_hand,
        #                      human_books, computer_books)
        self.play_game_round(active_player, opponent,
                             human_books, computer_books)

    def check_for_books(self, active_player, book_check_trigger):
        """
        - Check if the active player has a book (4 of equal rank)
        after each round
        """

        if active_player == "human":
            player_books = self.human_books
            player_hand = self.human_hand

            # Test output
            print("\n=== Checking for human books ===\n")

        elif active_player == "computer":
            player_books = self.computer_books
            player_hand = self.computer_hand

            print(f"\n=== Computer book_check_trigger: {book_check_trigger} ===\n")

            # Test output
            print("\n=== Checking for computer books ===\n")

        duplicate_ranks = [card for card in self.player_hand
                           if book_check_trigger in card]

        if len(duplicate_ranks) == 4:
            
            for card in duplicate_ranks:
                player_hand.remove(card)
            
            if active_player == "human":
                self.human_books += 1

            elif active_player == "computer":
                self.computer_books += 1
        
        # End the game if all 13 books have been won
        if self.human_books + self.computer_books == 13:
            self.game_end()
        return self.human_books, self.computer_books
        # sleep(0.5)

    def score_board(self, active_player):

        """
        - Display active player, human hand and book count for both players
        """

        # human_books = self.human_books
        # computer_books = self.computer_books
        
        print("\n")
        print("┌──────────────────────────────────────────────────────────┐")
        print("│                       SCORE BOARD                        │")
        print("└──────────────────────────────────────────────────────────┘")
        print(f"│   Active player: {active_player}                                   │")
        print("│                                                          │")
        print("│                                                          │")
        print("│   Human hand:", end=" ")
        print(*self.human_hand, end=" ")
        print("                      │")
        print("│                                                          │")
        print("│                                                          │")
        print(f"│   Human books: {self.human_books}                     Computer books: {self.computer_books}   │")
        print("└──────────────────────────────────────────────────────────┘")


    # def stock_pile(self):
    #     """
    #     - # Cards left
    #     - Rank and suit of cards left
    #     """
        
    #     # Test output
    #     print("\n*** Function running: stock_pile() ***\n")

    #     if self.stockpile_list == [] and self.computer_hand == []:
    #         self.game_end()

    def input_validation(self):
        """
        Check for:
        - Format
        - Case
        - Range
        """

        # Test output
        print("\n*** Function running: input_validation() ***\n")

    def game_end(self):
        """
        - Game ends when either player's hand AND
        the stockpile are empty
        """
        print("\n====== End of game ======\n")
        
        self.anounce_winner()
        self.play_again()

    def anounce_winner(self):
        """
        - Display final scores
        - Anounce the winner
        """
        
        # Display win/lose message
        if self.human_books > self.computer_books:
            message = ("\n*** Congratulations - You are the winner! ***\n")
        else:
            message = ("\n   *** Sorry - you lost this one! ***\n")

        # Display final scores
        print("*" * 45)
        print(message.upper())
        print("\n--------------- FINAL SCORES ----------------\n")
        print(f"    You: {self.human_books} books", end="        ")
        print(f"Computer: {self.computer_books} books\n")
        print("*" * 45)

        # Ask to play again
        play_again_input = input("\nDo you want to play again? Y/N ")

        if play_again_input.upper() == "Y":
            self.human_books = 0
            self.computer_books = 0
            self.play_again()
        else:
            print("*** BYE! ***")
            sleep(5)
            quit()

    def play_again(self):
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

        self.human_hand.clear()
        self.computer_hand.clear()

        self.build_deck()
        # deal_cards()
        # play_game_round(active_player, opponent, stockpile_list)


def main():
    """
    - Runs the main program functions
    """
    game = GoFish()
    game.new_game()

# Function trace
# def tracefunc(frame, event, arg, indent=[0]):
#       if event == "call":
#           indent[0] += 2
#           print("-" * indent[0] + "> call function", frame.f_code.co_name)
#       elif event == "return":
#           print("<" + "-" * indent[0], "exit function", frame.f_code.co_name)
#           indent[0] -= 2
#       return tracefunc
# import sys
# sys.setprofile(tracefunc)
main()

