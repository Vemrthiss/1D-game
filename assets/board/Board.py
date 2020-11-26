import BoardTile
import BoardInfo

num_tiles = BoardInfo.num_tiles #total number of tiles
max_tile_length = BoardInfo.max_tile_length

board = [f"{'x': <{max_tile_length}}" for num in range(num_tiles)]
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
def display_board(board):
    first_row = ''
    for tile in board[:11]:
        first_row += f'{str(tile)}'
    print(first_row)
    
    right_column = board[11:20]
    left_column = board[31:][::-1]

    for left_tile, right_tile in zip(left_column, right_column):
        row = str(left_tile) + (' '*max_tile_length*9) + str(right_tile)
        print(row)

    last_row = ''
    for tile in board[20:31][::-1]:
        last_row += f'{str(tile)}'
    print(last_row)

display_board(board)