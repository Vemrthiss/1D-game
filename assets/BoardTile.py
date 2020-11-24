class BoardTile():
    def __init__(self, typ):
        self.type = typ
        self.occupant = 0 # there is no 0th player, for instantiation purposes

    def __str__(self): #for testing
        return f'This is a tile of type {self.type}'
    
    def update_occupant(self, player_no):
        self.occupant = player_no