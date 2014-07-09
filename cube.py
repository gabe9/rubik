import moves

g = 1#green
r = 2#red
b = 3#blue
o = 4#orange
y = 5#yellow
w = 6#white
e = 0#empty spot

possibleMoves = ["u","u'","f","f'","l","l'","r","r'","d","d'","b","b'"]

#enter color values here depending on position. See layout.txt for more information on position.
#a is top, b is front, c is right, d is back, e is left and f is bottom.
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

#cube map
map = [[e,e,e,da,db,dc,e,e,e],
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

def move(moveArray):
  moves.move(moveArray)

def getEdges():
  #returns the edges. First the edges on the top face, then the edges in the middle slice of the cube, then finally the edges on the bottom. Going clockwise starting with the edge on the back of the cube.
  #the order of these edges will also represent the number associated with that edge.
  # [(ab,dh),(af,cd),(ah,bb),(ad,ef),(eb,dd),(df,db),(ch,bf),(bd,eh),(fh,db),(ff,cf),(fb,bh),(fd,ed)]
  return [(map[3][4],map[2][4]),(map[4][5],map[4][6]),(map[5][4],map[6][4]),(map[4][3],map[4][2]),(map[3][1],map[1][3]),(map[1][5],map[3][7]),(map[5][7],map[7][5]),(map[7][3],map[5][1]),(map[11][4],map[0][4]),(map[10][5],map[4][8]),(map[9][4],map[8][4]),(map[10][3],map[4][0])]

def getCorners():
  #      [(aa,ec,dg),(ac,di,ca),(ai,cg,bc),(ag,ba,ei),(fg,da,ea),(fi,cc,dc),(fc,bi,ci), (fa,eg,bg)]
  return [(map[3][3],map[3][2],map[2][3]),(map[3][5],map[2][5],map[3][6]),(map[5][5],map[5][6],map[6][5]),(map[5][3],map[6][3],map[5][2]),(map[11][3],map[0][3],map[3][0]),(map[11][5],map[3][8],map[0][5]),(map[9][5],map[8][5],map[5][8]), (map[9][3],map[5][0],map[8][3])]

