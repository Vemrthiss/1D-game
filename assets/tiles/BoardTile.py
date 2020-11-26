from assets.board.BoardInfo import max_tile_length

class BoardTile():
    def __init__(self, name):
        self.occupant = 0 # there is no 0th player, for instantiation purposes
        self.max_tile_length = max_tile_length
        self.name = name

    def __str__(self):
        #self.symbol to be declared in child classes
        return f'{self.symbol: <{self.max_tile_length}}'
    
    def update_occupant(self, player_no):
        self.occupant = player_no