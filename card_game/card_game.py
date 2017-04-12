# -*- coding: utf-8 -*-
from random import randint

cards = {
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'J' : 11,
    'Q' : 12,
    'K' : 13,
    'A' : 14
    }
suits = ('♠', '♣', '♥', '♦')

def all_cards_gen():
    global all_cards
    for suit in suits:
        for card in cards.keys():
            all_cards.append((card, suit))
    return all_cards

# generate cards for user
def user_cards_gen():
    for el in range(6):
        idx = randint(0,35 - el)
        my_cards.append(all_cards[idx])
        all_cards.pop(idx)
    print("--- your cards: ---\n", my_cards)

# generate cards for comp
def comp_cards_gen():
    for el in range(6):
        idx = randint(0,29 - el)
        comp_cards.append(all_cards[idx])
        all_cards.pop(idx)

# choosing the trump suit
def trump():
    global trump_card
    idx = randint(1, len(all_cards)-1)
    trump_card = all_cards[idx]
    print("Trump is:", trump_card)
    #pick a trump and move it as a last card to choose
    all_cards.append(all_cards.pop(all_cards.index(trump_card)))

def start_game():
    print("=======================================")
    print("Welcome! It's a card game 'durak'. v.1.0")

def logic():
    global my_cards
    global comp_cards
    global ext_comp_cards
    global ext_my_cards
    global one_round_cards
    global my_cards_idx 
    global comp_cards_idx

    #math for my_cards -- converting cards to int. Lets assume that trump cards have value: 100 + card
    for card in my_cards:
        if card[1] == trump_card[1]:
            my_cards_idx.append(cards.get(card[0])+100)
        else:
            my_cards_idx.append(cards.get(card[0]))
    #print(my_cards_idx)

    #math for comp_cards -- converting cards to int. Lets assume that trump cards have value: 100 + card
    for card in comp_cards:
        if card[1] == trump_card[1]:
            comp_cards_idx.append(cards.get(card[0])+100)
        else:
            comp_cards_idx.append(cards.get(card[0]))
    #print(comp_cards_idx)

    # extend cards with values // for comp artificial intelligence
    ext_comp_cards = list(zip(comp_cards,comp_cards_idx))
    ext_my_cards = list(zip(my_cards,my_cards_idx))
    #sorted cards
    ext_my_cards = sorted(ext_my_cards, key = lambda x: x[1])
    ext_comp_cards = sorted(ext_comp_cards, key = lambda x: x[1])

    #who goes first?
    if sorted(my_cards_idx)[::-1][0] > 100:
        my_min_tramp = min(filter(lambda x: x > 100, my_cards_idx))
    else:
        my_min_tramp = 0

    if sorted(comp_cards_idx)[::-1][0] > 100:
        comp_min_tramp = min(filter(lambda x: x > 100, comp_cards_idx))
    else:
        comp_min_tramp = 0
    
    if my_min_tramp < comp_min_tramp:
        print("--- You go first because you have less trump card ---")
        #user_step_attack()
    else:
        print("--- I go first. I have less trump card ---")
        print("computer cards:", ext_comp_cards)
        #comp_step_attack()
        print("--- sorry...implementation of this is ongoing... ---")
        exit()

def comp_step_attack():
    one_round_cards.append(ext_comp_cards[0])
    ext_comp_cards.pop(0)

def comp_step_defence():
    #print("comp:", ext_comp_cards)
    comp_options_to_choose = []
    for card in ext_comp_cards:
        if card[0][1] == one_round_cards[-1][0][1]:
            if card[1] > one_round_cards[-1][1]:
                comp_options_to_choose.append(card)
        elif card[1] > 100:
            comp_options_to_choose.append(card)
        else:
            continue
    if comp_options_to_choose:
        one_round_cards.append(comp_options_to_choose[0])
        ext_comp_cards.pop()
        print("--- I beat it with card:", comp_options_to_choose[0])
    else:
        print("--- I take this card ---")
        ext_comp_cards.append(one_round_cards[:])
        print("--- You won!")
        exit()

def user_step_attack():
    choise = ""
    print("--- Choose one card. Press:[1-6] ---\n", ext_my_cards)
    choise = input()
    if choise == '1':
        one_round_cards.append(ext_my_cards[0])
        ext_my_cards.pop(0)
        my_cards_idx.pop(0)
    elif choise == '2':
        one_round_cards.append(ext_my_cards[1])
        ext_my_cards.pop(1)
        my_cards_idx.pop(1)
    elif choise == '3':
        one_round_cards.append(ext_my_cards[2])
        ext_my_cards.pop(2)
        my_cards_idx.pop(2)
    elif choise == '4':
        one_round_cards.append(ext_my_cards[3])
        ext_my_cards.pop(3)
        my_cards_idx.pop(3)
    elif choise == '5':
        one_round_cards.append(ext_my_cards[4])
        ext_my_cards.pop(4)
        my_cards_idx.pop(4)
    elif choise == '6':
        one_round_cards.append(ext_my_cards[5])
        ext_my_cards.pop(5)
        my_cards_idx.pop(5)
    else:
        print("choose num between 1 - 6")

def add_more():
    print("--- cards on a table: %s" % one_round_cards)
    res = ''
    print("--- your cards: %s" % ext_my_cards)
    print("--- do u have any card? Press 'y'. End a round. Press 'e' ---")
    res = input()
    if res == 'y':
        user_step_attack()
        comp_step_defence()
        add_more()
    elif res == 'e':
        print("--- next round ---")
        one_round_cards[:] = []
    else:
        print("--- wrong input ---")
        add_more()

def take_card():
    n_card = all_cards[0]
    count = 6
    global ext_my_cards
    global my_cards_idx
    global my_cards
    if len(ext_my_cards) < 6:
        my_cards.append(n_card)
        if n_card[1] == trump_card[1]:
            my_cards_idx.append(cards.get(n_card[0])+100)
        else:
            my_cards_idx.append(cards.get(n_card[0]))

        ext_my_cards.append((my_cards[-1],my_cards_idx[-1]))
        #sorted cards
        ext_my_cards = sorted(ext_my_cards, key = lambda x: x[1])
        all_cards.remove(n_card)
        take_card()
    else:
        print("--- you draw card(s) ---")
        print(ext_my_cards)
        return None


def main_loop():
    for round in range(3):
        user_step_attack()
        comp_step_defence()
        add_more()
        take_card()
        print("---Computer makes next step...Sorry, it's not implemented yet. Make a step again :)")
    print("--- computer cards: %s ---" % ext_comp_cards)
    print("--- You are lucky. You won!!! ---")

######################### MAIN ####################

all_cards = []
my_cards = []
comp_cards = []
ext_comp_cards = []
ext_my_cards = []
comp_cards_idx = []
my_cards_idx = []
one_round_cards = []
trump_card = None
ext_comp_cards = []
next_action = 0

start_game()
all_cards_gen()
user_cards_gen()
comp_cards_gen()
trump()
#print("Koloda:", all_cards)
logic()
main_loop()