# --------Global variables-------

# Empty board
board= ["-","-","-",
        "-","-","-",
        "-","-","-"]

# if game is still going on
game_still_going = True

# Who won ? Or Tie?
winner = None

#Who's turn is it
current_player = "x"



def display_board():
  for index, item in enumerate(board,start=1):
    print(" "+item+" "+"|",end="")
    if not index % 3:
        print()


def play_game():

  # Display initial board     
  display_board()
  while game_still_going:

    # handle a single turn of arbitary player
    handle_turn(current_player)

    # check if the game has ended
    check_if_game_over()

    # flip to the other player
    flip_player()

  # Game has ended
  if winner =='x' or winner == 'o':
    print(winner+" won.")
  elif winner == None:
    print("Tie.")


def check_if_game_over():
  check_for_winner()
  check_if_tie()


def check_for_winner():
  # Setup global variable
  global winner

  # check rows
  row_winner = check_rows()
  
  # check coloumns
  col_winner = check_coloumns()

  # check diagnols
  diag_winner = check_diagnols()
  if row_winner:
    winner = row_winner
  elif col_winner:
    winner = col_winner
  elif diag_winner:
    winner = diag_winner
  else:
    winner = None
  return 

def check_rows():
  # Setting up global variable
  global game_still_going

  # Check if any of the row is having same value and is not empty
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"

  # If any row does have a match there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  
  # Returns the winner 'x' or 'o' 
  if row_1:
    return board[0]
  if row_2:
    return board[3]
  if row_3:
    return board[6]
  return


def check_coloumns():
   # Setting up global variable
  global game_still_going

  # Check if any of the row is having same value and is not empty
  col_1 = board[0] == board[3] == board[6] != "-"
  col_2 = board[1] == board[4] == board[7] != "-"
  col_3 = board[2] == board[5] == board[8] != "-"

  # If any row does have a match there is a win
  if col_1 or col_2 or col_3:
    game_still_going = False
  
  # Returns the winner 'x' or 'o' 
  if col_1:
    return board[0]
  if col_2:
    return board[1]
  if col_3:
    return board[2]
  return


def check_diagnols():
    # Setting up global variable
  global game_still_going

  # Check if any of the row is having same value and is not empty
  diag_1 = board[0] == board[4] == board[8] != "-"
  diag_2 = board[2] == board[4] == board[6] != "-"

  # If any row does have a match there is a win
  if diag_1 or diag_2:
    game_still_going = False
  
  # Returns the winner 'x' or 'o' 
  if diag_1:
    return board[0]
  if diag_2:
    return board[2]
  return


def check_if_tie():
  # global var declaration
  global game_still_going

  #if there is no vacant position in board it ties
  if '-' not in board:
    game_still_going = False
  return


def flip_player():
  #global variable we need
  global current_player

  # if current player was 'x' then change it to 'o'
  if current_player == 'x':
    current_player = 'o'
  else:
    current_player = 'x'
  return

# handle a single turn of arbitary player
def handle_turn(player):

  print(player+ "'s turn.")
  position = input("Choose a poistion from 1 to 9\n")
  
  valid = False
  while not valid:
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose position from 1 to 9\n")

    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Choose Again")

  board[position]=player
  display_board()


play_game()

# board
# display board
# play game
# handle turn
# check win
  #check rows
  #check coloumns 
  #check diagnols 
# check tie
# flip player

