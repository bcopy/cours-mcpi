import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.event
import mcpi.connection
import mcpi.util

import random
import math
import time


mc = minecraft.Minecraft.create()


####################
# inserer votre code ici


def cacherLeTresor():
	positionDuJoueur = mc.player.getPos()
	x = random.randint(int(positionDuJoueur.x)-50, int(positionDuJoueur.x)+50)
	z = random.randint(int(positionDuJoueur.z)-50, int(positionDuJoueur.z)+50)
	y = int(positionDuJoueur.y - 5)
	mc.setBlock(x,y,z, block.GOLD_BLOCK)
	return [x,y,z]
	
	
def distanceVersLeTresor(tresor):
	positionDuJoueur = mc.player.getPos()
	distanceX = tresor[0] - positionDuJoueur.x;
	distanceY = tresor[1] - positionDuJoueur.y;
	distanceZ = tresor[2] - positionDuJoueur.z;
	distance = math.sqrt(distanceX **2 + distanceY **2 +  distanceZ **2)
	return math.floor(distance)
	
positionDuTresor = cacherLeTresor()
mc.postToChat("La chasse est ouverte !")
print positionDuTresor
dernierePosition = mc.player.getPos()
derniereDistance = distanceVersLeTresor(positionDuTresor)

tresorTrouve = False
try:
	while (not tresorTrouve):
		if (dernierePosition != mc.player.getPos()):
			nouvelleDistance = distanceVersLeTresor(positionDuTresor)
			if(nouvelleDistance <=1):
				mc.postToChat("Tu as trouve !")
				tresorTrouve = True
			elif(nouvelleDistance > derniereDistance):
				mc.postToChat("tu refroidis... distance "+str(nouvelleDistance))
			elif (nouvelleDistance <= derniereDistance):
				mc.postToChat("tu chauffes... distance "+str(nouvelleDistance))
			dernierePosition = mc.player.getPos()
			derniereDistance = nouvelleDistance
					
		time.sleep(1)
	if mc.getBlock(positionDuTresor[0], positionDuTresor[1], positionDuTresor[2])== block.AIR:
		mc.setBlock(positionDuTresor[0], positionDuTresor[1], positionDuTresor[2], block.GOLD_BLOCK)
	mc.postToChat("Bravo, la chasse est terminee")	
except KeyboardInterrupt:
	print "Jeu interrompu"	

#
####################
