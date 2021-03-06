def get_prop_repr(prop):
    return f'{prop.name} {prop.symbol}'

class Player():
    def __init__(self, player_no):
        self.player_no = player_no
        self.token = ''
        self.wallet = 2500 # current amount of player
        self.properties = [] #empty list of property objects
        self.position = 0 # a single number representing current position on board (board is just a 1D list connected at its ends)
        self.is_in_jail = False
        self.has_jail_card = False # denotes if user has get out of jail card
        self.jail_roll_counter = 0 #keeps track of how many times the user has tried to roll doubles to get out of jail
        self.is_out = False # turns to true when this player is out of the game

    def __str__(self):
        all_props = []
        for prop in self.properties:
            all_props.append(get_prop_repr(prop))
        all_props_str = ', '.join(all_props)

        return f'----------------\nPlayer {self.player_no}/{self.token}\nWallet: ${self.wallet}\nOwned Properties: {all_props_str}\nHas Get Out of Jail Free Card: {self.has_jail_card}\nIs in Jail: {self.is_in_jail}\n--------------'

    def set_token(self, token):
        self.token = token

    def update_position(self, increment):
        new_position = self.position + increment
        num_tiles = 40
        if new_position < num_tiles:
            self.position = new_position
        elif new_position < 0: #negative indexing, accounting for negative increment for the 'go back 3 spaces' chance tile
            self.position = num_tiles + increment # increment is negative here (i.e. index -1 becomes 39, -2 becomes 38 etc.)
        else: #if new position now is more than length of the board, i.e. passes through start tile
            self.position = new_position - num_tiles # makes sure the position does not exceed list length, else will cause indexing issues
            self.update_wallet(200) #gives this player $200 since he crossed the start tile
            print(f'For crossing the Start tile, you received $200. You now have ${self.wallet}.')
    
    def update_wallet(self, amount):
        self.wallet += amount #if amount is negative, will minus

    def update_properties(self, action, prop): #adds/removes properties for this player
        if action == 'add':
            self.properties.append(prop)
        elif action == 'remove':
            self.properties.remove(prop)
    
    def clear_properties(self): #clears ALL properties, used for transfering ownership when bankrupt
        self.properties = []