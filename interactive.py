import os  #OS for Python operating platform
import sys  #SYS for system internals and clean exit sequence
import time  #time for sleep and display time
from random import shuffle
import random  #random for card selection



if os.name == "nt":  #ANSI for Windows Terminal/Console
  os.system("")

pyv = sys.version  #Determining Python version for compatibility
pyversion = pyv[1]



def homescreen():
  print("""
        Card Game

 by Seron Chanderabose.
 """)
  print("Playing on", os.name.upper(),"for Python")


#Start screen
def loadin():
  print("Loading Game")
  time.sleep(0.15)
  os.system('cls' if os.name == 'nt' else 'clear')

  print("Game Loaded.")
  time.sleep(0.3)
  os.system('cls' if os.name == 'nt' else 'clear')



loadin()
homescreen()



def Leave_Game():  #Exit sequence
  print("Exiting Game...")
  time.sleep(0.6)
  sys.exit("""Thank you for playing!
""")



#Play or Exit
gameLoop = True
Exiter = True

while gameLoop:
  while Exiter:
    pl = str(input("Play or Exit? P/E: "))
    pl = pl.lower()

    #Play
    if pl == "p":
      print("Loading Gamemode...")
      print()
      time.sleep(0.4)
      Exiter = False
      gameLoop = False
      os.system('cls' if os.name == 'nt' else 'clear')


    #Exit
    elif pl == "e":
      Leave_Game()


    #False input (!= P or E)
    else:
      print("Press 'P' key for 'play' or 'E' key for 'exit'. Then press ENTER.")
      pass



#cards
class Card:
  suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

  values = [
    None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen",
    "King", "Ace"
  ]


  def __init__(self, v, s):
    #suit + value are ints
    self.value = v
    self.suit = s

  def __lt__(self, c2):
    if self.value < c2.value:
      return True
    if self.value == c2.value:
      if self.suit < c2.suit:
        return True
      else:
        return False
    return False

  def __gt__(self, c2):
    if self.value > c2.value:
      return True
    if self.value == c2.value:
      if self.suit > c2.suit:
        return True
      else:
        return False
    return False

  def __repr__(self):
    v = self.values[self.value] +\
        " of " + \
        self.suits[self.suit]
    return v



class Deck:

  def __init__(self):
    self.cards = []
    for i in range(2, 15):
      for j in range(4):
        self.cards\
            .append(Card(i,
                         j))
    shuffle(self.cards)

  def rm_card(self):
    if len(self.cards) == 0:
      return
    return self.cards.pop()



class Player:

  def __init__(self, name):
    self.wins = 0
    self.card = None
    self.name = name



class Game:

  def __init__(self):
    name1 = input("Player 1 Name? ")
    name1 = name1.capitalize()
    name2 = input("Player 2 Name? ")
    name2 = name2.capitalize()
    self.deck = Deck()
    self.p1 = Player(name1)
    self.p2 = Player(name2)

  def wins(self, winner):
    w = "{} wins this round."
    w = w.format(winner)
    print(w)

  def draw(self, p1n, p1c, p2n, p2c):
    d = "{} drew {} {} drew {}"
    d = d.format(p1n, p1c, p2n, p2c)
    print(d)

  def play_game(self):
    cards = self.deck.cards
    print(" - Beginning Game - ")
    print()
    
    while len(cards) >= 2:
      m = "Type 'Q' to quit. Type ENTER to play:"
      response = input(m)
      if response == 'q':
        break
    
      p1c = self.deck.rm_card()
      p2c = self.deck.rm_card()
      p1n = self.p1.name
      p2n = self.p2.name
      self.draw(p1n, p1c, p2n, p2c)
      
      if p1c > p2c:
        self.p1.wins += 1
        self.wins(self.p1.name)
        
      else:
        self.p2.wins += 1
        self.wins(self.p2.name)

    win = self.winner(self.p1, self.p2)
    print("War is over. {} wins".format(win))

  def winner(self, p1, p2):
    if p1.wins > p2.wins:
      return p1.name
    if p1.wins < p2.wins:
      return p2.name
    return "It was a tie!"



game = Game()
game.play_game()
input("Press ENTER to quit:")
Leave_Game()
