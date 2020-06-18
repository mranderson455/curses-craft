class Tile:
	def __init__(self, tileTexture, tileName, tileColor):
		self.tileTexture = tileTexture
		self.tileName = tileName
		self.tileColor = tileColor

# Block list
tileList = []

# These tiles can have multiple textures that will be static

tileList.append(Tile(' ', "Air", 3))
tileList.append(Tile(['≈', '~'], "Dirt", 2))
tileList.append(Tile("^", "Grass", 1))
