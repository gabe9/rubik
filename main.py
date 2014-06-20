import tests
import moves
import globals
from random import randrange

def scramble():
  scrambleMoves = []
  for i in range(25):
    index = randrange(len(globals.possibleMoves))
    scrambleMoves.append(globals.possibleMoves[index])
  moves.move(scrambleMoves)

#tests.testAllMoves()

scramble()#scrambles cube
tests.printCube()

