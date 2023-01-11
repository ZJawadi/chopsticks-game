#this is a program that simulates the game chopsticks between two players
#Zorah V. Jawadi

#global variables
winner2 = None
player_1_hand = [1,1]
player_2_hand = [1,1]
chopstick = "|"

#function to display the chopsticks
def display(player,player_1_hand):
  print("{}'s hand: Hand 1: {}    Hand 2: {}".format(player, chopstick*player_1_hand[0],chopstick*player_1_hand[1]))

#function that allows a player to "attack" the other
def attack(player_1_hand, player_2_hand):
  #output
  print("\033[H\033[J") 
  print("YOU CHOSE ATTACK!")
  print("This is the current board: ")
  display(player_1, player_1_hand)
  display(player_2, player_2_hand)

  #choose the hand to attack
  while True:
    try:
      attack_player = input("\nChoose hand 1 or hand 2 of the other player to attack (pick 1 or 2): ")
      if attack_player in {"1","2"}:
        break
    except:
      pass
    print("Incorrect selection. Try again.")

  #choose to attack with which hand
  while True:
    try:
      with_hand = input("\nYou attack with which hand? (pick 1 or 2): ")
      if with_hand in {"1","2"}:
        break
    except:
      pass
    print("Incorrect selection. Try again.")

  #adding chopsticks to the attacked player's hand
  if attack_player in "1" and with_hand in "1":
    player_2_hand[0] += player_1_hand[0]

  if attack_player in "1" and with_hand in "2":
    player_2_hand[0] += player_1_hand[1]

  if attack_player in "2" and with_hand in "1":
    player_2_hand[1] += player_1_hand[0]

  if attack_player in "2" and with_hand in "2":
    player_2_hand[1] += player_1_hand[1]

  input("Press Enter to continue...")
  return player_1_hand, player_2_hand

#function that allows a player to "split" their chopsticks
def split(player, player_hand):
  while True:
    #output
    print("\033[H\033[J")
    print("YOU CHOSE SPLIT!")
    print("This is your hand: ")
    display(player, player_hand)

    #choosing which hand to add chopsticks to
    try:
      while True:
        try:
          hand = input("\nWhich hand would you like to add to? (1 or 2): ")
          if hand in {"1","2"}:
            break
        except:
          pass
        print("Incorrect selection. Try again.")

      #choosing the number of chopsticks
      while True:
        try:
          number = int(input("\nNumber of chopsticks you would like to add?: "))
          if 0<number<5:
            break
        except:
          pass
        print("Incorrect number of chopsticks, please pick a number between 1 and 5.")

      #ensures not too many chopsticks are added or subtracted
      if hand in "1":
        if player_hand[0] + number < 5 and player_hand[1] - number > -1:
          player_hand[0] += number
          player_hand[1] -= number
          break
      #ensures not too many chopsticks are added or subtracted
      if hand in "2":
        if player_hand[1] + number < 5 and player_hand[0] - number > -1:
          player_hand[1] += number
          player_hand[0] -= number
          break
    except:
      pass
    print("\nThere was an error computing your split. Try again with a different number of chopsticks.")
    input("Press Enter to continue...")
 
  input("Press Enter to continue...")
  return player_hand

#function that sets a hand with five or more chopsticks to zero 
def fivetozero(player, player_hand):
  print("\033[H\033[J")
  for x in range(-1, len(player_hand)-1):
    if player_hand[x] >= 5:
      print("{}'s hand {} has reached five fingers! Now it will be set to zero.".format(player, x+1))
      player_hand[x] = 0
      input("Press Enter to continue...")

#function that determined if a player has no chopsticks
def winner(player_1_hand):
  if player_1_hand[0] == 0 and player_1_hand[1] == 0:
    return player_1
  return None

#function that allows a player their turn
def play(player, yourhand, otherhand):
  #output
  print("\033[H\033[J") 
  print("---IT IS {}'S TURN---".format(player))
  print("This is the current board: ")
  display(player_1, player_1_hand)
  display(player_2, player_2_hand)

  #Choose to attack or split
  while True:
    try:
      choice = input("\nWould you like to A) attack the other player or B) split your chopsticks?: ")
      if choice in {"a", "A"}:
        attack(yourhand, otherhand)
        break
      if choice in {"b", "B"}:
        split(player, yourhand)
        break
    except:
      pass
    print("You did not pick correctly. Try again.")

#function that shows the winner
def exit_screen(player):
  print("\033[H\033[J") 
  print("Congratulations! {} wins!".format(player))

#user input
player_1 = input("Enter the name of Player 1: ")
player_2 = input("Enter the name of Player 2: ")

#loop until a winner is determined
while True:
  play(player_1, player_1_hand, player_2_hand)
  fivetozero(player_2, player_2_hand)
  winner2 = winner(player_2_hand)
  if winner2 != None:
    exit_screen(player_1)
    break
  play(player_2,player_2_hand, player_1_hand)
  fivetozero(player_1, player_1_hand)
  winner2 = winner(player_1_hand)
  if winner2 != None:
    exit_screen(player_2)
    break