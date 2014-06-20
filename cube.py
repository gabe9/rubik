g = 1
r = 2
b = 3
o = 4
y = 5
w = 6
colors = {1:'g', 2:'r', 3:'b', 4:'o', 5:'y', 6:'w'}

e = 0

aa = g
ab = g
ac = g
ad = g
ae = g
af = g
ag = g
ah = g
ai = g

ba = r
bb = r
bc = r
bd = r
be = r
bf = r
bg = r
bh = r
bi = r

ca = w
cb = w
cc = w
cd = w
ce = w
cf = w
cg = w
ch = w
ci = w

da = o
db = o
dc = o
dd = o
de = o
df = o
dg = o
dh = o
di = o

ea = y
eb = y
ec = y
ed = y
ee = y
ef = y
eg = y
eh = y
ei = y

fa = b 
fb = b
fc = b
fd = b
fe = b
ff = b
fg = b
fh = b
fi = b

cube = [[e,e,e,da,db,dc,e,e,e],
         [e,e,e,dd,de,df,e,e,e],
         [e,e,e,dg,dh,di,e,e,e],
      [ea,eb,ec,aa,ab,ac,ca,cb,cc],
      [ed,ee,ef,ad,ae,af,cd,ce,cf],
      [eg,eh,ei,ag,ah,ai,cg,ch,ci],
         [e,e,e,ba,bb,bc,e,e,e],
         [e,e,e,bd,be,bf,e,e,e],
         [e,e,e,bg,bh,bi,e,e,e],
         [e,e,e,fa,fb,fc,e,e,e],
         [e,e,e,fd,fe,ff,e,e,e],
         [e,e,e,fg,fh,fi,e,e,e]]


def cTop():#assume cube is front
  #cube
  #rotate front face
  temp = cube[3][3] 
  cube[3][3] = cube[5][3]
  cube[5][3] = cube[5][5]
  cube[5][5] = cube[3][5]
  cube[3][5] = temp
  temp = cube[3][4]
  cube[3][4] = cube[4][3]
  cube[4][3] = cube[5][4]
  cube[5][4] = cube[4][5]
  cube[4][5] = temp
  #rotate top
  temp = cube[2][3]
  cube[2][3] = cube[5][2]
  cube[5][2] = cube[6][5]
  cube[6][5] = cube[3][6]
  cube[3][6] = temp
  temp = cube[2][4]
  cube[2][4] = cube[4][2]
  cube[4][2] = cube[6][4]
  cube[6][4] = cube[4][6]
  cube[4][6] = temp
  temp = cube[2][5]
  cube[2][5] = cube[3][2]
  cube[3][2] = cube[6][3]
  cube[6][3] = cube[5][6]
  cube[5][6] = temp

def ccTop():
  temp = cube[3][3]
  cube[3][3] = cube[3][5]
  cube[3][5] = cube[5][5]
  cube[5][5] = cube[5][3]
  cube[5][3] = temp
  temp = cube[3][4]
  cube[3][4] = cube[4][5]
  cube[4][5] = cube[5][4]
  cube[5][4] = cube[4][3]
  cube[4][3] = temp

  temp = cube[2][3]
  cube[2][3] = cube[3][6]
  cube[3][6] = cube[6][5]
  cube[6][5] = cube[5][2]
  cube[5][2] = temp
  temp = cube[2][4]
  cube[2][4] = cube[4][6]
  cube[4][6] = cube[6][4]
  cube[6][4] = cube[4][2]
  cube[4][2] = temp
  temp = cube[2][5]
  cube[2][5] = cube[5][6]
  cube[5][6] = cube[6][3]
  cube[6][3] = cube[3][2]
  cube[3][2] = temp

def cFront():
  temp = cube[6][3]
  cube[6][3] = cube[8][3]
  cube[8][3] = cube[8][5]
  cube[8][5] = cube[6][5]
  cube[6][5] = temp
  temp = cube[6][4]
  cube[6][4] = cube[7][3]
  cube[7][3] = cube[8][4]
  cube[8][4] = cube[7][5]
  cube[7][5] = temp

  temp = cube[5][3]
  cube[5][3] = cube[5][0]
  cube[5][0] = cube[9][5]
  cube[9][5] = cube[5][6]
  cube[5][6] = temp
  temp = cube[5][4]
  cube[5][4] = cube[5][1]
  cube[5][1] = cube[9][4]
  cube[9][4] = cube[5][7]
  cube[5][7] = temp
  temp = cube[5][5]
  cube[5][5] = cube[5][2]
  cube[5][2] = cube[9][3]
  cube[9][3] = cube[5][8]
  cube[5][8] = temp

def ccFront():
  temp = cube[6][3]
  cube[6][3] = cube[6][5]
  cube[6][5] = cube[8][5]
  cube[8][5] = cube[8][3]
  cube[8][3] = temp
  temp = cube[6][4]
  cube[6][4] = cube[7][5]
  cube[7][5] = cube[8][4]
  cube[8][4] = cube[7][3]
  cube[7][3] = temp

  temp = cube[5][3]
  cube[5][3] = cube[5][6]
  cube[5][6] = cube[9][5]
  cube[9][5] = cube[5][0]
  cube[5][0] = temp
  temp = cube[5][4]
  cube[5][4] = cube[5][7]
  cube[5][7] = cube[9][4]
  cube[9][4] = cube[5][1]
  cube[5][1] = temp
  temp = cube[5][5]
  cube[5][5] = cube[5][8]
  cube[5][8] = cube[9][3]
  cube[9][3] = cube[5][2]
  cube[5][2] = temp

def cRight():
  temp = cube[3][6]
  cube[3][6] = cube[5][6]
  cube[5][6] = cube[5][8]
  cube[5][8] = cube[3][8]
  cube[3][8] = temp
  temp = cube[3][7]
  cube[3][7] = cube[4][6]
  cube[4][6] = cube[5][7]
  cube[5][7] = cube[4][8]
  cube[4][8] = temp

  temp = cube[2][5]
  cube[2][5] = cube[5][5]
  cube[5][5] = cube[8][5]
  cube[8][5] = cube[11][5]
  cube[11][5] = temp
  temp = cube[1][5]
  cube[1][5] = cube[4][5]
  cube[4][5] = cube[7][5]
  cube[7][5] = cube[10][5]
  cube[10][5] = temp
  temp = cube[0][5]
  cube[0][5] = cube[3][5]
  cube[3][5] = cube[6][5]
  cube[6][5] = cube[9][5]
  cube[9][5] = temp

def ccRight():
  temp = cube[3][6]
  cube[3][6] = cube[3][8]
  cube[3][8] = cube[5][8]
  cube[5][8] = cube[5][6]
  cube[5][6] = temp
  temp = cube[3][7]
  cube[3][7] = cube[4][8]
  cube[4][8] = cube[5][7]
  cube[5][7] = cube[4][6]
  cube[4][6] = temp

  temp = cube[2][5]
  cube[2][5] = cube[11][5]
  cube[11][5] = cube[8][5]
  cube[8][5] = cube[5][5]
  cube[5][5] = temp
  temp = cube[1][5]
  cube[1][5] = cube[10][5]
  cube[10][5] = cube[7][5]
  cube[7][5] = cube[4][5]
  cube[4][5] = temp
  temp = cube[0][5]
  cube[0][5] = cube[9][5]
  cube[9][5] =cube[6][5]
  cube[6][5] = cube[3][5]
  cube[3][5] = temp

def cLeft():
  temp = cube[3][0]
  cube[3][0] = cube[5][0]
  cube[5][0] = cube[5][2]
  cube[5][2] = cube[3][2]
  cube[3][2] = temp
  temp = cube[3][1]
  cube[3][1] = cube[4][0]
  cube[4][0] = cube[5][1]
  cube[5][1] = cube[4][2]
  cube[4][2] = temp

  temp = cube[0][3]
  cube[0][3] = cube[9][3]
  cube[9][3] = cube[6][3]
  cube[6][3] = cube[3][3]
  cube[3][3] = temp
  temp = cube[1][3]
  cube[1][3] = cube[10][3]
  cube[10][3] = cube[7][3]
  cube[7][3] = cube[4][3]
  cube[4][3] = temp
  temp = cube[2][3]
  cube[2][3] = cube[11][3]
  cube[11][3] = cube[8][3]
  cube[8][3] = cube[5][3]
  cube[5][3] = temp

def ccLeft():
  temp = cube[3][0]
  cube[3][0] = cube[3][2]
  cube[3][2] = cube[5][2]
  cube[5][2] = cube[5][0]
  cube[5][0] = temp
  temp = cube[3][1]
  cube[3][1] = cube[4][2]
  cube[4][2] = cube[5][1]
  cube[5][1] = cube[4][0]
  cube[4][0] = temp

  temp = cube[0][3]
  cube[0][3] = cube[3][3]
  cube[3][3] = cube[6][3]
  cube[6][3] = cube[9][3]
  cube[9][3] = temp
  temp = cube[1][3]
  cube[1][3] = cube[4][3]
  cube[4][3] = cube[7][3]
  cube[7][3] = cube[10][3]
  cube[10][3] = temp
  temp = cube[2][3]
  cube[2][3] = cube[5][3]
  cube[5][3] = cube[8][3]
  cube[8][3] = cube[11][3]
  cube[11][3] = temp

def cBack():
  temp = cube[0][3]
  cube[0][3] = cube[2][3]
  cube[2][3] = cube[2][5]
  cube[2][5] = cube[0][5]
  cube[0][5] = temp
  temp = cube[0][4]
  cube[0][4] = cube[1][3]
  cube[1][3] = cube[2][4]
  cube[2][4] = cube[1][5]
  cube[1][5] = temp

  temp = cube[11][3]
  cube[11][3] = cube[3][2]
  cube[3][2] = cube[3][5]
  cube[3][5] = cube[3][8]
  cube[3][8] = temp
  temp = cube[11][4]
  cube[11][4] = cube[3][1]
  cube[3][1] = cube[3][4]
  cube[3][4] = cube[3][7]
  cube[3][7] = temp
  temp = cube[11][5]
  cube[11][5] = cube[3][0]
  cube[3][0] = cube[3][3]
  cube[3][3] = cube[3][6]
  cube[3][6] = temp

def ccBack():
  temp = cube[0][3]
  cube[0][3] = cube[0][5]
  cube[0][5] = cube[2][5]
  cube[2][5] = cube[2][3]
  cube[2][3] = temp
  temp = cube[0][4]
  cube[0][4] = cube[1][5]
  cube[1][5] = cube[2][4]
  cube[2][4] = cube[1][3]
  cube[1][3] = temp

  temp = cube[11][3]
  cube[11][3] = cube[3][8]
  cube[3][8] = cube[3][5]
  cube[3][5] = cube[3][2]
  cube[3][2] = temp
  temp = cube[11][4]
  cube[11][4] = cube[3][7]
  cube[3][7] = cube[3][4]
  cube[3][4] = cube[3][1]
  cube[3][1] = temp
  temp = cube[11][5]
  cube[11][5] = cube[3][6]
  cube[3][6] = cube[3][3]
  cube[3][3] = cube[3][0]
  cube[3][0] = temp

def cBot():
  temp = cube[9][3]
  cube[9][3] = cube[11][3]
  cube[11][3] = cube[11][5]
  cube[11][5] = cube[9][5]
  cube[9][5] = temp
  temp = cube[9][4]
  cube[9][4] = cube[10][3]
  cube[10][3] = cube[11][4]
  cube[11][4] = cube[10][5]
  cube[10][5] = temp

  temp = cube[8][3]
  cube[8][3] = cube[3][0]
  cube[3][0] = cube[0][5]
  cube[0][5] = cube[5][8]
  cube[5][8] = temp
  temp = cube[8][4]
  cube[8][4] = cube[4][0]
  cube[4][0] = cube[0][4]
  cube[0][4] = cube[4][8]
  cube[4][8] = temp
  temp = cube[8][5]
  cube[8][5] = cube[5][0]
  cube[5][0] = cube[0][3]
  cube[0][3] = cube[3][8]
  cube[3][8] = temp

def ccBot():
  temp = cube[9][3]
  cube[9][3] = cube[9][5]
  cube[9][5] = cube[11][5]
  cube[11][5] = cube[11][3]
  cube[11][3] = temp
  temp = cube[9][4]
  cube[9][4] = cube[10][5]
  cube[10][5] = cube[11][4]
  cube[11][4] = cube[10][3]
  cube[10][3] = temp

  temp = cube[8][3]
  cube[8][3] = cube[5][8]
  cube[5][8] = cube[0][5]
  cube[0][5] = cube[3][0]
  cube[3][0] = temp
  temp = cube[8][4]
  cube[8][4] = cube[4][8]
  cube[4][8] = cube[0][4]
  cube[0][4] = cube[4][0]
  cube[4][0] = temp
  temp = cube[8][5]
  cube[8][5] = cube[3][8]
  cube[3][8] = cube[0][3]
  cube[0][3] = cube[5][0]
  cube[5][0] = temp

def testAlgo():
  ccRight()
  ccBot()
  cRight()
  cBot()

def printFront():
  print colors[cube[6][3]], colors[cube[6][4]], colors[cube[6][5]]
  print colors[cube[7][3]], colors[cube[7][4]], colors[cube[7][5]]
  print colors[cube[8][3]], colors[cube[8][4]], colors[cube[8][5]]

def printTop():
  print colors[cube[3][3]], colors[cube[3][4]], colors[cube[3][5]]
  print colors[cube[4][3]], colors[cube[4][4]], colors[cube[4][5]]
  print colors[cube[5][3]], colors[cube[5][4]], colors[cube[5][5]]

def printBot():
  print colors[cube[9][3]], colors[cube[9][4]], colors[cube[9][5]]
  print colors[cube[10][3]], colors[cube[10][4]], colors[cube[10][5]]
  print colors[cube[11][3]], colors[cube[11][4]], colors[cube[11][5]]

def printBack():
  print colors[cube[0][3]], colors[cube[0][4]], colors[cube[0][5]]
  print colors[cube[1][3]], colors[cube[1][4]], colors[cube[1][5]]
  print colors[cube[2][3]], colors[cube[2][4]], colors[cube[2][5]]

def printLeft():
  print colors[cube[3][0]], colors[cube[3][1]], colors[cube[3][2]]
  print colors[cube[4][0]], colors[cube[4][1]], colors[cube[4][2]]
  print colors[cube[5][0]], colors[cube[5][1]], colors[cube[5][2]]

def printRight():
  print colors[cube[3][6]], colors[cube[3][7]], colors[cube[3][8]]
  print colors[cube[4][6]], colors[cube[4][7]], colors[cube[4][8]]
  print colors[cube[5][6]], colors[cube[5][7]], colors[cube[5][8]]

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
  cRight()
  print "cRight"
  printCube()
  cBot()
  print "cBot"
  printCube()
  cRight()
  print "cRight"
  printCube()
  ccLeft()
  print "ccLeft"
  printCube()
  cTop()
  print "cTop"
  printCube()
  ccBot()
  print "ccBot"
  printCube()
  cFront()
  print "cFront"
  printCube()
  cLeft()
  print "cLeft"
  printCube()
  ccRight()
  print "ccRight"
  printCube()
  cTop()
  print "cTop"
  printCube()
  for line in cube:
    print line
  cBot()
  print "cBot"
  printCube()
  cBack()
  print "cBack"
  printCube()
  ccBot()
  print "ccBot"
  printCube()
  ccBack()
  print "ccBack"
  printCube()
  ccBack()
  print "ccBack"
  printCube()
  cRight()
  print "cRight"
  printCube()

