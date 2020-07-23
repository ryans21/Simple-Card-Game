import time
from time import sleep
import random
from random import choice
from pyfiglet import Figlet

deck = {
    'Two of Diamonds': 2,
    'Two of Spades': 2,
    'Two of Clubs': 2,
    'Two of Hearts': 2,
    'Three of Diamonds': 3,
    'Three of Spades': 3,
    'Three of Clubs': 3,
    'Three of Hearts': 3,
    'Four of Diamonds': 4,
    'Four of Spades': 4,
    'Four of Clubs': 4,
    'Four of Hearts': 4,
    'Five of Diamonds': 5,
    'Five of Spades': 5,
    'Five of Clubs': 5,
    'Five of Hearts': 5,
    'Six of Diamonds': 6,
    'Six of Spades': 6,
    'Six of Clubs': 6,
    'Six of Hearts': 6,
    'Seven of Diamonds': 7,
    'Seven of Spades': 7,
    'Seven of Clubs': 7,
    'Seven of Hearts': 7,
    'Eight of Diamonds': 8,
    'Eight of Spades': 8,
    'Eight of Clubs': 8,
    'Eight of Hearts': 8,
    'Nine of Diamonds': 9,
    'Nine of Spades': 9,
    'Nine of Clubs': 9,
    'Nine of Hearts': 9,
    'Ten of Diamonds': 10,
    'Ten of Spades': 10,
    'Ten of Clubs': 10,
    'Ten of Hearts': 10,
    'Jack of Diamonds': 10,
    'Jack of Spades': 10,
    'Jack of Clubs': 10,
    'Jack of Hearts': 10,
    'Queen of Diamonds': 10,
    'Queen of Spades': 10,
    'Queen of Clubs': 10,
    'Queen of Hearts': 10,
    'King of Diamonds': 10,
    'King of Spades': 10,
    'King of Clubs': 10,
    'King of Hearts': 10,
    'Ace of Diamonds': 11,
    'Ace of Spades': 11,
    'Ace of Clubs': 11,
    'Ace of Hearts': 11
}

yesses = ['Y' , 'y', 'yes', 'YES']
nos = ['N', 'n', 'no', 'NO']

def main():
    intro()
    while True:
        GameLoop()
        ans = str(input("Would you like to play blackjack again?"))
        if ans in yesses:
            continue
        if ans in nos:
            break
    

def intro():
    start_text = Figlet(font = 'big')
    rule_text = Figlet(font = 'straight')
    print("Welcome to...")
    time.sleep(1)
    print(start_text.renderText("BLACKJACK!"))
    time.sleep(2)
    print("This python commandline application of Blackjack;")
    time.sleep(1)
    print("It is as similar to the real-life version of Blackjack as possible;")
    time.sleep(1)
    print(rule_text.renderText("HOW TO PLAY: "))
    time.sleep(2)
    print("The objective of the game is to amass a card value of 21 or as close to 21 as going over 21 will result in a loss;")
    time.sleep(2)
    print("You will draw cards from a randomized deck with certain rules:")
    time.sleep(2)
    print("All royal cards = 10, No Jokers, and Aces only = 11.")
    time.sleep(2)
    print(start_text.renderText("LETS PLAY!"))
    time.sleep(3)

def GameLoop():

    #Creates mutable list copy of the deck
    current_deck = list(deck)

    #Draws 2 cards and removes them from the current deck
    card1 = random.sample(current_deck, 1)[0]
    current_deck.remove(card1)
    card2 = random.sample(current_deck, 1)[0]
    current_deck.remove(card2)

    #Draws the dealers cards
    dealer_card1 = random.sample(current_deck, 1)[0]
    current_deck.remove(dealer_card1)
    dealer_card2 = random.sample(current_deck, 1)[0]
    current_deck.remove(dealer_card2)

    #Creates dealer total
    dealer_total = deck.get(dealer_card1) + deck.get(dealer_card2)
    card_count = 1

    if dealer_total < 17:
        dealer_card3 = random.sample(current_deck, 1)[0]
        current_deck.remove(dealer_card3)
        dealer_total += deck.get(dealer_card3)
        card_count += 1

    #Returns the users draws w/ their value
    total = deck.get(card1) + deck.get(card2)
    print('You have drawn the ' + str(card1) + ' and the ' + str(card2) + ';\nTotal : ' + str(total))
    time.sleep(1)

    #Display what the dealer has drawn
    print('The dealer has drawn a ' + str(dealer_card1) + ' and ' + str(card_count) + ' other unkown card')

    #Case for immediate black jack
    if total == 21:
        print("Congratualtions you have won blackjack!")
        
    
    #The game loop for hitting
    while True:
        decision = str(input("Your current total is " + str(total) + ".\nWould you like to hit(Y/N)?: "))
        if decision in yesses:
            hit_card = random.sample(current_deck, 1)[0]
            current_deck.remove(hit_card)
            total += deck.get(hit_card)
            print('You have drawn the ' + str(hit_card) + ';\nTotal : ' + str(total))
            if total >= 21:
                print("You have gone over 21 and have lost")
                break
        else:
            break
    
    res = results(total, dealer_total)

    time.sleep(1)

    if res == 'p':
        print("The player has won the game!")

    if res == 'd':
        print("The house has won the game with a total of " + str(dealer_total) + " !")

    if res == 'n':
        print("The result is a draw neither have won...")

def results(player, dealer):
    #Over 21 For both
    if dealer > 21:
        if player <= 21:
            return 'p'
        if player > 21:
            return 'd'
    if player > 21:
        if dealer <= 21:
            return 'd'
    if player < dealer:
        return 'd'
    if dealer < player:
        return 'p'
    if dealer == player:
        return 'd'
    
if __name__ == "__main__":
    main()




