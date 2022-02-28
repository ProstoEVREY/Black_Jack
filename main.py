#black jack game, where in the end, you will lose anyway )))
import random
import sys
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
game_is_played = True
sum_on_board = 0
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]
    def __str__(self):
        return "{} of {}".format(self.suit,self.rank)
class Deck:
    def __init__(self):
        self.allcards = []
        for suit in suits:
            for rank in ranks:
                self.allcards.append(Card(suit,rank))
    def shuffledeck(self):
        random.shuffle(self.allcards)
    def pop_one(self):
        if(self.allcards == []):
            print("No more cards left!")
            sys.exit()
        else:
            return self.allcards.pop(0)
    def __str__(self):
        return f"This deck now has {len(self.allcards)}"
class Player:

    def __init__(self):
        self.hand = []
        self.deposit = 200
    def dep_up(self,sum):
        self.deposit+=sum
    def bet(self,sum):
        global sum_on_board
        sum_on_board += sum
        self.deposit-=sum
    def __str__(self):
        return "The player now has {} dollars deposit".format(self.deposit)


deck1 = Deck()
deck1.shuffledeck()
pl1 = Player()
while(game_is_played):
    print("Welcome to the Jack Black!")
    betting = True
    while(betting):
        if(pl1.deposit==0):
            print("You lost! Your wallet is empty!")
            sys.exit()
        else:
            bet = input("Please, place your bet: ")
            try:
                if(float(bet)>pl1.deposit):
                    print("Cannot bet that much!")
                    continue
            except Exception:
                continue
            pl1.bet(float(bet))
            betting = False
    print("You are given two cards!")
    pl1.hand.append(deck1.pop_one())
    pl1.hand.append(deck1.pop_one())
    playing = True
    while(playing):
        counter = 0
        for card in pl1.hand:
            if(card.rank == "Ace" and (counter+11) >21):
                counter+=1
            else:
                counter+=card.value
        if(counter>21):
            print("You have lost! It is more than 21")
            pl1.hand = []
            computer_hand = []
            break
        elif(counter==21):
            print("You have won! You have 21! ")
            pl1.hand = []
            computer_hand = []
            break
        else:
            print("Here are the cards you have:")
            for card in pl1.hand:
                print(card)
                print(f" (card value is '{card.value}')")

            choice = input("Do you want to stay or hit? ")
            if(choice=="hit".lower()):
                pl1.hand.append(deck1.pop_one())
            else:
                computer_hand = []
                computer_hand.append(deck1.pop_one())
                computer_hand.append(deck1.pop_one())
                counter2 = 0
                for card in computer_hand:
                    if (card.rank == "Ace" and (counter2 + 11) > 21):
                        counter2 += 1
                    else:
                        counter2 += card.value
                if(counter2>counter):
                    print("You lose! Computer has higher count!")
                    sum_on_board = 0
                    pl1.hand = []
                    computer_hand = []
                    break
                while(counter2<counter):
                    computer_hand.append(deck1.pop_one())
                    for card in computer_hand:
                        if (card.rank == "Ace" and (counter2 + 11) > 21):
                            counter2 += 1
                        else:
                            counter2 += card.value
                    if(counter2>21):
                        print("You win! Computer has lost!")
                        pl1.dep_up(2*sum_on_board)
                        sum_on_board=0
                        playing = 0
                        pl1.hand = []
                        computer_hand = []
                        break
                    elif(counter2>counter and counter2<=21):
                        print("You lose! Computer has higher values!")
                        break
                    else:
                        continue












