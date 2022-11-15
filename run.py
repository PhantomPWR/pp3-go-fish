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
        self.computer_hand = []
        self.opponent_hand = []
        self.human_books = 0
        self.player_books = 0
        self.computer_books = 0
        self.duplicate_ranks = []
        self.stockpile_list = []
        self.player_hand = []
        self.requested_card = ""
        self.book_check_trigger = ""
        self.active_player = ""
        self.text_to_remove = ""

    def welcome(self):
        """
        - Display the welcome screen
        """
        print("*" * 80)
        print("*")
        print("*")
        print("*")
        print("*")
        print("*")
        print("*")
        print("*")
        print("*")
        print("*")
        print("*")
        print("*")
        print("*")
        print("*")
        print("*")
        print("*")
        print("*")
        print("*")
        print("*")
        print("*")
        print("*")
        print("*")
        print("*")
        print("*")

    def clear_screen(self):
        """
        - Detect operating system and run relevant
          "clear screen" command
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
    RULES OF GO FISH!
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
    - The remaining cards are placed face down\
 on the table to form the stockpile
        """
        print(rules_pt1)
        self.continue_prompt()

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
    - A player has an empty hand and there are no cards left in \
the stockpile

        """
        print(rules_pt2)
        self.continue_prompt()

    def game_instructions(self):

        """
        - Game instructions
        """

        instructions = """
    INSTRUCTIONS
    ------------

    1. Enter the rank of the card you wish to request from the computer
    2. For number(rank) cards, you enter 2 to 10
    3. For court cards (Jack, Queen, King & Ace), enter either the full name \
or the first letter, e.g. Q or Queen
    4. If you need to review the rules & instructions during the game,
       enter either "H" or "Help" when it's your turn too request a card
    5. To exit during the game enter either "E" or "Exit"
    7. After the game has ended, enter either:
       - "Y" or "Yes" to play again or
       - "N" or "No" to exit the game
        """

        print(instructions)
        print("-" * 80)

    def continue_prompt(self):
        """
        - Lets the user press <ENTER> to continue
        - Once <ENTER> has been pressed, delete the prompt to avoid confusion
        """

        # Continue when the user presses <ENTER>
        input("Press <ENTER> to continue...")

        # Delete the "Press <ENTER>..." text
        print("\033[A\033[A")
        print("\033[A\033[A")

    def new_game(self):
        """
        - Display game rules & instructions
        - Reset # books
        - Deal hands
        - Set stockpile
        """

        self.clear_screen()
        print("Welcome to Go Fish!")

        self.clear_screen()
        self.game_rules()
        self.game_instructions()
        self.game_start()

    def game_start(self):
        """
        - Start the game once the human player is ready
        """

        start_game_input = input("When your're ready to play, \
press <ENTER>:\n")
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
        human_books = self.human_books
        computer_books = self.computer_books
        book_check_trigger = random.choice(self.player_hand)

        self.check_for_books(active_player, book_check_trigger)

        self.play_game_round(active_player, opponent,
                             human_books, computer_books)

    def draw_from_stockpile(self, active_player, stockpile_list,
                            human_books, computer_books):
        """
        - Draw a card from the stockpile
        - Add card to active player's hand
        """

        self.human_books = human_books
        self.computer_books = computer_books

        self.score_board(active_player)
        if not self.stockpile_list and not self.player_hand:
            self.game_end()
        else:
            drawn_card = stockpile_list[0]

        # Use the drawn card's rank to trigger
        #  checking for books
        book_check_trigger = drawn_card[:1]

        if active_player == "human":
            print(f"\nYou drew a {drawn_card} from the stockpile.")
            self.human_hand.append(drawn_card)

        else:
            print("\nThe computer drew a card from the stockpile")
            self.computer_hand.append(drawn_card)
        sleep(1)

        # End the game if both the stockpile and a player's hand are empty
        if len(stockpile_list) == 0 and not self.player_hand:
            self.game_end()
        else:
            stockpile_list.remove(drawn_card)
       
        self.check_for_books(active_player, book_check_trigger)
        self.switch_player(active_player)

    def switch_player(self, active_player):
        """
        Switch active player after turn has finished
        """

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
        sleep(1.5)

        self.play_game_round(active_player, opponent,
                             human_books, computer_books)

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

        # Display scoreboard
        self.score_board(active_player)

        # Group ranks together for readability
        self.human_hand.sort()

        if active_player == "human":
            human_input = input("\nWhich card would you like to ask for? ")
            requested_card = human_input.capitalize()
            if requested_card in ("Help", "H"):
                self.input_validation(requested_card)
                self.game_rules()
                self.game_instructions()
                input("Press <enter> to continue...")
                self.play_game_round(active_player, opponent,
                                     human_books, computer_books)
            elif requested_card in ("Exit", "E"):
                self.input_validation(requested_card)
                print("Thanks for playing!")
                print("*** BYE! ***")
                sleep(2)
                quit()
            else:
                self.input_validation(requested_card)
                print(f"\nYou asked for {requested_card}s")
                sleep(1)
                book_check_trigger = requested_card

        else:
            if len(self.computer_hand) >= 1:
                random_card = random.choice(self.computer_hand)
            else:
                random_card = str(random.choice([2, 10]))
            requested_card = random_card[:-1]
            book_check_trigger = requested_card
            print(f"\nThe computer asked for {requested_card}s\n")
            sleep(0.5)

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

        # Handle message grammar
        plural = ""
        singular = ""
        card_count = ""
        if len(match) > 1:
            plural = "s"
            singular = ""
            card_count = str(len(match))
        else:
            singular = "one"
            plural = ""
            card_count = ""

        if match:
            if active_player == "computer":
                print(f"You are handing over {singular}{card_count} \
{book_check_trigger}{plural}.")

            else:
                print(f"The computer is handing over {singular}{card_count} \
{book_check_trigger}{plural}.")
            sleep(1)
            self.player_hand.extend(match)
            self.check_for_books(active_player, book_check_trigger)
        else:
            if active_player == "computer":
                print(f"\n=== You don't have any {book_check_trigger}s. ===\n")
            else:
                print(f"\n=== The computer doesn't have any \
{book_check_trigger}s. ===\n")
            sleep(1.5)

            self.draw_from_stockpile(active_player, stockpile_list,
                                     human_books, computer_books)

        for card in match:
            self.opponent_hand.remove(card)

        self.player_hand.sort()

        self.play_game_round(active_player, opponent,
                             human_books, computer_books)

    def check_for_books(self, active_player, book_check_trigger):
        """
        - Check if the active player has a book (4 of equal rank)
        after each round
        """

        if active_player == "human":
            player_hand = self.human_hand

        elif active_player == "computer":
            player_hand = self.computer_hand

        self.score_board(active_player)
        sleep(1)

        duplicate_ranks = [card for card in self.player_hand
                           if book_check_trigger in card]

        if len(duplicate_ranks) == 4:
            
            for card in duplicate_ranks:
                player_hand.remove(card)
            
            if active_player == "human":
                self.human_books += 1
                print("\n*** You have a book! ***\n")

            elif active_player == "computer":
                self.computer_books += 1
                print("\n*** The computer has a book! ***\n")
            sleep(1)
        
        # End the game if all 13 books have been won
        if self.human_books + self.computer_books == 13:
            self.game_end()
        return self.human_books, self.computer_books

    def score_board(self, active_player):

        """
        - Display active player, human hand and book count for both players
        """

        if active_player == "human":
            player_display = "YOU"
        elif active_player == "computer":
            player_display = "COMPUTER"
        
        print("\n" * 10)
        print("┌──────────────────────────────────────────────────────────────\
────────────────┐")
        print("│                                 SCOREBOARD                   \
                │")
        print("└──────────────────────────────────────────────────────────────\
────────────────┘")
        print("\n")
        print(f"   Active player: {player_display}")
        print("\n")
        print("   Your hand:")
        print("\n  ", *self.human_hand, end=" ")
        print("\n")
        print("───────────────────────────────────────────────────────────────\
─────────────────")
        print(f"   Your books: {self.human_books}                             \
              Computer books: {self.computer_books}")
        print("===============================================================\
=================")
        print("\n")
        print("   MESSAGES                                   H - Game Rules   \
E - Exit game")
        print("───────────────────────────────────────────────────────────────\
─────────────────")

    def input_validation(self, requested_card):
        """
        Check for:
                - Format
                - Case
                - Range
        """
        court_card_list = ["Ace", "King", "Queen", "Jack"]
        if requested_card in court_card_list:
            requested_card = requested_card[:1]
            sleep(0.5)
            return requested_card

        valid_input_list = ["Ace",
                            "King",
                            "Queen",
                            "Jack",
                            "A",
                            "K",
                            "Q",
                            "J",
                            "10",
                            "9",
                            "8",
                            "7",
                            "6",
                            "5",
                            "4",
                            "3",
                            "2",
                            "H",
                            "Help",
                            "E",
                            "Exit",
                            "Y"]
        if requested_card not in valid_input_list:
            print(f"*** {requested_card} is not a valid option. Please try \
again. ***")
            sleep(1)
            self.play_game_round("human", "computer",
                                 self.human_books, self.computer_books)
        else:
            return requested_card

    def game_end(self):
        """
        - Game ends when either player's hand AND
        the stockpile are empty
        """
        print("*** THE GAME HAS ENDED ***")
        sleep(1)
        self.clear_screen()
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
      
        # Yes, play again
        if play_again_input.upper() == "Y":

            # Reset book scores
            self.human_books = 0
            self.computer_books = 0
            self.play_again()
        else:
            # No - quit game
            print("*** BYE! ***")
            sleep(2)
            quit()

    def play_again(self):
        """
        - Reset all scores
        - Build a new deck
        - Exclude rules & instructions
        """

        # Clear screen
        self.clear_screen()
        
        # Reset scores
        self.human_hand.clear()
        self.computer_hand.clear()

        # Build a new deck
        self.build_deck()


def main():
    """
    - Runs the main program functions
    """
    game = GoFish()
    game.new_game()
    # game.welcome()


main()
