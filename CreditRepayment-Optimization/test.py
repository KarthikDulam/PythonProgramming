budget = 800.0
num_cards = int(input())
cards = []
for i in range(num_cards):
    card = {}
    card['cardNickName']= card.get('cardNickName','')+ input()
    card['cardBalance']= card.get('cardBalance',0)+ float(input())
    cards.append(card)
    print(cards)