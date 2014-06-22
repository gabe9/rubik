import tests
import moves
import cube
from random import randrange

def scramble():
  scrambleMoves = []
  for i in range(25):
    index = randrange(len(cube.possibleMoves))
    scrambleMoves.append(cube.possibleMoves[index])
  moves.move(scrambleMoves)

#tests.testAllMoves()

scramble()#scrambles cube
tests.printCube()

