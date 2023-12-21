import random, joshfuncs

#    Deck Structure: 
#                  Colours: Red Yellow Blue Green Wild
#                  Colours: 0-9, reverse, skip, draw 2
#                  wild: draw 4 and change colour
#           0    1    1    2    2    3    3    4    4    5    5    6    6    7    7    8    8    9    9    r    r    s    s    d2   d2
UnoDeck = [[True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True], # Red 
           [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True], # Yellow
           [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True], # Blue
           [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True], # Green
           [True,True,True,True,True,True,True,True]]   
BlankUnoDeck = [[True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True], # Red 
           [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True], # Yellow
           [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True], # Blue
           [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True], # Green
           [True,True,True,True,True,True,True,True]]   

DiscardUnoDeck = [[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False], # Red 
           [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False], # Yellow
           [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False], # Blue
           [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False], # Green
           [False,False,False,False,False,False,False,False]]
BlankDiscardUnodeck = [[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False], # Red 
           [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False], # Yellow
           [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False], # Blue
           [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False], # Green
           [False,False,False,False,False,False,False,False]]

UnoDeckConvertionTable = [["r0","r11","r12","r21","r22","r31","r32","r41","r42","r51","r52","r61","r62","r71","r72","r81","r82","r91","r92","rr1","rr2","rs1","rs2","rd21","rd22"],
                         ["y0","y11","y12","y21","y22","y31","y32","y41","y42","y51","y52","y61","y62","y71","y72","y81","y82","y91","y92","yr1","yr2","ys1","ys2","yd21","yd22"],
                         ["b0","b11","b12","b21","b22","b31","b32","b41","b42","b51","b52","b61","b62","b71","b72","b81","b82","b91","b92","br1","br2","bs1","bs2","bd21","bd22"],
                         ["g0","g11","g12","g21","g22","g31","g32","g41","g42","g51","g52","g61","g62","g71","g72","g81","g82","g91","g92","gr1","gr2","gs1","gs2","gd21","gd22"],
                         ["wd41","wd42","wd43","wd44","w1","w2","w3","w4"]]


def CountDeck(deck):
    red = 0
    yellow = 0
    blue = 0
    green = 0
    wild = 0
    for card in deck[0]: # Red
        if card == True:
            red += 1
    for card in deck[1]: # Yellow
        if card == True:
            yellow += 1
    for card in deck[2]: # Blue
        if card == True:
            blue += 1
    for card in deck[3]: # Green
        if card == True:
            green += 1
    for card in deck[4]: # Wild
        if card == True:
            wild += 1
    
    total = red + yellow + blue + green + wild
    return([total, red, yellow, blue, green, wild])

def RemoveCard(colour,card,deck):
    deck[colour][card] = False
    return deck
            
def OrganiseCards(player_cards):
    red    = []
    yellow = []
    blue   = []
    green  = []
    wild   = []
    
    for card in player_cards:
        if card[0] == "r":
            red.append(card)
        elif card[0] == "y":
            yellow.append(card)
        elif card[0] == "b":
            blue.append(card)
        elif card[0] == "g":
            green.append(card)
        else:
            wild.append(card)
        
    red.sort()
    yellow.sort()
    blue.sort()
    green.sort()
    wild.sort()
    player_cards = []
    for card in red:
        player_cards.append(card)
    for card in yellow:
        player_cards.append(card)
    for card in blue:
        player_cards.append(card)
    for card in green:
        player_cards.append(card)
    for card in wild:
        player_cards.append(card)

    return player_cards
  
def AddCards(player_cards, cards_added, deck,table):
    i = 0
    deck_amount = CountDeck(deck)
    def choose_colour(deck_amount):
        # Choose Colour
        colour_random = random.randint(1, deck_amount[0])
        if colour_random - deck_amount[1] <= 0:
            colour = 0 # Red
        elif colour_random - deck_amount[1] - deck_amount[2] <= 0:
            colour = 1 # Yellow
        elif colour_random - deck_amount[1] - deck_amount[2] - deck_amount[3] <= 0:
            colour = 2 # Blue
        elif colour_random - deck_amount[1] - deck_amount[2] - deck_amount[3] - deck_amount[4] <= 0:
            colour = 3 # Green
        else:
            colour = 4 # Wild
            
        return colour
    def choose_card(colour,deck):
        deck_amount = CountDeck(deck)
        i = 0
        card_pos = 0
        if colour == 0:
            card_num = random.randint(0,deck_amount[1] - 1)
        elif colour == 1:
            card_num = random.randint(0,deck_amount[2] - 1)
        elif colour == 2:
            card_num = random.randint(0,deck_amount[3] - 1)
        elif colour == 3:
            card_num = random.randint(0,deck_amount[4] - 1)
        else:
            card_num = random.randint(0,deck_amount[5] - 1)

        set = deck[colour]
        valid = False
        while not valid:
            if set[card_num] == True:
                valid = True
            else:
                valid = False
                card_num += 1

        return card_num
   
    while (i in range(0, cards_added)):
        deck_amount = CountDeck(deck)
        colour = choose_colour(deck_amount)
        card = choose_card(colour, deck)
        deck = RemoveCard(colour,card,deck)
        player_cards.append(table[colour][card])
        i += 1
    
    return player_cards, deck

def AddCardReturnCardAdded(player_cards, deck, table):
    i = 0
    deck_amount = CountDeck(deck)
    def choose_colour(deck_amount):
        # Choose Colour
        colour_random = random.randint(1, deck_amount[0])
        if colour_random - deck_amount[1] <= 0:
            colour = 0 # Red
        elif colour_random - deck_amount[1] - deck_amount[2] <= 0:
            colour = 1 # Yellow
        elif colour_random - deck_amount[1] - deck_amount[2] - deck_amount[3] <= 0:
            colour = 2 # Blue
        elif colour_random - deck_amount[1] - deck_amount[2] - deck_amount[3] - deck_amount[4] <= 0:
            colour = 3 # Green
        else:
            colour = 4 # Wild
            
        return colour
    def choose_card(colour,deck):
        deck_amount = CountDeck(deck)
        i = 0
        card_pos = 0
        if colour == 0:
            card_num = random.randint(0,deck_amount[1] - 1)
        elif colour == 1:
            card_num = random.randint(0,deck_amount[2] - 1)
        elif colour == 2:
            card_num = random.randint(0,deck_amount[3] - 1)
        elif colour == 3:
            card_num = random.randint(0,deck_amount[4] - 1)
        else:
            card_num = random.randint(0,deck_amount[5] - 1)

        set = deck[colour]
        valid = False
        while not valid:
            if set[card_num] == True:
                valid = True
            else:
                valid = False
                card_num += 1

        return card_num
   
    deck_amount = CountDeck(deck)
    colour = choose_colour(deck_amount)
    card = choose_card(colour, deck)
    deck = RemoveCard(colour,card,deck)
    player_cards.append(table[colour][card])

    
    return player_cards, deck, table[colour][card]

def Reshuffle(deck, discard_deck):
    colour      = 0

    for set in discard_deck:
        card_num    = 0
        for card in set:
            if card == True:
                deck[colour][card_num] = True
            card_num += 1
        colour += 1
    discard_deck = BlankDiscardUnodeck
    return deck, discard_deck

def GenerateTopCard(deck, discard_deck, convertion_table):
    deck_amount = CountDeck(deck)
    def choose_colour(deck_amount):
        # Choose Colour
        colour_random = random.randint(1, deck_amount[0])
        if colour_random - deck_amount[1] <= 0:
            colour = 0 # Red
        elif colour_random - deck_amount[1] - deck_amount[2] <= 0:
            colour = 1 # Yellow
        elif colour_random - deck_amount[1] - deck_amount[2] - deck_amount[3] <= 0:
            colour = 2 # Blue
        elif colour_random - deck_amount[1] - deck_amount[2] - deck_amount[3] - deck_amount[4] <= 0:
            colour = 3 # Green
        else:
            colour = 4 # Wild
            
        return colour
    def choose_card(colour,deck):
        deck_amount = CountDeck(deck)
        i = 0
        card_pos = 0
        if colour == 0:
            card_num = random.randint(0,deck_amount[1] - 1)
        elif colour == 1:
            card_num = random.randint(0,deck_amount[2] - 1)
        elif colour == 2:
            card_num = random.randint(0,deck_amount[3] - 1)
        elif colour == 3:
            card_num = random.randint(0,deck_amount[4] - 1)
        else:
            card_num = random.randint(0,deck_amount[5] - 1)

        set = deck[colour]
        valid = False
        while not valid:
            if set[card_num] == True:
                valid = True
            else:
                valid = False
                card_num += 1

        return card_num

    deck_amount = CountDeck(deck)
    colour = choose_colour(deck_amount)
    card = choose_card(colour, deck)
    deck = RemoveCard(colour,card,deck)
    top_card = (convertion_table[colour][card])
    discard_deck[colour][card] = True
    return top_card, deck, discard_deck

def InitializePlayersCards(Players, CardsPerPlayer, deck, table):
    player1, player2, player3, player4 = [], [], [] ,[]
    
    if Players == 1:
        player1, deck = AddCards(player1, CardsPerPlayer, deck, table)
        player1 = OrganiseCards(player1)
    elif Players == 2:
        player1, deck = AddCards(player1, CardsPerPlayer, deck, table)
        player1 = OrganiseCards(player1)
        
        player2, deck = AddCards(player2, CardsPerPlayer, deck, table)
        player2 = OrganiseCards(player2)
    elif Players == 3:
        player1, deck = AddCards(player1, CardsPerPlayer, deck, table)
        player1 = OrganiseCards(player1)
        
        player2, deck = AddCards(player2, CardsPerPlayer, deck, table)
        player2 = OrganiseCards(player2)
        
        player3, deck = AddCards(player3, CardsPerPlayer, deck, table)
        player3 = OrganiseCards(player3)
    elif Players == 4:
        player1, deck = AddCards(player1, CardsPerPlayer, deck, table)
        player1 = OrganiseCards(player1)
        
        player2, deck = AddCards(player2, CardsPerPlayer, deck, table)
        player2 = OrganiseCards(player2)
        
        player3, deck = AddCards(player3, CardsPerPlayer, deck, table)
        player3 = OrganiseCards(player3)
        
        player4, deck = AddCards(player4, CardsPerPlayer, deck, table)
        player4 = OrganiseCards(player4)
        
        
    return player1, player2, player3, player4, deck

def PlaceCard(PlayerCards, NextPlayerCards, Deck, DiscardDeck, TopCard, ConvertionTable, direction):
    again = False
    print("--- Your Cards ---")
    print(PlayerCards)
    print("--- These Start from 1 and count up --- \n \n --- The Top Card Is:", TopCard, "---\n")
    cardToPlace = ''
    validcardtoplace = False
    placingCard = False
    validanswer = False
    
    while not validanswer:
        answer = input("Are you placing a card or picking up? (place, pick): ")
        if answer.lower() == "place":
            validanswer = True
            placingCard = True
        elif answer.lower() == "pick":
            validanswer = True
            placingCard = False
    
    if placingCard == True:        
        while not validcardtoplace:
            card = joshfuncs.intinputrange("Please enter the number card that you want to place, or p to pickup a card: ", 1, len(PlayerCards)) - 1
            cardToPlace = PlayerCards[card]
            if (cardToPlace[0] == 'w') or (cardToPlace[0] == TopCard[0]) or (cardToPlace[1] == TopCard[1]):
                validcardtoplace = True
                placingCard = True
            
            else:
                validcardtoplace = False
                print("Please Choose a card with the same top card colour. The current top card colour is", TopCard[0])
            
        colour, cardnum = NameToTable(cardToPlace, ConvertionTable)
        TopCard = cardToPlace
        DiscardDeck[colour][cardnum] = True
        PlayerCards.remove(cardToPlace)
        
        if cardToPlace[0] == 'w':
            if cardToPlace[1:2] == 'd4':
                NextPlayerCards, Deck = AddCards(NextPlayerCards, 4, Deck, ConvertionTable)
                NextPlayerCards = OrganiseCards(NextPlayerCards)                
            
            newcolour = input("What color would you like the next card to be? r, y, g or b: ")
            if newcolour.lower() == 'r':
                TopCard = 'r'
            elif newcolour.lower() == 'y':
                TopCard = 'y'
            elif newcolour.lower() == 'g':
                TopCard = 'g'
            else:
                TopCard = 'b'
            again = True
        if cardToPlace[1] == 'r':
            if direction == "Positive":
                direction = "Negative"
            else:
                direction = "Positive"
        if cardToPlace[1:2] == 'd2':
            NextPlayerCards, Deck = AddCards(NextPlayerCards, 2, Deck, ConvertionTable)
            NextPlayerCards = OrganiseCards(NextPlayerCards)
        
    else:
        PlayerCards, Deck, newcard = PickUpCard(PlayerCards, Deck, ConvertionTable)
        print("Your New Card Was:", newcard)

    PlayerCards = OrganiseCards(PlayerCards)
    return PlayerCards, NextPlayerCards, DiscardDeck, TopCard, again, direction
    
def NameToTable(card, table):
    cardnum = 0
    colour = 0
    if card[0] == 'r':
        colour = 0
    elif card[0] == "y":
        colour = 1
    elif card[0] == 'b':
        colour = 2
    elif card[0] == 'g':
        colour = 3
    else:
        colour = 4


    found = False
    i = 0
    while not found:
        if table[colour][i] == card:
            found = True
        else:
            i += 1
    cardnum = i
        
    return colour, cardnum

def PickUpCard(PlayerCards, deck, ConvertionTable):
    PlayerCards, deck, card = AddCardReturnCardAdded(PlayerCards, deck, ConvertionTable)
    
    return PlayerCards, deck, card
    


