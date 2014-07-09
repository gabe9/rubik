import cube

def cTop():#rotate top clockwise
  #rotate top face
  temp = cube.map[3][3] 
  cube.map[3][3] = cube.map[5][3]
  cube.map[5][3] = cube.map[5][5]
  cube.map[5][5] = cube.map[3][5]
  cube.map[3][5] = temp
  temp = cube.map[3][4]
  cube.map[3][4] = cube.map[4][3]
  cube.map[4][3] = cube.map[5][4]
  cube.map[5][4] = cube.map[4][5]
  cube.map[4][5] = temp

  #rotate top layer
  temp = cube.map[2][3]
  cube.map[2][3] = cube.map[5][2]
  cube.map[5][2] = cube.map[6][5]
  cube.map[6][5] = cube.map[3][6]
  cube.map[3][6] = temp
  temp = cube.map[2][4]
  cube.map[2][4] = cube.map[4][2]
  cube.map[4][2] = cube.map[6][4]
  cube.map[6][4] = cube.map[4][6]
  cube.map[4][6] = temp
  temp = cube.map[2][5]
  cube.map[2][5] = cube.map[3][2]
  cube.map[3][2] = cube.map[6][3]
  cube.map[6][3] = cube.map[5][6]
  cube.map[5][6] = temp

def ccTop():#rotate top counterclockwise
  #rotate top face
  temp = cube.map[3][3]
  cube.map[3][3] = cube.map[3][5]
  cube.map[3][5] = cube.map[5][5]
  cube.map[5][5] = cube.map[5][3]
  cube.map[5][3] = temp
  temp = cube.map[3][4]
  cube.map[3][4] = cube.map[4][5]
  cube.map[4][5] = cube.map[5][4]
  cube.map[5][4] = cube.map[4][3]
  cube.map[4][3] = temp

  #rotate top layer
  temp = cube.map[2][3]
  cube.map[2][3] = cube.map[3][6]
  cube.map[3][6] = cube.map[6][5]
  cube.map[6][5] = cube.map[5][2]
  cube.map[5][2] = temp
  temp = cube.map[2][4]
  cube.map[2][4] = cube.map[4][6]
  cube.map[4][6] = cube.map[6][4]
  cube.map[6][4] = cube.map[4][2]
  cube.map[4][2] = temp
  temp = cube.map[2][5]
  cube.map[2][5] = cube.map[5][6]
  cube.map[5][6] = cube.map[6][3]
  cube.map[6][3] = cube.map[3][2]
  cube.map[3][2] = temp


def cFront():#rotate front colockwise
  #rotate front face
  temp = cube.map[6][3]
  cube.map[6][3] = cube.map[8][3]
  cube.map[8][3] = cube.map[8][5]
  cube.map[8][5] = cube.map[6][5]
  cube.map[6][5] = temp
  temp = cube.map[6][4]
  cube.map[6][4] = cube.map[7][3]
  cube.map[7][3] = cube.map[8][4]
  cube.map[8][4] = cube.map[7][5]
  cube.map[7][5] = temp

  #rotate front layer
  temp = cube.map[5][3]
  cube.map[5][3] = cube.map[5][0]
  cube.map[5][0] = cube.map[9][5]
  cube.map[9][5] = cube.map[5][6]
  cube.map[5][6] = temp
  temp = cube.map[5][4]
  cube.map[5][4] = cube.map[5][1]
  cube.map[5][1] = cube.map[9][4]
  cube.map[9][4] = cube.map[5][7]
  cube.map[5][7] = temp
  temp = cube.map[5][5]
  cube.map[5][5] = cube.map[5][2]
  cube.map[5][2] = cube.map[9][3]
  cube.map[9][3] = cube.map[5][8]
  cube.map[5][8] = temp

def ccFront():#rotate front counterclockwise
  #rotate front face
  temp = cube.map[6][3]
  cube.map[6][3] = cube.map[6][5]
  cube.map[6][5] = cube.map[8][5]
  cube.map[8][5] = cube.map[8][3]
  cube.map[8][3] = temp
  temp = cube.map[6][4]
  cube.map[6][4] = cube.map[7][5]
  cube.map[7][5] = cube.map[8][4]
  cube.map[8][4] = cube.map[7][3]
  cube.map[7][3] = temp

  #rotate front layer
  temp = cube.map[5][3]
  cube.map[5][3] = cube.map[5][6]
  cube.map[5][6] = cube.map[9][5]
  cube.map[9][5] = cube.map[5][0]
  cube.map[5][0] = temp
  temp = cube.map[5][4]
  cube.map[5][4] = cube.map[5][7]
  cube.map[5][7] = cube.map[9][4]
  cube.map[9][4] = cube.map[5][1]
  cube.map[5][1] = temp
  temp = cube.map[5][5]
  cube.map[5][5] = cube.map[5][8]
  cube.map[5][8] = cube.map[9][3]
  cube.map[9][3] = cube.map[5][2]
  cube.map[5][2] = temp

def cRight():#rotate right clockwise
  #rotate right face
  temp = cube.map[3][6]
  cube.map[3][6] = cube.map[5][6]
  cube.map[5][6] = cube.map[5][8]
  cube.map[5][8] = cube.map[3][8]
  cube.map[3][8] = temp
  temp = cube.map[3][7]
  cube.map[3][7] = cube.map[4][6]
  cube.map[4][6] = cube.map[5][7]
  cube.map[5][7] = cube.map[4][8]
  cube.map[4][8] = temp

  #rotate right layer
  temp = cube.map[2][5]
  cube.map[2][5] = cube.map[5][5]
  cube.map[5][5] = cube.map[8][5]
  cube.map[8][5] = cube.map[11][5]
  cube.map[11][5] = temp
  temp = cube.map[1][5]
  cube.map[1][5] = cube.map[4][5]
  cube.map[4][5] = cube.map[7][5]
  cube.map[7][5] = cube.map[10][5]
  cube.map[10][5] = temp
  temp = cube.map[0][5]
  cube.map[0][5] = cube.map[3][5]
  cube.map[3][5] = cube.map[6][5]
  cube.map[6][5] = cube.map[9][5]
  cube.map[9][5] = temp

def ccRight():#rotate right counterclockwise
  #rotate right face
  temp = cube.map[3][6]
  cube.map[3][6] = cube.map[3][8]
  cube.map[3][8] = cube.map[5][8]
  cube.map[5][8] = cube.map[5][6]
  cube.map[5][6] = temp
  temp = cube.map[3][7]
  cube.map[3][7] = cube.map[4][8]
  cube.map[4][8] = cube.map[5][7]
  cube.map[5][7] = cube.map[4][6]
  cube.map[4][6] = temp

  #rotate right layer
  temp = cube.map[2][5]
  cube.map[2][5] = cube.map[11][5]
  cube.map[11][5] = cube.map[8][5]
  cube.map[8][5] = cube.map[5][5]
  cube.map[5][5] = temp
  temp = cube.map[1][5]
  cube.map[1][5] = cube.map[10][5]
  cube.map[10][5] = cube.map[7][5]
  cube.map[7][5] = cube.map[4][5]
  cube.map[4][5] = temp
  temp = cube.map[0][5]
  cube.map[0][5] = cube.map[9][5]
  cube.map[9][5] =cube.map[6][5]
  cube.map[6][5] = cube.map[3][5]
  cube.map[3][5] = temp

def cLeft():#rotate left clockwise
  #rotate left face
  temp = cube.map[3][0]
  cube.map[3][0] = cube.map[5][0]
  cube.map[5][0] = cube.map[5][2]
  cube.map[5][2] = cube.map[3][2]
  cube.map[3][2] = temp
  temp = cube.map[3][1]
  cube.map[3][1] = cube.map[4][0]
  cube.map[4][0] = cube.map[5][1]
  cube.map[5][1] = cube.map[4][2]
  cube.map[4][2] = temp

  #rotate left layer
  temp = cube.map[0][3]
  cube.map[0][3] = cube.map[9][3]
  cube.map[9][3] = cube.map[6][3]
  cube.map[6][3] = cube.map[3][3]
  cube.map[3][3] = temp
  temp = cube.map[1][3]
  cube.map[1][3] = cube.map[10][3]
  cube.map[10][3] = cube.map[7][3]
  cube.map[7][3] = cube.map[4][3]
  cube.map[4][3] = temp
  temp = cube.map[2][3]
  cube.map[2][3] = cube.map[11][3]
  cube.map[11][3] = cube.map[8][3]
  cube.map[8][3] = cube.map[5][3]
  cube.map[5][3] = temp

def ccLeft():#rotate left counterclockwise
  #rotate left face
  temp = cube.map[3][0]
  cube.map[3][0] = cube.map[3][2]
  cube.map[3][2] = cube.map[5][2]
  cube.map[5][2] = cube.map[5][0]
  cube.map[5][0] = temp
  temp = cube.map[3][1]
  cube.map[3][1] = cube.map[4][2]
  cube.map[4][2] = cube.map[5][1]
  cube.map[5][1] = cube.map[4][0]
  cube.map[4][0] = temp

  #rotate left layer
  temp = cube.map[0][3]
  cube.map[0][3] = cube.map[3][3]
  cube.map[3][3] = cube.map[6][3]
  cube.map[6][3] = cube.map[9][3]
  cube.map[9][3] = temp
  temp = cube.map[1][3]
  cube.map[1][3] = cube.map[4][3]
  cube.map[4][3] = cube.map[7][3]
  cube.map[7][3] = cube.map[10][3]
  cube.map[10][3] = temp
  temp = cube.map[2][3]
  cube.map[2][3] = cube.map[5][3]
  cube.map[5][3] = cube.map[8][3]
  cube.map[8][3] = cube.map[11][3]
  cube.map[11][3] = temp

def cBack():#rotae back clockwise
  #rotate left face
  temp = cube.map[0][3]
  cube.map[0][3] = cube.map[2][3]
  cube.map[2][3] = cube.map[2][5]
  cube.map[2][5] = cube.map[0][5]
  cube.map[0][5] = temp
  temp = cube.map[0][4]
  cube.map[0][4] = cube.map[1][3]
  cube.map[1][3] = cube.map[2][4]
  cube.map[2][4] = cube.map[1][5]
  cube.map[1][5] = temp

  #rotate left layer
  temp = cube.map[11][3]
  cube.map[11][3] = cube.map[3][2]
  cube.map[3][2] = cube.map[3][5]
  cube.map[3][5] = cube.map[3][8]
  cube.map[3][8] = temp
  temp = cube.map[11][4]
  cube.map[11][4] = cube.map[3][1]
  cube.map[3][1] = cube.map[3][4]
  cube.map[3][4] = cube.map[3][7]
  cube.map[3][7] = temp
  temp = cube.map[11][5]
  cube.map[11][5] = cube.map[3][0]
  cube.map[3][0] = cube.map[3][3]
  cube.map[3][3] = cube.map[3][6]
  cube.map[3][6] = temp

def ccBack():#rotate back counterclockwise
  #rotate back face
  temp = cube.map[0][3]
  cube.map[0][3] = cube.map[0][5]
  cube.map[0][5] = cube.map[2][5]
  cube.map[2][5] = cube.map[2][3]
  cube.map[2][3] = temp
  temp = cube.map[0][4]
  cube.map[0][4] = cube.map[1][5]
  cube.map[1][5] = cube.map[2][4]
  cube.map[2][4] = cube.map[1][3]
  cube.map[1][3] = temp

  #rotate back layer
  temp = cube.map[11][3]
  cube.map[11][3] = cube.map[3][8]
  cube.map[3][8] = cube.map[3][5]
  cube.map[3][5] = cube.map[3][2]
  cube.map[3][2] = temp
  temp = cube.map[11][4]
  cube.map[11][4] = cube.map[3][7]
  cube.map[3][7] = cube.map[3][4]
  cube.map[3][4] = cube.map[3][1]
  cube.map[3][1] = temp
  temp = cube.map[11][5]
  cube.map[11][5] = cube.map[3][6]
  cube.map[3][6] = cube.map[3][3]
  cube.map[3][3] = cube.map[3][0]
  cube.map[3][0] = temp

def cBot():#rotate bottom clockwise
  #rotate bottom face
  temp = cube.map[9][3]
  cube.map[9][3] = cube.map[11][3]
  cube.map[11][3] = cube.map[11][5]
  cube.map[11][5] = cube.map[9][5]
  cube.map[9][5] = temp
  temp = cube.map[9][4]
  cube.map[9][4] = cube.map[10][3]
  cube.map[10][3] = cube.map[11][4]
  cube.map[11][4] = cube.map[10][5]
  cube.map[10][5] = temp

  #rotate bottom layer
  temp = cube.map[8][3]
  cube.map[8][3] = cube.map[3][0]
  cube.map[3][0] = cube.map[0][5]
  cube.map[0][5] = cube.map[5][8]
  cube.map[5][8] = temp
  temp = cube.map[8][4]
  cube.map[8][4] = cube.map[4][0]
  cube.map[4][0] = cube.map[0][4]
  cube.map[0][4] = cube.map[4][8]
  cube.map[4][8] = temp
  temp = cube.map[8][5]
  cube.map[8][5] = cube.map[5][0]
  cube.map[5][0] = cube.map[0][3]
  cube.map[0][3] = cube.map[3][8]
  cube.map[3][8] = temp

def ccBot():#rotate bottom counterclockwise
  #rotate bottom face
  temp = cube.map[9][3]
  cube.map[9][3] = cube.map[9][5]
  cube.map[9][5] = cube.map[11][5]
  cube.map[11][5] = cube.map[11][3]
  cube.map[11][3] = temp
  temp = cube.map[9][4]
  cube.map[9][4] = cube.map[10][5]
  cube.map[10][5] = cube.map[11][4]
  cube.map[11][4] = cube.map[10][3]
  cube.map[10][3] = temp

  #rotate bottom layer
  temp = cube.map[8][3]
  cube.map[8][3] = cube.map[5][8]
  cube.map[5][8] = cube.map[0][5]
  cube.map[0][5] = cube.map[3][0]
  cube.map[3][0] = temp
  temp = cube.map[8][4]
  cube.map[8][4] = cube.map[4][8]
  cube.map[4][8] = cube.map[0][4]
  cube.map[0][4] = cube.map[4][0]
  cube.map[4][0] = temp
  temp = cube.map[8][5]
  cube.map[8][5] = cube.map[3][8]
  cube.map[3][8] = cube.map[0][3]
  cube.map[0][3] = cube.map[5][0]
  cube.map[5][0] = temp

def move(moveArray):
  for move in moveArray:
    if move == "u":
      cTop()
    elif move == "u'":
      ccTop()
    elif move == "f":
      cFront()
    elif move == "f'":
      ccFront()
    elif move == "d":
      cBot()
    elif move == "d'":
      ccBot()
    elif move == "b":
      cBack()
    elif move == "b'":
      ccBack()
    elif move == "l":
      cLeft()
    elif move == "l'":
      ccLeft()
    elif move == "r":
      cRight()
    elif move == "r'":
      ccRight()
    else:
      return "Move not valid."
