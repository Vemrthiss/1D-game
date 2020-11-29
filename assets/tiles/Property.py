from assets.tiles.BoardTile import BoardTile

class Property(BoardTile):
    def __init__(self, name, listing_price):
        BoardTile.__init__(self, name)
        self.listing_price = listing_price
        self.owner = 0
        #self.rental and self.symbol to be set in child classes

    def __str__(self):
        #self.symbol to be declared in child classes
        #return f'{self.name: <{self.max_tile_length}}\n{self.symbol: <{self.max_tile_length}}'
        user_tokens = [occupant.token for occupant in self.occupants]
        user_tokens_str = f"({', '.join(user_tokens)})"
        owner_token = f' [{self.owner.token}] ' if self.owner != 0 else ' '

        str_repr = f'{self.symbol}{owner_token}{user_tokens_str}' if len(user_tokens) != 0 else f'{self.symbol}{owner_token}'
    
        return f'{str_repr: <{self.max_tile_length}}'
    
    def update_owner(self, player_obj):
        self.owner = player_obj