import assets.Player as player
import assets.board.Board as board

# ----------------------------------APPLICATION STATE TO INITIALISE----------------------------------
game_players = []
game_properties = [] #list of all 22 houses to be on the board
game_board = board.init_board() # initalises a persisting BOARD STATE, to be taken reference whenever the board is to be printed

#rewriting imported functions as they always take the same arguments
def update_board():
    board.update_board(game_board, game_players)

def display_board():
    board.display_board(game_board)



# ----------------------------------------GAME LOOP---------------------------------------
# welcome message
print('For the best experience, please maximise your terminal :)')
# asks for number of players
num_players = input('Welcome to Python Monopoly! How many players do we have today? ')
while not num_players.isdigit():
    print('Please enter a number')
    num_players = input('Welcome to Python Monopoly! How many players do we have today? ')
num_players = int(num_players)

# instantiates that number of players and adds to game
for player_no in range(1, num_players+1):
    game_players.append(player.Player(player_no))

# asks that user for their token/initials for board display, and updates the state
for user in game_players:
    user_token = input(f'Dear Player {user.player_no}, please enter your initials which will be displayed on the board. ')
    while not user_token: #runs if user_token is an empty string, a falsey value
        print('Please enter something')
        user_token = input(f'Dear Player {user.player_no}, please enter your initials which will be displayed on the board. ')
    user.set_token(user_token)

# prints inital board
display_board()

#for testing: assigning player object(s) a position through hard coding
test_user = game_players[0]
test_user.update_position(2) #gives the player object a new position at pos 2
print(game_players[0]) #verifies that the above action updates the app state of game players
update_board()
display_board()
print(game_board[2].occupants)
test_user2 = game_players[1]
test_user2.update_position(4)
print(game_players[1])
update_board()
display_board()
print(game_board[4].occupants)
test_user.update_position(4)
print(game_players[0])
update_board()
display_board()
print(game_board[4].occupants)

# ------------------------------------------------TESTING---------------------------------------------------
# for user in game_players:
#     print(user)