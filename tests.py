import globals
import moves

colors = {1:'g', 2:'r', 3:'b', 4:'o', 5:'y', 6:'w'}

def testAlgo():
  moves.ccRight()
  moves.ccBot()
  moves.cRight()
  moves.cBot()

def printFront():
  print colors[globals.cube[6][3]], colors[globals.cube[6][4]], colors[globals.cube[6][5]]
  print colors[globals.cube[7][3]], colors[globals.cube[7][4]], colors[globals.cube[7][5]]
  print colors[globals.cube[8][3]], colors[globals.cube[8][4]], colors[globals.cube[8][5]]

def printTop():
  print colors[globals.cube[3][3]], colors[globals.cube[3][4]], colors[globals.cube[3][5]]
  print colors[globals.cube[4][3]], colors[globals.cube[4][4]], colors[globals.cube[4][5]]
  print colors[globals.cube[5][3]], colors[globals.cube[5][4]], colors[globals.cube[5][5]]

def printBot():
  print colors[globals.cube[9][3]], colors[globals.cube[9][4]], colors[globals.cube[9][5]]
  print colors[globals.cube[10][3]], colors[globals.cube[10][4]], colors[globals.cube[10][5]]
  print colors[globals.cube[11][3]], colors[globals.cube[11][4]], colors[globals.cube[11][5]]

def printBack():
  print colors[globals.cube[0][3]], colors[globals.cube[0][4]], colors[globals.cube[0][5]]
  print colors[globals.cube[1][3]], colors[globals.cube[1][4]], colors[globals.cube[1][5]]
  print colors[globals.cube[2][3]], colors[globals.cube[2][4]], colors[globals.cube[2][5]]

def printLeft():
  print colors[globals.cube[3][0]], colors[globals.cube[3][1]], colors[globals.cube[3][2]]
  print colors[globals.cube[4][0]], colors[globals.cube[4][1]], colors[globals.cube[4][2]]
  print colors[globals.cube[5][0]], colors[globals.cube[5][1]], colors[globals.cube[5][2]]

def printRight():
  print colors[globals.cube[3][6]], colors[globals.cube[3][7]], colors[globals.cube[3][8]]
  print colors[globals.cube[4][6]], colors[globals.cube[4][7]], colors[globals.cube[4][8]]
  print colors[globals.cube[5][6]], colors[globals.cube[5][7]], colors[globals.cube[5][8]]

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
