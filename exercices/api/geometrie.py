import mcpi.block as block
import mcpi.minecraft as minecraft
import math

class Geometrie:
	def __init__(self, minecrft):
		self.minecraft = minecrft
	
	def placeUnMurDirectionX(self,x,y, z, largeur, hauteur,materiel):
		for xpos in xrange(x, x+largeur):
			for ypos in xrange(y, y+hauteur):
				self.minecraft.setBlock(xpos,ypos,z,materiel)
				
	def placeUnMurDirectionZ(self,x,y, z, largeur, hauteur,materiel):
		for zpos in xrange(z, z+largeur):
			for ypos in xrange(y, y+hauteur):
				self.minecraft.setBlock(x,ypos,zpos,materiel)
				
	def placeUnePiece(self,x,y,z, largeur, profondeur, hauteur, materiel):
		self.placeUnMurDirectionX(x,y,z, profondeur, hauteur,materiel)
		self.placeUnMurDirectionX(x,y,z+largeur, profondeur, hauteur,materiel)
		self.placeUnMurDirectionZ(x,y,z, largeur, hauteur,materiel)
		self.placeUnMurDirectionZ(x+profondeur,y,z, largeur+1, hauteur, materiel)
				
	def placeUnPlancher(self,x,y,z, largeur, profondeur, materiel):
		for xpos in xrange(x, x+largeur):
			for zpos in xrange(z, z+profondeur):
				self.minecraft.setBlock(xpos,y,zpos,materiel)
				
	def placeUnEscalierDirectionX(self,x,y,z, longueurEscalier, largeurDesMarches,  materiel):
		for xpos in xrange(x, x+longueurEscalier):
			self.minecraft.setBlocks(xpos,y, z, xpos,y, z+largeurDesMarches, materiel)
			y = y+1
			
			
		
	def prepareLeSol(self,x,z, largeur, profondeur):
		self.minecraft.setBlocks(x-math.floor(largeur/2),0  ,z -math.floor(profondeur/2)  ,x+math.floor(largeur/2),30, z+math.floor(profondeur/2), block.AIR)
		self.minecraft.setBlocks(x-math.floor(largeur/2),-5  ,z - math.floor(profondeur/2)  ,x+math.floor(largeur/2),0, z+math.floor(profondeur/2), block.GRASS)
		
