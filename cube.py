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
