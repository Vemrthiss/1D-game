from assets.tiles import *
import assets.board.BoardInfo as BoardInfo
import random

num_tiles = BoardInfo.num_tiles #total number of tiles
max_tile_length = BoardInfo.max_tile_length
corner_difference = int(num_tiles/2)

#initialises an empty, new board
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

    fresh_board[5] = Station.Station('Jurong West', 200)
    fresh_board[15] = Station.Station('Bishan', 200)
    fresh_board[25] = Station.Station('Bedok', 250)
    fresh_board[35] = Station.Station('Harbourfront', 300)

    fresh_board[12] = Utility.Utility('PUB Water', 100)
    fresh_board[28] = Utility.Utility('SP Electricity', 150)

    #sets street tiles
    for street in BoardInfo.board_streets:
        street_pos = street['position']
        street_name = street['name']
        street_value = street['value']
        fresh_board[street_pos] = Street.Street(street_name, street_value)

    return fresh_board

def set_start_tile(board, players_ls):
    for player in players_ls:
        board[0].add_occupants(player) #adds ALL players to the start position

# receives a board list (from app state) and displays it
def display_board(board):
    first_row = ''
    for tile in board[:11]:
        first_row += f'{str(tile)}'
    print(f'\n----------------------------------------------------------------------THIS IS THE BOARD----------------------------------------------------------------------\n\n{first_row}')
    
    right_column = board[11:20]
    left_column = board[31:][::-1]

    for left_tile, right_tile in zip(left_column, right_column):
        row = str(left_tile) + (' '*max_tile_length*9) + str(right_tile)
        print(f'\n{row}')

    last_row = ''
    for tile in board[20:31][::-1]:
        last_row += f'{str(tile)}'
    print(f'\n{last_row}\n\n------------------------------------------------------------------------END OF BOARD-------------------------------------------------------------------------\n')

def update_board(board, players_ls):
    players_pos = [player.position for player in players_ls] #list of all current player positions
    for tile in board:
        tile.reset_occupants() #clears all tiles first
    for index, position in enumerate(players_pos):
        board[position].add_occupants(players_ls[index]) #index refers to that player object's index in the game_players state list

#-----------randomises and returns the list of chance and chest cards--------------
def init_chances():
    board_chances = BoardInfo.board_chances
    random.shuffle(board_chances)
    return board_chances

def init_chests():
    board_chests = BoardInfo.board_chests
    random.shuffle(board_chests)
    return board_chests