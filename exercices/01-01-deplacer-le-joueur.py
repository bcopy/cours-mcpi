import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()


x = 10
y = 11
z = 12

# deplacer le joueur
mc.player.setTilePos(x,y,z)
