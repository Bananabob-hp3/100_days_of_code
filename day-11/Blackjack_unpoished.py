import random
add = [30 + 31 + 30 + 31 + 10]
print(add)
print(30 + 31 + 30 + 31 + 10 + 30 + 31 + 30 + 31)

def deal_card():
    """Returns a random  card  from the deck"""
    cards = [11 , 2 ,3, 4, 5 , 6 , 7 , 8 ,9, 10, 10 , 10 , 10]
    card = random.choice(cards)
    return card
#deal_card()

player_cards = []
computer_cards = []

for _ in range(2):
    new_card = deal_card()
    player_cards.append(deal_card())
    computer_cards.append(deal_card())
#print(user_cards)
#print(computer_cards)
#user_cards += del_card 
#usker_cards.append(deal_card)
#user_cards.append(deal_card)
#computer_cards.append(deal_card)
#computer_cards.append(deal_card)
#print(user_cards)
#deck = [user_cards , computer_cards]
def calculate_score(cards):
    total = sum(cards)
    return total
player_cards = []
def first_two_cards():
    player_cards.append(deal_card())
    player_cards.append(deal_card())
    print(player_cards)
first_two_cards()
another_card = input("Do you want another card?y/n\n")
if another_card == "y":
    player_cards.append(deal_card())
player_score = sum(player_cards)

computer_cards = []
computer_cards.append(deal_card())
computer_cards.append(deal_card())
computer_score = sum(computer_cards)
while sum(computer_cards) < 17:
    computer_cards.append(deal_card())

def winner(player_cards , computer_cards):
    if player_score > 21 and computer_score > 21:
        return "both lost"
    elif player_score > 21 and computer_score < 21:
        return "computer wins"
    elif computer_score > 21 and player_score < 21:
        return "player wins"
    elif computer_score == 21 and player_score < 21:
        return "Computer got blackjack.computer wins"
    elif player_score == 21 and computer_score < 21:
        return "player got blackjack.player wins"
    elif player_score > computer_score and computer_score < 21:
        return "player wins"
    elif computer_score > player_score and computer_score < 21:
        return "computer wins"
    else:
        return" Draw"
print("Player cards:", player_cards)
print("Player score:", calculate_score(player_cards))

print("Computer cards:", computer_cards)
print("Computer score:", calculate_score(computer_cards))


print(winner(player_cards, computer_cards))

# create blackjack for ace card : when 2 cards total is less than is less than 10 make ace value as 11,if its greater then 10 make its value a sit is
sum_of_2 = sum(first_two_cards())
if first_two_cards() < 10:
    deal_cards() == 11
elif sum(first_two_cards > 10):
    deal_cards() == 1


#and this motherfucker tries to destroy my peace of mind me whole life , and why i cant fucking concentrate with fuck,,,,fbh nicotie addicts came to mo'fuckin house ,, motherfucker trying to bull
# i need a job by novemeber 2026 and august and september would be fine , its april , may , june , july left with 10 days of march as well 
# thats 30 + 31+ 30 + 31 + 10 = 
add = [30 + 31 + 30 + 31 + 10]
print(add)
