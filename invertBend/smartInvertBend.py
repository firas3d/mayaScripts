import maya.cmds as mc
import math

# invertBend UI
def invertBendUI ():
  global locBase
  global locCenter
  global selected
  global smartInvertBendVer
  
  c1 = [1.0, 1.0, 0.9]
  c2 = [1.0, 0.8, 1.0]

  if (mc.window ( "smartInvertBend", ex=True) == True) :
    mc.deleteUI ("smartInvertBend")
    mc.windowPref ("smartInvertBend", remove = True)
  mc.window ("smartInvertBend", t=("smartInvertBend ver "+smartInvertBendVer), w=230, h=200, s=False)

  mc.columnLayout (adjustableColumn=True, columnAttach=("both", 5), rowSpacing=5, columnWidth=200)
  aboutBtn = mc.button (w=110, align="center", bgc=(c2[0],c2[1],c2[2]), l=("About.."), c=("ibAboutUI()") )
  mc.separator()
  createManipBtn = mc.button (w=110, align="center", l=("create Manipulator"), c=("createManipulator()") )
  mc.separator()
  mc.checkBox( enable = False, label='duplicate object', align='left' )
  mc.checkBox( enable = False, label='create bend deformer', align='left' )
  mc.checkBox( enable = False, label='connect mesh', align='left' )
  mc.separator()
  invertBendBtn = mc.button (w=110, align="center",bgc=(c1[0],c1[1],c1[2]), l=("invertBend"), c=("applyIB()") )
  mc.showWindow ("smartInvertBend") 


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

#def create Manipulator      
def createManipulator ( ) :
  
  global locBase
  global locCenter
  global selected
  
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

def applyIB ():
  global locBase
  global locCenter
  global selected
  
  #*check selection type
  
  # store all vtx in one array
  selected = mc.ls (sl=True) # store object selection
  vtxCount = mc.polyEvaluate (selected[0], v=True)
  mc.select (selected[0]+".vtx [0:%d]" % (vtxCount - 1)) 
  vtxArray = mc.ls (sl=True, fl=True)
  
  mc.select (clear=True)
  
  #* checkbox duplicate
  #* if checkbox
  
  #main loop
  for vtx in vtxArray :
    vtxPos = positionOf(vtx)
    cenPos = positionOf(locCenter)
    basePos = positionOf(locBase)
    rad = cenPos[1]-basePos[1]  
    vtxR = distance(cenPos[0],cenPos[1],vtxPos[0],vtxPos[1])
    vtxA = angleIB(cenPos[0],cenPos[1],vtxPos[0],vtxPos[1])
    
    if (vtxPos[0]>basePos[0]) :  
      flatX = rad * math.pi * vtxA
    elif ((vtxPos[0]<basePos[0]) & (vtxPos[1]>cenPos[1])):
      flatX = rad * math.pi * vtxA * (-1)
      print vtxA
    else :
      flatX = rad * math.pi * vtxA
    
    flatY = basePos[1]+ (rad - vtxR)

    place (vtx,flatX,flatY,vtxPos[2])
  
  #delete manipulator
  mc.select (locBase, locCenter)
  mc.delete()
 
  #* checkbox bend deformer
  
  #* checkbox connect mesh
#call invertBend
def invertBend() :
  global locBase
  global locCenter
  global selected
  global smartInvertBendVer
  
  smartInvertBendVer = "0.1"
  
  invertBendUI()
######## end of invertBend
invertBend()