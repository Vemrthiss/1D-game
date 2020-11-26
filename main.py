import assets.Player as player
import assets.Property as prop
import assets.board.Board as board
import assets.board.BoardTile as boardTile

# ----------------------------------APPLICATION STATE TO INITIALISE----------------------------------
game_players = []
game_properties = [] #list of all 22 houses to be on the board
#game_board = 


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



# ------------------------------------------------TESTING---------------------------------------------------
for user in game_players:
    print(user)