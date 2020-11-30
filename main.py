import random, itertools
import assets.Player as player
import assets.board.Board as board

# ----------------------------------APPLICATION STATE TO INITIALISE----------------------------------
game_players = [] #current game players
out_players = [] #list of out players, since it is ordered, also tracks who came in last, 2nd last etc
game_properties = [] #list of all 22 houses to be on the board
game_board = board.init_board() # initalises a persisting BOARD STATE, to be taken reference whenever the board is to be printed
game_chances = board.init_chances() #initialises a randomised chance deck
game_chests = board.init_chests() #initalises a randomised chest deck

# -----------------------------------FUNCTIONS-------------------------------------------
#rewriting imported functions as they always take the same arguments FROM THE APP STATE
def update_display_board(): #updates AND displays board
    board.update_board(game_board, game_players)
    board.display_board(game_board)

def display_board():
    board.display_board(game_board)


#defining reusable functions:
def send_user_to_jail(player_obj): #send player to jail
    print('Uh oh! Time to go to jail!')
    input('Press Enter to continue...') #a way to ask for user acknowledgement before sending that user to jail
    player_obj.position = 10 #jail's position
    player_obj.is_in_jail = True
    update_display_board()
    print(f"Player {player_obj.player_no}'s turn will end now")

def remove_user_from_jail(player_obj): # removes user from jail
    player_obj.is_in_jail = False #note that player's position will still be 10
    player_obj.jail_roll_counter = 0 #resets the counter
    print('You are now out of jail!')

def move_nearest_property(property_ls, current_pos, player_obj): #for 'advance to nearest xxx' chance cards
    ls_index = 0
    max_difference = 0
    for index, pos in enumerate(property_ls):
        pos_difference = abs(current_pos - pos)
        if pos_difference > max_difference:
            max_difference = pos_difference
            ls_index = index
    pos_to_move_to = property_ls[ls_index]
    player_obj.update_position(pos_to_move_to - current_pos)
    update_display_board()

def advance_to_start(player_obj, current_pos):
    start_index = 40
    increment = start_index - current_pos
    player_obj.update_position(increment)
    update_display_board()
    print('You are brought to the start and have received $200.')

def remove_player(player_obj):
    player_obj.is_out = True # sets this attr in the player object to be true
    game_players.remove(player_obj)
    out_players.append(player_obj)

def pay_someone(player_obj, creditor, amount_due):
    player_obj.update_wallet(-amount_due)
    if creditor != 'bank': #if paying to another player
        creditor.update_wallet(amount_due)

def liquidate_property(player_obj, prop):
    prop.update_owner(0) #0 means return to the bank
    player_obj.update_properties('remove', prop) # removes ownership from player obj
    player_obj.update_wallet(prop.selling_price) # player gets money
    print(f'You sold your {prop.name} property for ${prop.selling_price}. You now have ${player_obj.wallet}')

def sell_properties(player_obj):
    affirmations = ['Y', 'N']
    selling = True
    while selling:
        num_properties = len(player_obj.properties)
        properties_list = ''
        for index, prop in enumerate(player_obj.properties):
            properties_list += f'\n{index+1}) {prop.name} {prop.symbol} (${prop.selling_price})'
        print(f'You currently own these properties: {properties_list}')

        if num_properties == 1: #if user only has 1 property
            only_property = player_obj.properties[0]
            user_affirmation = input(f'Would you like to sell this {only_property.name} property? [Y / N] ')
            while user_affirmation not in affirmations:
                print('Please type in something valid from the options given')
                user_affirmation = input(f'Would you like to sell this {only_property.name} property? [Y / N] ')
            if user_affirmation == 'Y': #if user wants to sell
                liquidate_property(player_obj, only_property)
            selling = False

        else: #user has more than 1 property
            prop_index_to_sell = input('Which property would you like to sell (refer to the numbering)? Entering 0 means you do not want to sell any properties. ')
            while not prop_index_to_sell.isdigit() and int(prop_index_to_sell) not in range(1, num_properties):
                print(f'Please input a number between 1 and {num_properties}')
                prop_index_to_sell = input('Which property would you like to sell (refer to the numbering)? Entering 0 means you do not want to sell any properties. ')
            prop_index_to_sell = int(prop_index_to_sell)

            if prop_index_to_sell == 0:
                selling = False
            else: #if user wants to sell properties
                prop_to_sell = player_obj.properties[prop_index_to_sell-1] #because 0 indexed
                liquidate_property(player_obj, prop_to_sell)
                sell_again = input('Would you like to sell another property? [Y / N] ')
                while sell_again not in affirmations:
                    print('Please type in something valid from the options given')
                    sell_again = input('Would you like to sell another property? [Y / N] ')

                if sell_again == 'N':
                    selling = False

def bankruptcy_check(player_obj, creditor, amount_due):
    if player_obj == creditor:
        print("You landed on your own property! You of course don't pay rent.")
    
    elif player_obj.wallet < amount_due: #if player has lesser money than what is owed
        if player_obj.properties: #if player owns assets
            #calculates total liquidation value of player's assets
            total_liquidity = 0
            for prop in player_obj.properties:
                total_liquidity += prop.selling_price
            
            if total_liquidity + player_obj.wallet < amount_due: #when ALL player's assets' liquidation value  AND his current money CANNOT meet amount owed
                print(f'Although you have assets, their total liquidation value of ${total_liquidity} and your current holdings of ${player_obj.wallet} is lesser than the ${amount_due} which you owe.')
                if creditor != 'bank': 
                    print(f'In order to pay up the debt, all your current assets will be transferred to Player {creditor.player_no}. You are now bankrupt and are out of the game.')
                else:
                    print('In order to pay up the debt, all your current assets will be transferred to the Bank. You are now bankrupt and are out of the game.')
                
                #TRANSFERRING OWNERSHIP OF PROPERTIES (no money involved)
                for prop in player_obj.properties:
                    player_obj.update_properties('remove', prop)
                    if creditor != 'bank': #if creditor is another player
                        prop.update_owner(creditor)
                        creditor.update_properties('add', prop)
                    else:
                        prop.update_owner(0)
                #--------------------------LOSING CONDITION------------------------------
                remove_player(player_obj) #removing this player from the game

            else: #when player can sell assets to pay money owed
                print(f'Oops you owe money but currently do not have enough (you have ${player_obj.wallet}) to pay up your debt (${amount_due})! Your current ownings can be liquidated to clear your debt.')
                # ----------SELLING PROPERTIES-------------
                sell_properties(player_obj)
                #once user decides to stop selling the first round above (do while loop)
                while player_obj.wallet < amount_due: #if still not enough money, force user to sell properties
                    print(f'Sorry you must sell your properties to pay your debt. You currently have ${player_obj.wallet} and you owe ${amount_due}.')
                    sell_properties(player_obj)
                #once user has enough money, pay money to creditor
                pay_someone(player_obj, creditor, amount_due) #creditor could be 'bank
                if creditor != 'bank':
                    print(f'You have paid Player {creditor.player_no} ${amount_due}. You now have ${player_obj.wallet}.')
                else:
                    print(f'You have paid the Bank ${amount_due}. You now have ${player_obj.wallet}.')

        else: # if player does not own any asset
            print(f'Dear Player {player_obj.player_no}, you have run out of money and have no properties to mortgage. You are now bankrupt and are out of the game.')
            #----------------------LOSING CONDITION---------------------------
            remove_player(player_obj)

    else: #user has enough money. pay creditor 
        pay_someone(player_obj, creditor, amount_due) #creditor could be 'bank'
        if creditor != 'bank':
            print(f'You have paid Player {creditor.player_no} ${amount_due}. You now have ${player_obj.wallet}.')
        else:
            print(f'You have paid the Bank ${amount_due}. You now have ${player_obj.wallet}.')

# ----------------------------------------GAME CODE---------------------------------------
# welcome message
print('For the best experience, please maximise your terminal :)')

# asks for number of players
num_players = input('Welcome to Python Monopoly! How many players do we have today? ')
while not num_players.isdigit() or not (int(num_players) >= 2 and int(num_players) <= 4):
    print('Please enter a number between 2 to 4')
    num_players = input('Welcome to Python Monopoly! How many players do we have today? ')
num_players = int(num_players)

# instantiates that number of players and adds to game
for player_no in range(1, num_players+1):
    game_players.append(player.Player(player_no))

# asks that user for their token/initials for board display, and updates the state
taken_user_tokens = [] #stores current user tokens taken, makes sure that tokens are unique
for user in game_players:
    user_token = input(f'Dear Player {user.player_no}, please enter your initials (max 2 characters) which will be displayed on the board. ')
    while not user_token or user_token in taken_user_tokens or len(user_token) > 2: #runs if user_token is an empty string, a falsey value
        print('Please enter something, enter something unique, or enter maximum of 2 characters only.')
        user_token = input(f'Dear Player {user.player_no}, please enter your initials (max 2 characters) which will be displayed on the board. ')
    user.set_token(user_token)
    taken_user_tokens.append(user_token)

# sets all players to the start position and prints inital board
board.set_start_tile(game_board, game_players)
display_board()

# --------------STARTS THE MAIN 'WHILE' LOOP---------------------
for user in itertools.cycle(game_players): # infinitely cycle through the list
    end_turn = False
    if len(out_players) == 3: # there are 3 players who are out, the game ends
        break

    elif user.is_out:
        continue

    else: #user is in the game
        if user.is_in_jail: #if user is in jail, has a different set of actions, ---------------VERIFIED-----------------
            jail_tile = game_board[10] #jail tile obj
            possible_actions = ['show_my_info', 'pay']
            if user.jail_roll_counter < 3:
                possible_actions.append('roll')
            if user.has_jail_card: #if user has a out of jail card, add it as one of the options
                possible_actions.append('use_card')
            possible_actions_str = ' / '.join(possible_actions)

            print(f'Dear Player {user.player_no}, you are sadly in jail :(\n')
            print(f'There are 3 ways to get out of here:\n1) Pay a fine of ${jail_tile.fine}\n2) Roll doubles\n3) Use a Get Out of Jail Free card (if you have)\n')

            while not end_turn:
                if 'roll' in possible_actions: 
                    print('Do note that choosing "roll" will end your turn immediately afterwards.')
                action = input(f'What would you like to do? [{possible_actions_str}] ')
                while action not in possible_actions:
                    print('Please type in something valid from the options given')
                    if 'roll' in possible_actions: 
                        print('Do note that choosing "roll" will end your turn immediately afterwards.')
                    action = input(f'What would you like to do? [{possible_actions_str}] ')

                if action == 'show_my_info':
                    print(user)
                elif action == 'roll':
                    print(f'You can only attempt to roll doubles once a turn. If you fail 3 consecutive turns, you would be forced to either pay the fine or use the Get Out of Jail Free card.')
                    user.jail_roll_counter += 1 # updates counter
                    diceroll1 = random.randint(1, 6)
                    diceroll2 = random.randint(1, 6)
                    if diceroll1 == diceroll2: # a double is rolled
                        print(f'Congratulations! You rolled doubles of {diceroll1}. You are free to go.')
                        remove_user_from_jail(user)
                        update_display_board()
                    else: # if no double is rolled
                        print(f'Oh no! You failed to roll a double. What you rolled was a {diceroll1} and a {diceroll2}.\nYou have attempted to roll doubles for {user.jail_roll_counter} time(s).')   
                        
                    end_turn = True # ends turn after a roll, regardless of outcome
                else:
                    if action == 'pay': #VERIFIED
                        fine = jail_tile.fine
                        bankruptcy_check(user, 'bank', fine)
                    elif action == 'use_card': #VERIFIED
                        user.has_jail_card = False #removes jail card from user
                        print('You used your Get Out of Jail Free card!')
                    
                    # these 2 actions will guarantee the user being removed from jail and ends his turn
                    remove_user_from_jail(user)
                    update_display_board()
                    end_turn = True


        else: #if user is not in jail
            possible_actions = ['roll_dice', 'show_my_info', 'end_turn']
            possible_actions_str = ' / '.join(possible_actions) #str representation of possible actions user can take

            while not end_turn:
                action = input(f'Dear Player {user.player_no}, what would you like to do? [{possible_actions_str}] ')
                while action not in possible_actions:
                    print('Please type in something valid from the options given')
                    action = input(f'Dear Player {user.player_no}, what would you like to do? [{possible_actions_str}] ')

                if action == 'end_turn':
                    display_board() #display the board before ending an empty turn
                    end_turn = True
                
                elif action == 'roll_dice': #rolling dice entails that user moves and handling of what happens when the user lands on a tile is done here
                    diceroll1 = random.randint(1, 6) #simulates a single dice roll
                    diceroll2 = random.randint(1, 6)
                    user_diceroll = diceroll1 + diceroll2
                    user.update_position(user_diceroll) #adds diceroll to previous position of user
                    
                    #------testing each tile's functionality-------
                    #user.update_position(30) #testing go_jail functionality
                    #user.update_position(4) #testing road tax
                    #user.update_position(38) #testing income tax
                    #-----end of testing-------------------------

                    update_display_board()
                    print(f'You rolled a {diceroll1} and a {diceroll2}, totalling to {user_diceroll}')

                    landed_tile = game_board[user.position] #represents the tile object on which the user has landed
                    if hasattr(landed_tile, 'owner'): #checks if the tile might have an owner
                        property_name = landed_tile.name
                        property_type = 'Station' if landed_tile.symbol == 'STATION' else 'Utility' if landed_tile.symbol == 'UTILITY' else 'Street'

                        if landed_tile.owner != 0: #if property is already owned, pay respective rent
                            # finding the current owner (as a Player object)
                            for player in game_players:
                                if player.player_no == landed_tile.owner.player_no:
                                    property_owner = player
                                    break #once owner is found, break the for loop
                            
                            rental_due = landed_tile.rental
                            print(f'This {property_type} property "{property_name}" you landed on is already owned by Player {property_owner.player_no} or {property_owner.token}. You have to pay him/her rent of ${rental_due}!')
                            #------------------CHECK--------------------------
                            bankruptcy_check(user, property_owner, rental_due)
                            # user.update_wallet(-rental_due) #user pays money
                            # property_owner.update_wallet(rental_due) #owner receives money
                            #print(f'You now have ${user.wallet} and Player {property_owner.player_no} has ${property_owner.wallet}') #to omit? what happens if user is removed after the check above?

                        else: #if property is NOT owned, give choice to current user to buy it, (if not set up an auction)
                            purchase_options = ['Y', 'N']
                            property_price = landed_tile.listing_price
                            user_purchase = input(f'This {property_type} property "{property_name}" is currently not owned! Would you like to buy it at its listed price of ${property_price}? [Y / N] ')
                            while user_purchase not in purchase_options:
                                print('Please input a valid option given in the square brackets above')
                                user_purchase = input(f'This {property_type} property "{property_name}" is currently not owned! Would you like to buy it at its listed price of ${property_price}? [Y / N] ')
                            
                            if user_purchase == 'Y': #user wants to buy property
                                if user.wallet >= property_price:
                                    landed_tile.update_owner(user) #assigns owner (player obj) to this property tile
                                    user.update_wallet(-property_price) #deducts money from user for property purchase
                                    user.update_properties('add', landed_tile) #adds this property to user's owned properties list
                                    print(f'You have purchased the property {property_name} for ${property_price}. Now you have ${user.wallet} left')
                                else: #user does not have enough money to buy
                                    print(f'Sorry you do not have enough money to buy this property.')
                                    #to implement asking user if he wants to sell any of his current properties in order to buy this one
                            else:
                                pass #to set up auction

                    else: #filters out the tiles which are unownable, i.e. start, chest, tax, chance, jail, go_jail, parking
                        if landed_tile.symbol == 'CHANCE':
                            print('You landed on CHANCE, draw a Chance card!')
                            current_pos = user.position
                            drawn_chance = game_chances.pop(0) # removes the card at top of deck and returns it (ls.pop method)
                            print(f'You received a "{drawn_chance}" Chance card!')
                            
                            #--------HANDLING DIFFERENT CHANCES---------------
                            if drawn_chance == 'Get Out of Jail Free':
                                user.has_jail_card = True

                            elif drawn_chance == 'Advance to Go': #brings user to start (tile 0) and gives him $200
                                advance_to_start(user, current_pos)

                            elif drawn_chance == 'Go directly to Jail':
                                send_user_to_jail(user)
                                end_turn = True # once user lands into jail, his turn ends

                            elif drawn_chance == 'Go back 3 spaces':
                                user.update_position(-3)
                                update_display_board()
                                print('You were brought back 3 spaces.')

                            elif drawn_chance == 'Advance to nearest Utility':
                                utility_pos = [12, 28]
                                move_nearest_property(utility_pos, current_pos, user)
                                
                            elif drawn_chance == 'Advance to nearest Station':
                                station_pos = [5, 15, 25, 35]
                                move_nearest_property(station_pos, current_pos, user)

                            elif drawn_chance == 'Pay poor tax of $50':
                                bankruptcy_check(user, 'bank', 50)

                            elif drawn_chance == 'Bank pays you $100 as dividends':
                                user.update_wallet(100)
                                print(f'You received $100 and now have ${user.wallet}')

                            game_chances.append(drawn_chance) #after handling the card's actions, move it to the bottom of the deck

                        elif landed_tile.symbol == 'CHEST':
                            print('You landed on COMMUNITY CHEST, draw a Chest card!')
                            drawn_chest = game_chests.pop(0)
                            print(f'You received a "{drawn_chest}" Chest card!')

                            if drawn_chest == 'Get Out of Jail, Free':
                                user.has_jail_card = True

                            elif drawn_chest == 'Advance to Go': #brings user to start (tile 0) and gives him $200
                                advance_to_start(user, current_pos)

                            elif drawn_chest == 'Go directly to Jail':
                                send_user_to_jail(user)
                                end_turn = True # once user lands into jail, his turn ends
                            
                            elif drawn_chest == 'You inherit $100':
                                user.update_wallet(100)
                                print(f'You received $100 and now have ${user.wallet}')
                            
                            elif drawn_chest == 'Income Tax refund of $200':
                                user.update_wallet(200)
                                print(f'You received $200 and now have ${user.wallet}')

                            elif drawn_chest == 'Life Insurance matures, collect $150':
                                user.update_wallet(150)
                                print(f'You received $150 and now have ${user.wallet}')
                            
                            elif drawn_chest == '$200 Hospital Bill':
                                bankruptcy_check(user, 'bank', 200)
                            
                            elif drawn_chest == '$100 school fees':
                                bankruptcy_check(user, 'bank', 100)

                            game_chests.append(drawn_chest) #after handling the card's actions, move it to the bottom of the deck

                        elif landed_tile.symbol == 'TAX': #VERIFIED
                            print("It's time to pay taxes!")
                            if hasattr(landed_tile, 'amount'): #if the tile already has am 'amount' attribute, it is road tax
                                print('You have to pay road tax.')
                                road_tax = 100
                                bankruptcy_check(user, 'bank', road_tax)

                            else: #income tax tile
                                amount_to_deduct = landed_tile.determine_income_tax(user)
                                print(f'For income tax, you either pay $200 or 10% of your total net worth, whichever is higher.')
                                bankruptcy_check(user, 'bank', amount_to_deduct)

                        elif landed_tile.symbol == 'JAIL': #VERIFED
                            print("You landed on jail! But don't worry, you're only visiting.")

                        elif landed_tile.symbol == 'GO_JAIL': #VERIFIED
                            send_user_to_jail(user)
                            end_turn = True # once user lands into jail, his turn ends

                        elif landed_tile.symbol == 'PARKING': #VERFIED
                            print('You landed on free parking!...which does nothing, have a good day!')


                    #--------------------------updating possible actions list-----------------------------
                    possible_actions.remove('roll_dice') #user can only roll dice once in his turn
                    possible_actions_str = ' / '.join(possible_actions) #updates the possible actions string

                elif action == 'show_my_info': #TO LOOK INTO IT AGAIN, SEE HOW BETTER TO DISPLAY USER INFO
                    print(user)


#---------------------------------------------------CONCLUDING THE GAME----------------------------------------------------------
print('------------------------------------------GAME REPORT-------------------------------------------------')
print('The game has ended!')
winner_obj = game_players[0] #the last player standing
print(f'Player {winner_obj.player_no}/{winner_obj.token} has won with ${winner_obj.wallet}!')
pos_counter = 2
for player in out_players[::-1]:
    print(f'{pos_counter}) Player {player.player_no}/{player.token}')
    pos_counter += 1