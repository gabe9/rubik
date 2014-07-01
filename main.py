import tests
import cube
from random import randrange

def scramble():
  scrambleMoves = []
  for i in range(25):
    index = randrange(len(cube.possibleMoves))
    scrambleMoves.append(cube.possibleMoves[index])
  cube.move(scrambleMoves)

#tests.testAllMoves()

# scramble()#scrambles cube
tests.printCube()

print "Corners:"
tests.printArray(cube.getCorners())
print "Edges:"
tests.printArray(cube.getEdges())
