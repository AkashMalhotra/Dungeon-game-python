import random
#Cells

Coordinates = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]


def get_locations():
  Possible_locations = Coordinates[:]
  Position = ()
  def _do_pos():
    Position = Possible_locations.pop(Possible_locations.index(random.choice(Possible_locations)))
    return Position
  monster = _do_pos()
  door = _do_pos()
  start = _do_pos()

  return monster, door, start



def move_player(player, Movement):
  a = player[0]
  b = player[1]
  if Movement == "LEFT":
      a -= 1
  elif Movement == "RIGHT":
      a += 1
  elif Movement == "UP":
      b += 1
  elif Movement == "DOWN":
      b -= 1
  player = (a, b)
  return player


def get_moves(player):
  MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
  if player[0] == 0:
      MOVES.remove("LEFT")
  if player[0] == 2:
      MOVES.remove("RIGHT")
  if player[1] == 0:
      MOVES.remove("DOWN")
  if player[1] == 2:
      MOVES.remove("UP")
  return MOVES


monsterpos, doorpos, playerpos = get_locations()
print("Welcome to the dungeon!")
while True:

  print("You're currently in room {}".format(playerpos))
  print("You can Move {}".format(get_moves(playerpos)))
  print("Enter QUIT to quit")

  Movement = input("> ")
  Movement = Movement.upper()

  if Movement == 'QUIT':
    break

  if Movement in get_moves(playerpos):
      playerpos = move_player(playerpos, Movement)
  elif Movement not in get_moves(playerpos):
      print("Error, can't move to that location!")

  if playerpos == doorpos:
      print("Congratulations, you made it through the dungeon!")

      quit()
  elif playerpos == monsterpos:
      print("The monster has got you!")

      quit()
  else:
      continue
