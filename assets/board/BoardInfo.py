num_tiles = 40

board_layout = { #defines how many of each tile type there should be in the board, TO BE REMOVED????
    'start': 1, #start/parking are corner pairs
    'parking': 1,
    'jail': 1, #jail tile is also 'just visiting' if he/she is not in jail
    'go_jail': 1, #jail/go_jail are corner pairs
    'chance': 3,
    'community_chest': 3,
    'small_tax': 1,
    'large_tax': 1,
    'train_station': 4, #one on each side
    'utility_bills': 2 #e.g. water, electricity
}

def get_max_tile_length():
    max_length = 0
    for key in board_layout: #references 'board_layout' variable of this file
        if len(key) > max_length:
            max_length = len(key)
    return max_length

max_tile_length = get_max_tile_length()