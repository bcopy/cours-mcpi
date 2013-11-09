import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.event
import mcpi.connection
import mcpi.util

mc = minecraft.Minecraft.create()


####################
# inserer votre code ici



for x in xrange(1, 20):
	for y in xrange(4, 20):
		mc.setBlock(x, y, 0, block.STONE)


#
####################
print "Completed !"
