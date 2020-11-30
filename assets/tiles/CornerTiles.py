from assets.tiles.BoardTile import BoardTile

class Start(BoardTile):
    def __init__(self):
        name = 'GO'
        BoardTile.__init__(self, name)
        self.symbol = 'START'

class Parking(BoardTile):
    def __init__(self):
        name = 'Free Parking'
        BoardTile.__init__(self, name)
        self.symbol = 'PARKING'

class Jail(BoardTile):
    def __init__(self):
        name = 'In Jail/Just Visiting'
        BoardTile.__init__(self, name)
        self.symbol = 'JAIL'
        self.fine = 100

    def __str__(self): #handles string representation if an occupant is an inmate
        user_tokens = [occupant.token for occupant in self.occupants]
        for index, occupant in enumerate(self.occupants):
            if occupant.is_in_jail: #if occupant is in jail
                user_tokens[index] += ' [in jail]'
        user_tokens_str = f"({', '.join(user_tokens)})"
        str_repr = f'{self.symbol} {user_tokens_str}' if len(user_tokens) != 0 else self.symbol
    
        return f'{str_repr: <{self.max_tile_length}}'

class GoJail(BoardTile):
    def __init__(self):
        name ='Go To Jail'
        BoardTile.__init__(self, name)
        self.symbol = 'GO_JAIL'