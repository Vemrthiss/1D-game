from assets.tiles import *
import assets.board.BoardInfo as BoardInfo

num_tiles = BoardInfo.num_tiles #total number of tiles
max_tile_length = BoardInfo.max_tile_length
corner_difference = int(num_tiles/2)

def init_board():
    fresh_board = [f"{'x': <{max_tile_length}}" for num in range(num_tiles)]

    #setting ALL tile positions
    fresh_board[0] = CornerTiles.Start()
    fresh_board[corner_difference] = CornerTiles.Parking()
    fresh_board[10] = CornerTiles.Jail()
    fresh_board[10+corner_difference] = CornerTiles.GoJail()

    #cannot assign multiple variables to the same value at once (else all point to same object)
    fresh_board[7] = Chance.Chance()
    fresh_board[22] = Chance.Chance()
    fresh_board[36] = Chance.Chance()
    fresh_board[2] = Chest.Chest()
    fresh_board[17] = Chest.Chest()
    fresh_board[33] = Chest.Chest()

    fresh_board[4] = Tax.Tax('small')
    fresh_board[38] = Tax.Tax('large')

    fresh_board[5] = Station.Station('Jurong West')
    fresh_board[15] = Station.Station('Ang Mo Kio')
    fresh_board[25] = Station.Station('Bedok')
    fresh_board[35] = Station.Station('Harbourfront')

    fresh_board[12] = Utility.Utility('Water Bills')
    fresh_board[28] = Utility.Utility('Electricity Bills')

    return fresh_board


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