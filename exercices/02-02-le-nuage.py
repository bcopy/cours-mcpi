import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.event
import mcpi.connection
import mcpi.util

import time

mc = minecraft.Minecraft.create()


####################
# inserer votre code ici

def dessineLeNuage(x, y, z):
	for xp in xrange(x-2, x+2):
		for zp in xrange(z-2, z+2):
			mc.setBlock(xp, y, zp, block.WOOL)

def effaceLeNuage(x, y, z):
	for xp in xrange(x-2, x+2):
		for zp in xrange(z-2, z+2):
			mc.setBlock(xp, y, zp, block.AIR)


try:
	print "Nuage en cours..."
	dernierePosition = mc.player.getPos()
	while True:
		if(dernierePosition != mc.player.getPos()):
			effaceLeNuage(int(dernierePosition.x), int(dernierePosition.y) + 10, int(dernierePosition.z) +2)
			dernierePosition = mc.player.getPos()
			dessineLeNuage(int(dernierePosition.x), int(dernierePosition.y) + 10, int(dernierePosition.z) +2)
		time.sleep(0.3)
except KeyboardInterrupt:
	print "Interruption !"

#
####################
