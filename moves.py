import globals
def cTop():#rotate top clockwise
  #rotate top face
  temp = globals.cube[3][3] 
  globals.cube[3][3] = globals.cube[5][3]
  globals.cube[5][3] = globals.cube[5][5]
  globals.cube[5][5] = globals.cube[3][5]
  globals.cube[3][5] = temp
  temp = globals.cube[3][4]
  globals.cube[3][4] = globals.cube[4][3]
  globals.cube[4][3] = globals.cube[5][4]
  globals.cube[5][4] = globals.cube[4][5]
  globals.cube[4][5] = temp

  #rotate top layer
  temp = globals.cube[2][3]
  globals.cube[2][3] = globals.cube[5][2]
  globals.cube[5][2] = globals.cube[6][5]
  globals.cube[6][5] = globals.cube[3][6]
  globals.cube[3][6] = temp
  temp = globals.cube[2][4]
  globals.cube[2][4] = globals.cube[4][2]
  globals.cube[4][2] = globals.cube[6][4]
  globals.cube[6][4] = globals.cube[4][6]
  globals.cube[4][6] = temp
  temp = globals.cube[2][5]
  globals.cube[2][5] = globals.cube[3][2]
  globals.cube[3][2] = globals.cube[6][3]
  globals.cube[6][3] = globals.cube[5][6]
  globals.cube[5][6] = temp

def ccTop():#rotate top counterclockwise
  #rotate top face
  temp = globals.cube[3][3]
  globals.cube[3][3] = globals.cube[3][5]
  globals.cube[3][5] = globals.cube[5][5]
  globals.cube[5][5] = globals.cube[5][3]
  globals.cube[5][3] = temp
  temp = globals.cube[3][4]
  globals.cube[3][4] = globals.cube[4][5]
  globals.cube[4][5] = globals.cube[5][4]
  globals.cube[5][4] = globals.cube[4][3]
  globals.cube[4][3] = temp

  #rotate top layer
  temp = globals.cube[2][3]
  globals.cube[2][3] = globals.cube[3][6]
  globals.cube[3][6] = globals.cube[6][5]
  globals.cube[6][5] = globals.cube[5][2]
  globals.cube[5][2] = temp
  temp = globals.cube[2][4]
  globals.cube[2][4] = globals.cube[4][6]
  globals.cube[4][6] = globals.cube[6][4]
  globals.cube[6][4] = globals.cube[4][2]
  globals.cube[4][2] = temp
  temp = globals.cube[2][5]
  globals.cube[2][5] = globals.cube[5][6]
  globals.cube[5][6] = globals.cube[6][3]
  globals.cube[6][3] = globals.cube[3][2]
  globals.cube[3][2] = temp


def cFront():#rotate front colockwise
  #rotate front face
  temp = globals.cube[6][3]
  globals.cube[6][3] = globals.cube[8][3]
  globals.cube[8][3] = globals.cube[8][5]
  globals.cube[8][5] = globals.cube[6][5]
  globals.cube[6][5] = temp
  temp = globals.cube[6][4]
  globals.cube[6][4] = globals.cube[7][3]
  globals.cube[7][3] = globals.cube[8][4]
  globals.cube[8][4] = globals.cube[7][5]
  globals.cube[7][5] = temp

  #rotate front layer
  temp = globals.cube[5][3]
  globals.cube[5][3] = globals.cube[5][0]
  globals.cube[5][0] = globals.cube[9][5]
  globals.cube[9][5] = globals.cube[5][6]
  globals.cube[5][6] = temp
  temp = globals.cube[5][4]
  globals.cube[5][4] = globals.cube[5][1]
  globals.cube[5][1] = globals.cube[9][4]
  globals.cube[9][4] = globals.cube[5][7]
  globals.cube[5][7] = temp
  temp = globals.cube[5][5]
  globals.cube[5][5] = globals.cube[5][2]
  globals.cube[5][2] = globals.cube[9][3]
  globals.cube[9][3] = globals.cube[5][8]
  globals.cube[5][8] = temp

def ccFront():#rotate front counterclockwise
  #rotate front face
  temp = globals.cube[6][3]
  globals.cube[6][3] = globals.cube[6][5]
  globals.cube[6][5] = globals.cube[8][5]
  globals.cube[8][5] = globals.cube[8][3]
  globals.cube[8][3] = temp
  temp = globals.cube[6][4]
  globals.cube[6][4] = globals.cube[7][5]
  globals.cube[7][5] = globals.cube[8][4]
  globals.cube[8][4] = globals.cube[7][3]
  globals.cube[7][3] = temp

  #rotate front layer
  temp = globals.cube[5][3]
  globals.cube[5][3] = globals.cube[5][6]
  globals.cube[5][6] = globals.cube[9][5]
  globals.cube[9][5] = globals.cube[5][0]
  globals.cube[5][0] = temp
  temp = globals.cube[5][4]
  globals.cube[5][4] = globals.cube[5][7]
  globals.cube[5][7] = globals.cube[9][4]
  globals.cube[9][4] = globals.cube[5][1]
  globals.cube[5][1] = temp
  temp = globals.cube[5][5]
  globals.cube[5][5] = globals.cube[5][8]
  globals.cube[5][8] = globals.cube[9][3]
  globals.cube[9][3] = globals.cube[5][2]
  globals.cube[5][2] = temp

def cRight():#rotate right clockwise
  #rotate right face
  temp = globals.cube[3][6]
  globals.cube[3][6] = globals.cube[5][6]
  globals.cube[5][6] = globals.cube[5][8]
  globals.cube[5][8] = globals.cube[3][8]
  globals.cube[3][8] = temp
  temp = globals.cube[3][7]
  globals.cube[3][7] = globals.cube[4][6]
  globals.cube[4][6] = globals.cube[5][7]
  globals.cube[5][7] = globals.cube[4][8]
  globals.cube[4][8] = temp

  #rotate right layer
  temp = globals.cube[2][5]
  globals.cube[2][5] = globals.cube[5][5]
  globals.cube[5][5] = globals.cube[8][5]
  globals.cube[8][5] = globals.cube[11][5]
  globals.cube[11][5] = temp
  temp = globals.cube[1][5]
  globals.cube[1][5] = globals.cube[4][5]
  globals.cube[4][5] = globals.cube[7][5]
  globals.cube[7][5] = globals.cube[10][5]
  globals.cube[10][5] = temp
  temp = globals.cube[0][5]
  globals.cube[0][5] = globals.cube[3][5]
  globals.cube[3][5] = globals.cube[6][5]
  globals.cube[6][5] = globals.cube[9][5]
  globals.cube[9][5] = temp

def ccRight():#rotate right counterclockwise
  #rotate right face
  temp = globals.cube[3][6]
  globals.cube[3][6] = globals.cube[3][8]
  globals.cube[3][8] = globals.cube[5][8]
  globals.cube[5][8] = globals.cube[5][6]
  globals.cube[5][6] = temp
  temp = globals.cube[3][7]
  globals.cube[3][7] = globals.cube[4][8]
  globals.cube[4][8] = globals.cube[5][7]
  globals.cube[5][7] = globals.cube[4][6]
  globals.cube[4][6] = temp

  #rotate right layer
  temp = globals.cube[2][5]
  globals.cube[2][5] = globals.cube[11][5]
  globals.cube[11][5] = globals.cube[8][5]
  globals.cube[8][5] = globals.cube[5][5]
  globals.cube[5][5] = temp
  temp = globals.cube[1][5]
  globals.cube[1][5] = globals.cube[10][5]
  globals.cube[10][5] = globals.cube[7][5]
  globals.cube[7][5] = globals.cube[4][5]
  globals.cube[4][5] = temp
  temp = globals.cube[0][5]
  globals.cube[0][5] = globals.cube[9][5]
  globals.cube[9][5] =globals.cube[6][5]
  globals.cube[6][5] = globals.cube[3][5]
  globals.cube[3][5] = temp

def cLeft():#rotate left clockwise
  #rotate left face
  temp = globals.cube[3][0]
  globals.cube[3][0] = globals.cube[5][0]
  globals.cube[5][0] = globals.cube[5][2]
  globals.cube[5][2] = globals.cube[3][2]
  globals.cube[3][2] = temp
  temp = globals.cube[3][1]
  globals.cube[3][1] = globals.cube[4][0]
  globals.cube[4][0] = globals.cube[5][1]
  globals.cube[5][1] = globals.cube[4][2]
  globals.cube[4][2] = temp

  #rotate left layer
  temp = globals.cube[0][3]
  globals.cube[0][3] = globals.cube[9][3]
  globals.cube[9][3] = globals.cube[6][3]
  globals.cube[6][3] = globals.cube[3][3]
  globals.cube[3][3] = temp
  temp = globals.cube[1][3]
  globals.cube[1][3] = globals.cube[10][3]
  globals.cube[10][3] = globals.cube[7][3]
  globals.cube[7][3] = globals.cube[4][3]
  globals.cube[4][3] = temp
  temp = globals.cube[2][3]
  globals.cube[2][3] = globals.cube[11][3]
  globals.cube[11][3] = globals.cube[8][3]
  globals.cube[8][3] = globals.cube[5][3]
  globals.cube[5][3] = temp

def ccLeft():#rotate left counterclockwise
  #rotate left face
  temp = globals.cube[3][0]
  globals.cube[3][0] = globals.cube[3][2]
  globals.cube[3][2] = globals.cube[5][2]
  globals.cube[5][2] = globals.cube[5][0]
  globals.cube[5][0] = temp
  temp = globals.cube[3][1]
  globals.cube[3][1] = globals.cube[4][2]
  globals.cube[4][2] = globals.cube[5][1]
  globals.cube[5][1] = globals.cube[4][0]
  globals.cube[4][0] = temp

  #rotate left layer
  temp = globals.cube[0][3]
  globals.cube[0][3] = globals.cube[3][3]
  globals.cube[3][3] = globals.cube[6][3]
  globals.cube[6][3] = globals.cube[9][3]
  globals.cube[9][3] = temp
  temp = globals.cube[1][3]
  globals.cube[1][3] = globals.cube[4][3]
  globals.cube[4][3] = globals.cube[7][3]
  globals.cube[7][3] = globals.cube[10][3]
  globals.cube[10][3] = temp
  temp = globals.cube[2][3]
  globals.cube[2][3] = globals.cube[5][3]
  globals.cube[5][3] = globals.cube[8][3]
  globals.cube[8][3] = globals.cube[11][3]
  globals.cube[11][3] = temp

def cBack():#rotae back clockwise
  #rotate left face
  temp = globals.cube[0][3]
  globals.cube[0][3] = globals.cube[2][3]
  globals.cube[2][3] = globals.cube[2][5]
  globals.cube[2][5] = globals.cube[0][5]
  globals.cube[0][5] = temp
  temp = globals.cube[0][4]
  globals.cube[0][4] = globals.cube[1][3]
  globals.cube[1][3] = globals.cube[2][4]
  globals.cube[2][4] = globals.cube[1][5]
  globals.cube[1][5] = temp

  #rotate left layer
  temp = globals.cube[11][3]
  globals.cube[11][3] = globals.cube[3][2]
  globals.cube[3][2] = globals.cube[3][5]
  globals.cube[3][5] = globals.cube[3][8]
  globals.cube[3][8] = temp
  temp = globals.cube[11][4]
  globals.cube[11][4] = globals.cube[3][1]
  globals.cube[3][1] = globals.cube[3][4]
  globals.cube[3][4] = globals.cube[3][7]
  globals.cube[3][7] = temp
  temp = globals.cube[11][5]
  globals.cube[11][5] = globals.cube[3][0]
  globals.cube[3][0] = globals.cube[3][3]
  globals.cube[3][3] = globals.cube[3][6]
  globals.cube[3][6] = temp

def ccBack():#rotate back counterclockwise
  #rotate back face
  temp = globals.cube[0][3]
  globals.cube[0][3] = globals.cube[0][5]
  globals.cube[0][5] = globals.cube[2][5]
  globals.cube[2][5] = globals.cube[2][3]
  globals.cube[2][3] = temp
  temp = globals.cube[0][4]
  globals.cube[0][4] = globals.cube[1][5]
  globals.cube[1][5] = globals.cube[2][4]
  globals.cube[2][4] = globals.cube[1][3]
  globals.cube[1][3] = temp

  #rotate back layer
  temp = globals.cube[11][3]
  globals.cube[11][3] = globals.cube[3][8]
  globals.cube[3][8] = globals.cube[3][5]
  globals.cube[3][5] = globals.cube[3][2]
  globals.cube[3][2] = temp
  temp = globals.cube[11][4]
  globals.cube[11][4] = globals.cube[3][7]
  globals.cube[3][7] = globals.cube[3][4]
  globals.cube[3][4] = globals.cube[3][1]
  globals.cube[3][1] = temp
  temp = globals.cube[11][5]
  globals.cube[11][5] = globals.cube[3][6]
  globals.cube[3][6] = globals.cube[3][3]
  globals.cube[3][3] = globals.cube[3][0]
  globals.cube[3][0] = temp

def cBot():#rotate bottom clockwise
  #rotate bottom face
  temp = globals.cube[9][3]
  globals.cube[9][3] = globals.cube[11][3]
  globals.cube[11][3] = globals.cube[11][5]
  globals.cube[11][5] = globals.cube[9][5]
  globals.cube[9][5] = temp
  temp = globals.cube[9][4]
  globals.cube[9][4] = globals.cube[10][3]
  globals.cube[10][3] = globals.cube[11][4]
  globals.cube[11][4] = globals.cube[10][5]
  globals.cube[10][5] = temp

  #rotate bottom layer
  temp = globals.cube[8][3]
  globals.cube[8][3] = globals.cube[3][0]
  globals.cube[3][0] = globals.cube[0][5]
  globals.cube[0][5] = globals.cube[5][8]
  globals.cube[5][8] = temp
  temp = globals.cube[8][4]
  globals.cube[8][4] = globals.cube[4][0]
  globals.cube[4][0] = globals.cube[0][4]
  globals.cube[0][4] = globals.cube[4][8]
  globals.cube[4][8] = temp
  temp = globals.cube[8][5]
  globals.cube[8][5] = globals.cube[5][0]
  globals.cube[5][0] = globals.cube[0][3]
  globals.cube[0][3] = globals.cube[3][8]
  globals.cube[3][8] = temp

def ccBot():#rotate bottom counterclockwise
  #rotate bottom face
  temp = globals.cube[9][3]
  globals.cube[9][3] = globals.cube[9][5]
  globals.cube[9][5] = globals.cube[11][5]
  globals.cube[11][5] = globals.cube[11][3]
  globals.cube[11][3] = temp
  temp = globals.cube[9][4]
  globals.cube[9][4] = globals.cube[10][5]
  globals.cube[10][5] = globals.cube[11][4]
  globals.cube[11][4] = globals.cube[10][3]
  globals.cube[10][3] = temp

  #rotate bottom layer
  temp = globals.cube[8][3]
  globals.cube[8][3] = globals.cube[5][8]
  globals.cube[5][8] = globals.cube[0][5]
  globals.cube[0][5] = globals.cube[3][0]
  globals.cube[3][0] = temp
  temp = globals.cube[8][4]
  globals.cube[8][4] = globals.cube[4][8]
  globals.cube[4][8] = globals.cube[0][4]
  globals.cube[0][4] = globals.cube[4][0]
  globals.cube[4][0] = temp
  temp = globals.cube[8][5]
  globals.cube[8][5] = globals.cube[3][8]
  globals.cube[3][8] = globals.cube[0][3]
  globals.cube[0][3] = globals.cube[5][0]
  globals.cube[5][0] = temp
