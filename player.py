class Entity:
	def __init__(self, entityTexture, entityName, entityColor, entityPos):
		self.entityName = entityName
		self.entityPos = entityPos
		self.entityTexture = entityTexture

	def draw_entity(self, stdscr, offset):
		cPos = (self.entityPos[0] + offset[0], self.entityPos[1] + offset[1])
		
		if (cPos[0] >= 0 and cPos[0] < 30) and (cPos[1] >= 0 and cPos[1] < 119):
			stdscr.addstr(self.entityPos[0] + offset[0], self.entityPos[1] + offset[1], self.entityTexture)

	def get_pos(self):
		return self.entityPos

	def set_pos(self, newPos):
		self.entityPos = newPos


class Player(Entity):
	def move(self, dir):
		newPos = self.get_pos()
		newPos[0] += dir[0]
		newPos[1] += dir[1]

		self.set_pos(newPos)
