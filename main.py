import deckmanager, joshfuncs

# VARIABLES
player1_cards           = []
player2_cards           = []
player3_cards           = []
player4_cards           = []
deck                    = deckmanager.UnoDeck
discard_deck            = deckmanager.DiscardUnoDeck
card_conversion_table   = deckmanager.UnoDeckConvertionTable
top_card                = ''
starting_cards          = 10
ValidTopCard            = False
again                   = False
turn                    = 1
gameloop                = True
direction               = "Positive"


print("--- Welcome To Teribble Uno ---\n")

# Generate Starting Cards
players = 4
player1_cards, player2_cards, player3_cards, player4_cards, deck = deckmanager.InitializePlayersCards(players, starting_cards, deck, card_conversion_table)


# Generate Valid Top Card
while not ValidTopCard:
    top_card, deck, discard_deck = deckmanager.GenerateTopCard(deck,discard_deck,card_conversion_table)
    if (top_card[0] == "d") or (top_card[0] == "w"):
        ValidTopCard = False
    else:
        ValidTopCard = True

# Main Game Loop
while gameloop == True:
    

    while turn == 1:
        print("Hello Player 1 Its Your Turn: ")  
        player1_cards = deckmanager.OrganiseCards(player1_cards)
        if direction == "Positive":  
            player1_cards, player2_cards, discard_deck, top_card, again, direction = deckmanager.PlaceCard(player1_cards, player2_cards, deck, discard_deck, top_card, card_conversion_table, direction)
        else:
            player1_cards, player4_cards, discard_deck, top_card, again, direction = deckmanager.PlaceCard(player1_cards, player4_cards, deck, discard_deck, top_card, card_conversion_table, direction)
            
        if again == True:
            turn = 1
            again = False            
        else:
            if direction == "Positive":
                if (turn + 1) > players:
                    turn = 1
                else:
                    turn += 1
            else:
                if (turn - 1) < players:
                    turn = 3
                else:
                    turn -= 1

    if (deckmanager.CountDeck(deck)[0] == 0):
        print("Reshuffling Deck")
        deck, discard_deck = deckmanager.Reshuffle(deck, discard_deck)

    while turn == 2:
        print("Hello Player 2 Its Your Turn: ")     
        player2_cards = deckmanager.OrganiseCards(player2_cards)  
        
        if direction == "Positive":  
            player2_cards, player3_cards, discard_deck, top_card, again, direction = deckmanager.PlaceCard(player2_cards, player3_cards, deck, discard_deck, top_card, card_conversion_table, direction)
        else:
            player2_cards, player1_cards, discard_deck, top_card, again, direction = deckmanager.PlaceCard(player2_cards, player1_cards, deck, discard_deck, top_card, card_conversion_table, direction)
        
        
        if again == True:
            turn = 1
            again = False            
        else:
            if direction == "Positive":
                if (turn + 1) > players:
                    turn = 1
                else:
                    turn += 1
            else:
                if (turn - 1) < players:
                    turn = 3
                else:
                    turn -= 1

    if (deckmanager.CountDeck(deck)[0] == 0):
        print("Reshuffling Deck")
        deck, discard_deck = deckmanager.Reshuffle(deck, discard_deck)
  
    while turn == 3:
        print("Hello Player 3 Its Your Turn: ")
        player3_cards = deckmanager.OrganiseCards(player3_cards)  
        
        if direction == "Positive":  
            player3_cards, player4_cards, discard_deck, top_card, again, direction = deckmanager.PlaceCard(player3_cards, player4_cards, deck, discard_deck, top_card, card_conversion_table, direction)
        else:
            player3_cards, player2_cards, discard_deck, top_card, again, direction = deckmanager.PlaceCard(player3_cards, player2_cards, deck, discard_deck, top_card, card_conversion_table, direction)
        
        
        if again == True:
            turn = 1
            again = False            
        else:
            if direction == "Positive":
                if (turn + 1) > players:
                    turn = 1
                else:
                    turn += 1
            else:
                if (turn - 1) < players:
                    turn = 3
                else:
                    turn -= 1
 
    if (deckmanager.CountDeck(deck)[0] == 0):
        print("Reshuffling Deck")
        deck, discard_deck = deckmanager.Reshuffle(deck, discard_deck)
   
    while turn == 4:
        print("Hello Player 4 Its Your Turn: ")  
        player4_cards = deckmanager.OrganiseCards(player4_cards)          
        
        if direction == "Positive":  
            player4_cards, player1_cards, discard_deck, top_card, again, direction = deckmanager.PlaceCard(player4_cards, player1_cards, deck, discard_deck, top_card, card_conversion_table, direction)
        else:
            player4_cards, player3_cards, discard_deck, top_card, again, direction = deckmanager.PlaceCard(player4_cards, player3_cards, deck, discard_deck, top_card, card_conversion_table, direction)
        
        
        if again == True:
            turn = 1
            again = False            
        else:
            if direction == "Positive":
                if (turn + 1) > players:
                    turn = 1
                else:
                    turn += 1
            else:
                if (turn - 1) < players:
                    turn = 3
                else:
                    turn -= 1      

    if (deckmanager.CountDeck(deck)[0] == 0):
        print("Reshuffling Deck")
        deck, discard_deck = deckmanager.Reshuffle(deck, discard_deck)

