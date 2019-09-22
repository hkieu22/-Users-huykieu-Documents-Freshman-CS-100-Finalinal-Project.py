import random

deckOfCard = [1,2,3,4,5,6,7,8,9,10,11,12,13]*4

def dealCards(deck):
    hand=[]
    random.shuffle(deckOfCard)
    for i in range(0,2):
        card = deckOfCard.pop()
        if card == 1:
            card = "A"
        if card == 11:
            card = "J"
        if card == 12:
            card = "Q"
        if card == 13:
            card = "K"
        hand.append(card)
    return hand

def summ(hand):
    t = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            t = t+10
        elif card == "A":
            if t >= 11: 
                t = t+1
            else: 
                t = t+11
        else:
            t = t + card
    return t

def hit(hand):
    card = deckOfCard.pop()
    if card == 1:
        card = "A"
    if card == 11:
        card = "J"
    if card == 12:
        card = "Q"
    if card == 13:
        card = "K"
        
    hand.append(card)
    
    return hand
	
def result(handOfDealer,handOfPlayer):
    print("Dealer has " + str(handOfDealer) + ". Dealer's sum is " + str(summ(handOfDealer)))
	
    print("You have " + str(handOfPlayer) + ". Your sum is " + str(summ(handOfPlayer)))

def playAgain():
    playAgain = input("Keep playing? (Yes or No) : ")

    while playAgain == "Yes":
        handOfDealer = []
        handOfPlayer = []
        playgame()
    

    print("Thank you for playing! Goodbye!")

    return False


def blackjack(handOfDealer,handOfPlayer):
    if summ(handOfPlayer) == 21:
        result(handOfDealer,handOfPlayer)
        print("You got a Blackjack! You win!\n")
        playAgain()
        
    elif summ(handOfDealer) == 21:
        result(handOfDealer,handOfPlayer)		
        print("You lose! The dealer got a blackjack.\n")
        playAgain()
    
    else:
        return False

def rule(handOfDealer,handOfPlayer):
    if summ(handOfPlayer) == 21:
        result(handOfDealer,handOfPlayer)
        print("You got a Blackjack! You win!\n")
    elif summ(handOfDealer) == 21:
        result(handOfDealer,handOfPlayer)
        print("You lose! The dealer got a blackjack.\n")
    elif summ(handOfPlayer) > 21:
        result(handOfDealer,handOfPlayer)
        print("You busted. You lose this game.\n")
    elif summ(handOfDealer) > 21:
        result(handOfDealer,handOfPlayer)
        print("Dealer busted. You win this game!\n")
    elif summ(handOfPlayer) < summ(handOfDealer):
        result(handOfDealer,handOfPlayer)
        print("Your point is lower than the dealer. You lose this game.\n")
    elif summ(handOfPlayer) > summ(handOfDealer):
        result(handOfDealer,handOfPlayer)
        print("Your point is higher than the dealer. You win this game\n")	
    else: #sum(handOfPlayer) == sum(handOfDealer)
        result(handOfDealer,handOfPlayer)
        print("Push")

    playAgain()
        
def playgame():
    decision = 0	
    print ("Let's play Blackjack!\n")
    handOfDealer = dealCards(deckOfCard)
    handOfPlayer = dealCards(deckOfCard)
      
    while decision!= "q":
        print("The dealer has a " + str(handOfDealer[0]))
        print("You have " + str(handOfPlayer) + ". Your sum is " + str(summ(handOfPlayer)))
        blackjack(handOfDealer,handOfPlayer)
        decision = input("Do you want to Hit or Stand?: ")
        if decision == "Hit":
            hit(handOfPlayer)
            
            while summ(handOfDealer) < 17:
                hit(handOfDealer)
                rule(handOfDealer,handOfPlayer)
                playAgain()
                
        if decision == "Stand":
            while summ(handOfDealer) < 17:
                hit(handOfDealer)
                rule(handOfDealer,handOfPlayer)
                playAgain()
            rule(handOfDealer,handOfPlayer)
    
    else:
        return False

playgame()