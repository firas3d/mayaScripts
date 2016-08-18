//Maya ASCII 2008 scene
//Name: arrow.ma
//Last modified: Sun, Jul 27, 2008 09:39:21 AM
//Codeset: 1252
requires maya "2008";
requires "maxwell" "1.6.6";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya Unlimited 2008";
fileInfo "version" "2008 Extension 2";
fileInfo "cutIdentifier" "200802250025-718075";
fileInfo "osv" "Microsoft Windows Vista Service Pack 1 (Build 6001)\n";
createNode transform -n "curve1";
	setAttr ".t" -type "double3" 0 -0.70068845186285078 0 ;
	setAttr ".r" -type "double3" 0 0 90 ;
	setAttr ".s" -type "double3" 1 8.7629630279619466 1 ;
	setAttr ".rp" -type "double3" 0 0.70068845186285078 0 ;
	setAttr ".sp" -type "double3" 0 0.70068845186285078 0 ;
createNode nurbsCurve -n "curveShape1" -p "curve1";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 12 2 no 3
		13 0 1 2 3 4 5 6 7 8 9 10 11 12
		13
		0 0.7006884518633093 -0.40345170000000002
		0 -0.32075960998488623 -0.40345170000000002
		0 -0.32075960998488623 -0.6724194
		0 -0.40345170000000002 0
		0 -0.32075960998488623 0.6724194
		0 -0.32075960998488623 0.40345170000000002
		0 0.7006884518633093 0.40345170000000002
		0 1.7221365137105891 0.40345170000000002
		0 1.7221365137105891 0.6724194
		0 1.8048286037257015 0
		0 1.7221365137105891 -0.6724194
		0 1.7221365137105891 -0.40345170000000002
		0 0.7006884518633093 -0.40345170000000002
		;
createNode lightLinker -n "lightLinker1";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
select -ne :time1;
	setAttr ".o" 1;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 2 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :lightList1;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	setAttr ".ren" -type "string" "mentalRay";
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :defaultHardwareRenderGlobals;
	setAttr ".fn" -type "string" "im";
	setAttr ".res" -type "string" "ntsc_4d 646 485 1.333";
connectAttr ":defaultLightSet.msg" "lightLinker1.lnk[0].llnk";
connectAttr ":initialShadingGroup.msg" "lightLinker1.lnk[0].olnk";
connectAttr ":defaultLightSet.msg" "lightLinker1.lnk[1].llnk";
connectAttr ":initialParticleSE.msg" "lightLinker1.lnk[1].olnk";
connectAttr ":defaultLightSet.msg" "lightLinker1.slnk[0].sllk";
connectAttr ":initialShadingGroup.msg" "lightLinker1.slnk[0].solk";
connectAttr ":defaultLightSet.msg" "lightLinker1.slnk[1].sllk";
connectAttr ":initialParticleSE.msg" "lightLinker1.slnk[1].solk";
connectAttr "lightLinker1.msg" ":lightList1.ln" -na;
// End of arrow.ma
