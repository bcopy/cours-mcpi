import api.geometrie as geometrie
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

geom = geometrie.Geometrie(mc)

####################
# inserer votre code ici
geom.prepareLeSol(0,0, 100, 100)
etages = ["Rez de chaussee", "1er etage", "2eme etage"]
for ypos in xrange(0,2):
	print etages[ypos]
	geom.placeUnPlancher(0,ypos*5,0, 32, 32, block.SANDSTONE)
	geom.placeUnEscalierDirectionX(2,(ypos*5)+1,2,5, 2, block.STONE)
	for zpos in [0,8,16,24]:
		for xpos in [0,8,16,24]:
			geom.placeUnePiece(xpos,ypos*5,zpos,8,8,5,block.STONE)
#
####################


