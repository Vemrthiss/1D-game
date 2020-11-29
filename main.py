import random, itertools
import assets.Player as player
import assets.board.Board as board

# ----------------------------------APPLICATION STATE TO INITIALISE----------------------------------
game_players = []
game_properties = [] #list of all 22 houses to be on the board
game_board = board.init_board() # initalises a persisting BOARD STATE, to be taken reference whenever the board is to be printed
#game_is_running = True #controls the main game loop

#rewriting imported functions as they always take the same arguments FROM THE APP STATE
def update_display_board(): #updates AND displays board
    board.update_board(game_board, game_players)
    board.display_board(game_board)

def display_board():
    board.display_board(game_board)


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
    user_token = input(f'Dear Player {user.player_no}, please enter your initials which will be displayed on the board. ')
    while not user_token or user_token in taken_user_tokens: #runs if user_token is an empty string, a falsey value
        print('Please enter something, or enter something unique')
        user_token = input(f'Dear Player {user.player_no}, please enter your initials which will be displayed on the board. ')
    user.set_token(user_token)
    taken_user_tokens.append(user_token)

# sets all players to the start position and prints inital board
board.set_start_tile(game_board, game_players)
display_board()

#---testing if user in jail functionality----
# game_players[0].is_in_jail = True
# game_players[0].has_jail_card = True
# game_players[0].position = 10
# update_display_board()

# --------------STARTS THE MAIN 'WHILE' LOOP---------------------
for user in itertools.cycle(game_players): # infinitely cycle through the list
    end_turn = False
    
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
                    jail_tile.remove_user_from_jail(user)
                    update_display_board()
                else: # if no double is rolled
                    print(f'Oh no! You failed to roll a double. What you rolled was a {diceroll1} and a {diceroll2}.\nYou have attempted to roll doubles for {user.jail_roll_counter} time(s).')   
                    
                end_turn = True # ends turn after a roll, regardless of outcome
            else:
                if action == 'pay': #VERIFIED
                    user.update_wallet(-jail_tile.fine)
                    print(f'${jail_tile.fine} has been deducted from your wallet and now you have ${user.wallet} left.')
                elif action == 'use_card': #VERIFIED
                    user.has_jail_card = False #removes jail card from user
                    print('You used your Get Out of Jail Free card!')
                
                # these 2 actions will guarantee the user being removed from jail and ends his turn
                jail_tile.remove_user_from_jail(user)
                update_display_board()
                end_turn = True


    else: #if user is not in jail
        possible_actions = ['roll_dice', 'show_my_info', 'end_turn']
        possible_actions_str = ' / '.join(possible_actions) #str representation of possible actions user can take

        while not end_turn and not user.is_out: #user.is_out checks if this user is still in the game
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
                print(f'You rolled a {diceroll1} and a {diceroll2}, totalling to {user_diceroll}')
                
                user.update_position(user_diceroll) #adds diceroll to previous position of user
                
                #------testing each tile's functionality-------
                #user.update_position(30) #testing go_jail functionality
                #user.update_position(4) #testing road tax
                #user.update_position(38) #testing income tax
                #-----end of testing-------------------------

                update_display_board()

                landed_tile = game_board[user.position] #represents the tile object on which the user has landed
                if hasattr(landed_tile, 'owner'): #checks if the tile might have an owner
                    if landed_tile.owner != 0: #if property is already owned, pay respective rent
                        # finding the current owner (as a Player object)
                        for player in game_players:
                            if player.player_no == landed_tile.owner.player_no:
                                property_owner = player
                                break #once owner is found, break the for loop
                        
                        rental_due = landed_tile.rental
                        print(f'The property you landed on is already owned by Player {property_owner.player_no} or {property_owner.token}. You have to pay him/her rent of ${rental_due}!')
                        user.update_wallet(-rental_due) #user pays money
                        property_owner.update_wallet(rental_due) #owner receives money
                        print(f'You now have ${user.wallet} and Player {property_owner.player_no} has ${property_owner.wallet}')

                    else: #if property is NOT owned, give choice to current user to buy it, (if not set up an auction)
                        purchase_options = ['Y', 'N']
                        property_name = landed_tile.name
                        property_price = landed_tile.listing_price
                        property_type = 'Station' if landed_tile.symbol == 'STATION' else 'Utility' if landed_tile.symbol == 'UTILITY' else 'Street'

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
                        print('You landed on chance!')

                    elif landed_tile.symbol == 'CHEST':
                        print('You landed on chest!')

                    elif landed_tile.symbol == 'TAX': #VERIFIED
                        print("It's time to pay taxes!")
                        if hasattr(landed_tile, 'amount'): #if the tile already has am 'amount' attribute, it is road tax
                            user.update_wallet(-100)
                            print(f'$100 has been deducted from your wallet for road tax. You are now left with ${user.wallet}')
                        else: #income tax tile
                            amount_to_deduct = landed_tile.determine_income_tax(user)
                            user.update_wallet(-amount_to_deduct)
                            print(f'For income tax, you either pay $200 or 10% of your total net worth, whichever is higher. You have paid ${amount_to_deduct} and are now left with ${user.wallet}')

                    elif landed_tile.symbol == 'JAIL': #VERIFED
                        print("You landed on jail! But don't worry, you're only visiting.")

                    elif landed_tile.symbol == 'GO_JAIL': #VERIFIED
                        print('Uh oh! Time to go to jail!')
                        input('Press Enter to continue...') #a way to ask for user acknowledgement before sending that user to jail
                        landed_tile.send_user_to_jail(user) #sends user to jail, method from CornerTile.GoJail class
                        update_display_board()
                        print(f"Player {user.player_no}'s turn will end now")
                        end_turn = True # once user lands into jail, his turn ends

                    elif landed_tile.symbol == 'PARKING': #VERFIED
                        print('You landed on free parking!...which does nothing, have a good day!')


                #--------------------------updating possible actions list-----------------------------
                possible_actions.remove('roll_dice') #user can only roll dice once in his turn
                possible_actions_str = ' / '.join(possible_actions) #updates the possible actions string

            elif action == 'show_my_info': #TO LOOK INTO IT AGAIN, SEE HOW BETTER TO DISPLAY USER INFO
                print(user)

            else: #for testing only until other actions have been coded up
                continue


# ------------------------------------------------TESTING---------------------------------------------------
#for testing: assigning player object(s) a position through hard coding
# test_user = game_players[0]
# test_user.update_position(2) #gives the player object a new position at pos 2
# print(game_players[0]) #verifies that the above action updates the app state of game players
# update_board()
# display_board()
# print(game_board[2].occupants)
# test_user2 = game_players[1]
# test_user2.update_position(4)
# print(game_players[1])
# update_board()
# display_board()
# print(game_board[4].occupants)
# test_user.update_position(4)
# print(game_players[0])
# update_board()
# display_board()
# print(game_board[4].occupants)

# for user in game_players:
#     print(user)