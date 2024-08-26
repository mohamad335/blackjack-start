import random
def deal_card():
  card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  cards = random.choice(card)
  return cards
def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) >21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
deal_card = []
computer_card = []
game_over = False
while not game_over:
  for _ in range(2):
    
    deal_card.append(deal_card())
    computer_card.append(deal_card())
  print(f"your cards: {deal_card}, current score: {calculate_score(deal_card)}") 
  print(f"copmuter's first card: {computer_card[0]}, current score: {calculate_score(computer_card)}")
  if calculate_score(deal_card) == 0 or calculate_score(computer_card) == 0 or calculate_score(deal_card) > 21:
    game_over = True
  else:
    if input("type 'y' to get another card, type 'n' to pass: ")== "y":
      deal_card.append(deal_card())
    else:
      game_over = True
while calculate_score(computer_card) != 0 and calculate_score(computer_card) < 17:
  computer_card.append(deal_card())
print(f"your final hand: {deal_card}, final score: {calculate_score(deal_card)}")
print(f"computer's final hand: {computer_card}, final score: {calculate_score(computer_card)}")

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


