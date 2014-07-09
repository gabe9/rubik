import cube
import moves

colors = {1:'g', 2:'r', 3:'b', 4:'o', 5:'y', 6:'w'}

def printCubie(array):
  counter = 0
  for element in array:#array of tuples
    counter += 1
    ans = ""
    for side in element:
      ans += colors[side] 
    print ans

def printFront():
  print colors[cube.map[6][3]], colors[cube.map[6][4]], colors[cube.map[6][5]]
  print colors[cube.map[7][3]], colors[cube.map[7][4]], colors[cube.map[7][5]]
  print colors[cube.map[8][3]], colors[cube.map[8][4]], colors[cube.map[8][5]]

def printTop():
  print colors[cube.map[3][3]], colors[cube.map[3][4]], colors[cube.map[3][5]]
  print colors[cube.map[4][3]], colors[cube.map[4][4]], colors[cube.map[4][5]]
  print colors[cube.map[5][3]], colors[cube.map[5][4]], colors[cube.map[5][5]]

def printBot():
  print colors[cube.map[9][3]], colors[cube.map[9][4]], colors[cube.map[9][5]]
  print colors[cube.map[10][3]], colors[cube.map[10][4]], colors[cube.map[10][5]]
  print colors[cube.map[11][3]], colors[cube.map[11][4]], colors[cube.map[11][5]]

def printBack():
  print colors[cube.map[0][3]], colors[cube.map[0][4]], colors[cube.map[0][5]]
  print colors[cube.map[1][3]], colors[cube.map[1][4]], colors[cube.map[1][5]]
  print colors[cube.map[2][3]], colors[cube.map[2][4]], colors[cube.map[2][5]]

def printLeft():
  print colors[cube.map[3][0]], colors[cube.map[3][1]], colors[cube.map[3][2]]
  print colors[cube.map[4][0]], colors[cube.map[4][1]], colors[cube.map[4][2]]
  print colors[cube.map[5][0]], colors[cube.map[5][1]], colors[cube.map[5][2]]

def printRight():
  print colors[cube.map[3][6]], colors[cube.map[3][7]], colors[cube.map[3][8]]
  print colors[cube.map[4][6]], colors[cube.map[4][7]], colors[cube.map[4][8]]
  print colors[cube.map[5][6]], colors[cube.map[5][7]], colors[cube.map[5][8]]

def printCube():
  print
  print "Top"
  printTop()
  print "Front"
  printFront()
  print "Bottom"
  printBot()
  print "Back"
  printBack()
  print "Left"
  printLeft()
  print "Right"
  printRight()
  print

def testAllMoves():
  printCube()
  moves.cRight()
  print "cRight"
  printCube()
  moves.cBot()
  print "cBot"
  printCube()
  moves.cRight()
  print "cRight"
  printCube()
  moves.ccLeft()
  print "ccLeft"
  printCube()
  moves.cTop()
  print "cTop"
  printCube()
  moves.ccBot()
  print "ccBot"
  printCube()
  moves.cFront()
  print "cFront"
  printCube()
  moves.cLeft()
  print "cLeft"
  printCube()
  moves.ccRight()
  print "ccRight"
  printCube()
  moves.cTop()
  print "cTop"
  printCube()
  moves.cBot()
  print "cBot"
  printCube()
  moves.cBack()
  print "cBack"
  printCube()
  moves.ccBot()
  print "ccBot"
  printCube()
  moves.ccBack()
  print "ccBack"
  printCube()
  moves.ccBack()
  print "ccBack"
  printCube()
  moves.cRight()
  print "cRight"
  printCube()
