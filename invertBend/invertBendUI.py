def invertBendUI ():
  smartInvertBendVer = "0.1"
  c1 = [1.0, 1.0, 0.9]
  c2 = [1.0, 0.8, 1.0]

  if (mc.window ( "smartInvertBend", ex=True) == True) :
    mc.deleteUI ("smartInvertBend")
    mc.windowPref ("smartInvertBend", remove = True)
  	
  mc.window ("smartInvertBend", t=("smartInvertBend ver "+smartInvertBendVer), w=230, h=200, s=False)

  mc.columnLayout (adjustableColumn=True, columnAttach=("both", 5), rowSpacing=5, columnWidth=200)
  aboutBtn = mc.button (w=110, align="center", bgc=(c2[0],c2[1],c2[2]), l=("About.."), c=("ibAboutUI") )
  mc.separator()
  createManipBtn = mc.button (w=110, align="center", l=("create Manipulator"), c=("ibManipulator") )
  mc.separator()
  cmds.checkBox( label='duplicate object', align='left' )
  cmds.checkBox( label='create bend deformer', align='left' )
  cmds.checkBox( label='connect mesh', align='left' )
  mc.separator()
  invertBendBtn = mc.button (w=110, align="center",bgc=(c1[0],c1[1],c1[2]), l=("invertBend"), c=("ibApply") )
  mc.showWindow ("smartInvertBend") 
invertBendUI()