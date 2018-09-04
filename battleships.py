#! python2.

from random import randint
userTurn = 0
board = []

#create the game board with numbers to help with coordinates
board.append([" ", "1", "2", "3", "4", "5", "6", "7"])
board.append(["1", "O", "O", "O", "O", "O", "O", "O"])
board.append(["2", "O", "O", "O", "O", "O", "O", "O"])
board.append(["3", "O", "O", "O", "O", "O", "O", "O"])
board.append(["4", "O", "O", "O", "O", "O", "O", "O"])
board.append(["5", "O", "O", "O", "O", "O", "O", "O"])


#function to print the board each row on a new line
def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(1, len(board) - 1)

def random_col(board):
  return randint(1, len(board[0]) - 1)
#ship status variables, 10 indicates alive 0 idicates dead
ship1Status = 10
ship2Status = 10
#assign coordinates of battleship 1
ship_row = random_row(board)
ship_col = random_col(board)

#assign coordinates of ship 2, ensuring they do not match ship 1
ship2_row = random_row(board)
while ship2_row == ship_row:
  ship2_row = random_row(board)

ship2_col = random_col(board)
while ship2_col == ship_col:
  ship2_col = random_col(board)




# Creating an infinte while loop so the user can keep playing until they win


while True:
  #ship locations displayed for debugging purposes
  print "ship 1 row ", ship_row 
  print "ship 1 col ", ship_col 
  print "ship 2 row ", ship2_row 
  print "ship 2 col ", ship2_col 
  userTurn += 1
  

  
  if ship1Status == 0 and ship2Status == 0:
    print "Well played! You took out both of my battleships! come back and play again soon!"
    break
  print "================= Turn #",  userTurn,  " ====================="
  
  #input validation for row
  rowInput = raw_input("Guess Row: ")
  while rowInput.isdigit() == False:
    rowInput = raw_input("Please enter a positive integer ")
  guess_row = int(rowInput)
  
  colInput= raw_input("Guess Col ")
  while colInput.isdigit() == False:
    colInput = raw_input("Please enter a positive integer ")
  guess_col = int(colInput)


  
  if guess_row < 1 or guess_row > 5 or guess_col < 1 or guess_col > 7:
    print "Ooops! that's not even in the water!"  
    

  elif board[guess_row][guess_col] == "1":
    print "You've already sank battleship 1!"

  elif board[guess_row][guess_col] == "2":
    print "You've already sank battleship 2!"

  elif guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship 1!"
    board[guess_row][guess_col] = "1"
    
    #changeship status to dead
    ship1Status = 0
    
    

  elif guess_row == ship2_row and guess_col == ship2_col:
    print "Congratulations! You sank my battleship 2!"
    board[guess_row][guess_col] = "2"
    
    #change ship status to dead
    ship2Status = 0

    
  elif guess_row < 1 or guess_row > 5 or guess_col < 1 or guess_col > 7:
    print "Ooops! that's not even in the water!"

  else:
    
    if board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
      

    else:
      print "You missed my battleships!"
      board[guess_row][guess_col] = "X"
    
        
  print_board(board)

"""
  guess_col = int(raw_input("Guess Col: "))
  while guess_col < 1 or guess_col > 7:
    guess_col = int(raw_input("Oops! That's not even in the ocean! try again "))
  """




