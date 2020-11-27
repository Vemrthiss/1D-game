from assets.board.BoardInfo import max_tile_length

class BoardTile():
    def __init__(self, name):
        self.occupants = [] # an empty list of player OBJECTS, for instantiation purposes, to hold the PLAYER OBJECT by reference
        self.max_tile_length = max_tile_length
        self.name = name

    def __str__(self):
        #self.symbol to be declared in child classes
        #return f'{self.name: <{self.max_tile_length}}\n{self.symbol: <{self.max_tile_length}}'
        user_tokens = [occupant.token for occupant in self.occupants]
        user_token_str = f"({', '.join(user_tokens)})"
        str_repr = f'{self.symbol} {user_token_str}' if len(user_tokens) != 0 else self.symbol
    
        return f'{str_repr: <{self.max_tile_length}}'
    
    def update_occupants(self, player_obj, action):
        if action == 'entering':
            self.occupants.append(player_obj)
        elif action == 'leaving':
            self.occupants.remove(player_obj)