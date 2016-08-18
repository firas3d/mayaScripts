import maya.cmds as mc
import math

#find angle by givin line(2 points) and vertrical line, first point should be the center
def angleIB(x0, y0, x1, y1):
    from math import degrees, atan2
    a = (degrees( atan2(y1-y0, x1-x0) ) + 90) / 180
    return a

#find the 2D distance    
def distance(x0, y0, x1, y1):
    from math import sqrt, pow
    return sqrt(pow(x1-x0, 2) + pow(y1-y0, 2))

#find position of input object or component
def positionOf(obj):
  return mc.xform(obj, q=True, ws=True, t=True)  

#position input object or component to x,y,z
def place(obj, x, y, z) :
  mc.xform(obj, ws=True, t=(x, y, z))
  
# invertBend body function    
def invertBend ( ) :
  # store object selection
  selected = mc.ls (sl=True)
  
  # create manipulator
  manCircle = mc.circle (ch=True,o=True,sw=-180, name="manCircleIB")
  mc.move (0,1,0,r=False)
  locBase = mc.spaceLocator (p=(0,0,0), n="manBaseIB")
  locCenter = mc.spaceLocator (p=(0,0,0), n="manCenterIB",r=True)
  mc.move (0,1,0,r=False)
  distanceNode = mc.createNode ("distanceBetween", n="raduisIB")
  mc.connectAttr (locBase[0]+".translate", distanceNode+".point1")
  mc.connectAttr (locCenter[0]+".translate", distanceNode+".point2")
  mc.connectAttr (distanceNode+".distance", manCircle[1]+".radius")
  mc.connectAttr (distanceNode+".distance", manCircle[0]+".ty")
  mc.setAttr (manCircle[0]+".sp", 0, -1, 0)
  mc.setAttr (manCircle[0]+".rp", 0, -1, 0)
  mc.connectAttr (locBase[0]+".translateX", locCenter[0]+".translateX", f=True)
  mc.connectAttr (locBase[0]+".translateZ", locCenter[0]+".translateZ", f=True)
  mc.parent (manCircle[0], locBase[0])
  mc.select (clear = True)
  
  # store all vtx in one array
  vtxCount = mc.polyEvaluate (selected[0], v=True)
  mc.select (selected[0]+".vtx [0:%d]" % (vtxCount - 1)) 
  vtxArray = mc.ls (sl=True, fl=True)
  
  mc.select (clear=True)
  #confirm button
  result = mc.confirmDialog(
    title="invertBend",
    message="ready to invertBend?",
	button=['OK', 'Cancel'],
	defaultButton='OK',
	cancelButton='Cancel',
	dismissString='Cancel')
  if result == "OK" :
    for vtx in vtxArray :
      vtxPos = positionOf(vtx)
      cenPos = positionOf(locCenter)
      basePos = positionOf(locBase)
      rad = cenPos[1]-basePos[1]  
      vtxR = distance(cenPos[0],cenPos[1],vtxPos[0],vtxPos[1])
      vtxA = angleIB(cenPos[0],cenPos[1],vtxPos[0],vtxPos[1])
      
      flatX = rad * math.pi * vtxA
      flatY = basePos[1]+ ( cenPos[1]-vtxR )

      place (vtx,flatX,flatY,vtxPos[2])
    
#call invertBend
invertBend()