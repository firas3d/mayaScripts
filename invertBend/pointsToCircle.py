import maya.cmds as mc
import math

#find circle radios from 3 points a,b and c
def center (x1,y1,x2,y2,x3,y3) :
  cen = [0,0]
  ma = (y2-y1)/(x2-x1)
  mb = (y3-y2)/(x3-x2)

  x = ((ma * mb * (y1-y3)) + (mb*(x1+x2)) - (ma*(x2+x3))) / (2*(mb-ma))
  y = (1/ma)*( x - ((x1+x2)/2) ) + ((y1+y2)/2)

  cen[0] = x
  cen[1] = y
  return cen

x1=1
y1=2
x2=2
y2=1
x3=1
y3=0

c = center (x1,y1,x2,y2,x3,y3)