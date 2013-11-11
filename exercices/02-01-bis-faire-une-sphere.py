import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.event
import mcpi.connection
import mcpi.util
import math

mc = minecraft.Minecraft.create()


####################
# inserer votre code ici


def dessineUneSphere(x, y, z, radius, typeDeBloc):
	for xr in range(radius*-1,radius):
		for yr in range(radius*-1, radius):
			for zr in range(radius*-1,radius):
				if (xr**2 + yr**2 + zr**2 < radius**2 ) :
					mc.setBlock(x + xr, y + yr + radius, z - zr - 10, typeDeBloc)


def dessineUneDemiSphere(x, y, z, radius, typeDeBloc):
	for xr in range(radius*-1,radius):
		for zr in range((int(math.sqrt(radius**2 - xr**2))*-1),int(math.sqrt(radius**2 - xr**2))):
			print(str(radius**2) +" "+ str(xr**2) +" "+ str( zr**2))
			yr = int(math.sqrt(radius**2 - xr**2 - zr**2))
			mc.setBlock(xr+x, y-yr, zr+z, typeDeBloc)


mc.postToChat("Construction de la sphere...")

#
# Ajouter l'appel de fonction pour dessiner la sphere aux coordonnees 0, 5, 5
#
mc.postToChat("Construction terminee !")
#
####################
