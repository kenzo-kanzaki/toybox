#Autorig by Jonas Lilja 2013
#import language
import maya.cmds as cmds

arm = ['clavicle', 'shoulder', 'elbow', 'elbowPV', 'wrist']
leg = ['hip', 'knee', 'kneePV', 'foot', 'ball', 'toe']
ext = ['_loc', '_cnst', '_jnt', '_ctrl', '_grp']

#Right arm locators
def rightArmLoc (arm):
    side = raw_input('Define naming?')
    cmds.spaceLocator( p=(0, 0, 0), n= side + '_' + arm [0] + ext [0])
    cmds.spaceLocator( p=(2, 2, 0), n= side + '_' + arm [1] + ext [0])
    cmds.spaceLocator( p=(4, 2, 0), n= side + '_' + arm [2] + ext [0])
    cmds.spaceLocator( p=(4, 2, -10), n= side + '_' + arm [3] + ext [0])
    cmds.spaceLocator( p=(6, 2, 0), n= side + '_' + arm [4] + ext [0])
    cmds.parentConstraint( side + '_' + arm [1] + ext [0], side + '_' + arm [4] + ext [0], side + '_' + arm [2] + ext [0], n = side + '_' + arm[1] + 'Parent' )
    cmds.group (side + '_' + arm [0] + ext [0] , name = side + '_arm' + ext [4] )
    cmds.parent(side + '_' + arm [3] + ext [0] , side + arm [0] + '_loc')
    cmds.parent(side + '_shoulder_loc', side + '_clavicle_loc')
    cmds.parent(side + '_wrist_loc', side + '_clavicle_loc')
    cmds.parent(side + '_elbow_loc', side + '_clavicle_loc')
    cmds.parent(side + '_shoulderParent_cnst', side + '_clavicle_loc') 

#definitions with lists


if cmds.window('JonasAutorig', exists=True):
        cmds.deleteUI('JonasAutorig', window=True)

cmds.window( 'JonasAutorig', width=800, height=800 )
cmds.columnLayout( adjustableColumn=True )
cmds.button(width=100, label='Right arm', command=rightArmLoc)
cmds.button(width=100, label='Left arm', command=leftArmLoc )
cmds.button(width=100, label='Right leg' )
cmds.button(width=100, label='Left leg' )
cmds.button(width=100, label='Spine' )
cmds.button(width=100, label='Neck' )
cmds.button(width=100, label='Tail' )
cmds.button(width=100, label='Wings' )
cmds.showWindow()