import BoardInfo

class BoardTile():
    def __init__(self, typ):
        self.type = typ
        self.occupant = 0 # there is no 0th player, for instantiation purposes

    def __str__(self):
        max_length = BoardInfo.max_tile_length

        return f'{self.type: <{max_length}}'
    
    def update_occupant(self, player_no):
        self.occupant = player_no