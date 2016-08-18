import maya.cmds as mc
import string
sel = mc.ls (sl = True, fl = True)
print sel[0]
dotPosition = string.find(sel[0],".")
print string.split(sel[0],".")