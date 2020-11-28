class Player():
    def __init__(self, player_no):
        self.player_no = player_no
        self.token = ''
        self.wallet = 2000 # current amount of player
        self.properties = [] #empty list of property objects
        self.position = 0 # a single number representing current position on board (board is just a 1D list connected at its ends)
        self.is_in_jail = False

    def __str__(self):
        return f'This is {self.token} or Player {self.player_no} with ${self.wallet}, {self.properties} houses, and is at position {self.position}'

    def set_token(self, token):
        self.token = token

    def update_position(self, new_pos):
        self.position = new_pos
    
    def update_wallet(self, amount):
        self.wallet += amount #if amount is negative, will minus

    def filter_properties(prop, prop_name):
        return prop['name'] == prop_name 
    
    def update_properties(self, action, prop, name_to_remove):
        if action == 'add':
            self.properties.append(prop)
        else:
            filtered_iterable = filter(lambda prop: filter_properties(prop, name_to_remove), self.properties)
            self.properties = list(filtered_iterable)