import random

# Define game board size
MAX_VALUE = 100

# Define snakes and ladders (modify these as needed)
snakes = {16: 6, 49: 11, 56: 53, 62: 19, 98: 1}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 84: 91}

def roll_dice():
  """Simulates a dice roll between 1 and 6."""
  return random.randint(1, 6)

def move_player(current_position, dice_roll):
  """Calculates the new position after a dice roll.

  Args:
      current_position: The player's current position on the board.
      dice_roll: The outcome of the dice roll.

  Returns:
      int: The player's new position on the board.
  """
  new_position = current_position + dice_roll

  # Check for snakes and ladders
  if new_position in snakes:
    new_position = snakes[new_position]
    print("Ouch! Landed on a snake. Slithering down to", new_position)
  elif new_position in ladders:
    new_position = ladders[new_position]
    print("Yay! Climbed a ladder to", new_position)

  # Handle going over the board limit (bounce back)
  if new_position > MAX_VALUE:
    print("Oops! Rolled too high. Bouncing back to", current_position)
    new_position = current_position

  return new_position

def play_game():
  """Simulates a single game of Snake and Ladders."""
  player_position = 1
  current_player = "Player 1"

  while player_position < MAX_VALUE:
    dice_result = roll_dice()
    print(f"{current_player}'s turn. Rolled a {dice_result}")

    player_position = move_player(player_position, dice_result)

    print(f"{current_player} is now on position {player_position}")

    # Check for win
    if player_position == MAX_VALUE:
      print(f"{current_player} wins!")
      break

    # Switch turns if not a six
    if dice_result != 6:
      current_player = "Player 2" if current_player == "Player 1" else "Player 1"

# Start the game
play_game()
