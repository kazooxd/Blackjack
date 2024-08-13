import art
import random


def blackjack():
    print(art.logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = []
    computer_cards = []

    card1 = random.choice(cards)
    card2 = random.choice(cards)
    computer_card1 = random.choice(cards)
    computer_card2 = random.choice(cards)

    game_on = True

    player_cards.extend([card1, card2])
    computer_cards.append(computer_card1)

    current_score = sum(player_cards)
    computer_score = sum(computer_cards)

    print(f"Your cards are {player_cards}, current score: {current_score}")
    print(f"Computer's first card is: {computer_cards}\n")

    while game_on and current_score < 21:
        player_choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if player_choice == "y":
            new_player_card = random.choice(cards)
            if new_player_card == 11:
                ace = int(input("You got an Ace, do you wanna consider it as 1 or 11?: "))
                if ace == 1:
                    new_player_card = 1
                else:
                    new_player_card = 11
            new_computer_card = random.choice(cards)
            computer_cards.append(new_computer_card)
            player_cards.append(new_player_card)
            current_score = sum(player_cards)
            computer_score = sum(computer_cards)
            print(f"Your cards are {player_cards}, current score: {current_score}")
            print(f"Computer's card are {computer_cards}, current score {computer_score}\n")

        else:
            while computer_score < 17:
                new_computer_card = random.choice(cards)
                computer_cards.append(computer_card2)
                computer_score = sum(computer_cards)
            game_on = False
            print(f"Your final cards are {player_cards}, final score: {current_score}")
            print(f"Computer's final hand is {computer_cards}, final score: {computer_score}\n")

    if current_score > computer_score and current_score < 21:
        game_on = False
        print("Your score is higher and under 21. You won!\n")

    elif current_score == 21:
        game_on = False
        print("Your score is exactly 21. You won!\n")

    elif current_score == computer_score:
        game_on = False
        print("You have the same score as the computer. It's a draw!\n")

    elif current_score > 21:
        game_on = False
        print("You went over 21. You lost!\n")

    elif current_score < computer_score and computer_score < 21:
        game_on = False
        print("Computer wins!")

    elif computer_score > 21:
        game_on = False
        print("Computer went over. You won!\n")

    play_again = input("If you wanna play again type 'y', if not type 'n': ")

    if play_again == "y":
        blackjack()


blackjack()