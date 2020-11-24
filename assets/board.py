import BoardTile

num_tiles = 40 #total number of tiles
board_layout = { #defines how many of each tile type there should be in the board
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

board = ['x' for num in range(num_tiles)]
corner_difference = int(num_tiles/2)

#setting ALL tile positions
board[0] = BoardTile.BoardTile('start')
board[corner_difference] = BoardTile.BoardTile('parking')
board[10] = BoardTile.BoardTile('jail')
board[10+corner_difference] = BoardTile.BoardTile('go_jail')

#cannot assign multiple variables to the same value at once (else all point to same object)
board[7] = BoardTile.BoardTile('chance')
board[22] = BoardTile.BoardTile('chance')
board[36] = BoardTile.BoardTile('chance')
board[2] = BoardTile.BoardTile('community_chest')
board[17] = BoardTile.BoardTile('community_chest')
board[33] = BoardTile.BoardTile('community_chest')

board[4] = BoardTile.BoardTile('small_tax')
board[38] = BoardTile.BoardTile('large_tax')

board[5] = BoardTile.BoardTile('train_station')
board[15] = BoardTile.BoardTile('train_station')
board[25] = BoardTile.BoardTile('train_station')
board[35] = BoardTile.BoardTile('train_station')

board[12] = BoardTile.BoardTile('utility_bills')
board[28] = BoardTile.BoardTile('utility_bills')

#--------TESTING----------------
print(board[5] is board[35])
for tile in board:
    print(tile)