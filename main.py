import curses
import tile
import entity
from chunk import Chunk
import random

# stdscr dimensions
h = 30
w = 119


# Chunk dimensions
cH = 128
cW = 16


# Key-key
# 0n, 1ne, 2e, 3se, 4s, 5sw, 6w, 7nw
kk = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


# EVERYTHING MUST BE IN THE FORMAT (Y, X)
cameraOrigin = [-70, 1]


# Total/master terrain map
tMap = []


# Total/master entity list
entities = []

# Draws all avaiable entities at their correct positions (again, VERY unoptimized)
def draw_all_entities(stdscr, offset):
	for e in entities:
		e.draw_entity(stdscr, offset)

# Easy function to create generic entity
def create_entity(entityTexture, entityName, entityColor, entityPos):
	e = entity.Entity(entityTexture, entityName, entityColor, entityPos)
	entities.append(e)
	return e


def gen_chunk(chunkID):
	cMap = []

	# initialization
	for i in range(cH):
		row = []
		for j in range(cW):
			row.append(0)
		cMap.append(row)

	# generating
	for i in range(cH):
		for j in range(cW):
			if i > 64:
				cMap[i][j] = 1
			elif i == 64:
				cMap[i][j] = 2

	fooChunk = Chunk(chunkID, cMap)
	tMap.append(fooChunk)
	return fooChunk


def draw_chunk(stdscr, chunk, offset):
	for i in range(cH):
		for j in range(cW):
			cTile = tile.tileList[chunk.chunkContents[i][j]]
			cPos = (i + offset[0], j + offset[1])
			if (cPos[0] >= 0 and cPos[0] < h) and (cPos[1] >= 0 and cPos[1] < w):
				if type(cTile.tileTexture) == list:
					# Choosing texture from pool based on list position (seed makes the value the same every time)
					random.seed(i * j)
					rTex = random.choice(cTile.tileTexture)

					stdscr.addstr(cPos[0], cPos[1], rTex, curses.color_pair(cTile.tileColor))
				else:
					stdscr.addstr(cPos[0], cPos[1], cTile.tileTexture, curses.color_pair(cTile.tileColor))

# Used for distinguising empty vs. tiles (VERY unoptimized)
def draw_debug(stdscr):
	for i in range(h):
		for j in range(w):
			stdscr.addstr(i, j, "Ø")

# Draws all avaiable chunks at their correct positions (again, VERY unoptimized)
def draw_screen_all(stdscr, offset):
	for c in tMap:
		draw_chunk(stdscr, c, (offset[0], offset[1] + (c.chunkID * cW)))




def main(stdscr):
	curses.initscr()

	curses.curs_set(0)
	crash = False

	# Player
	pl = entity.Player("☻", "steve", 4, [63, 0])
	entities.append(pl)

	# Colors
	curses.start_color()
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN) # Organic
	curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW) # Brown/earthy
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_CYAN) # Sky blue
	curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_RED) # Black and yellow

	gen_chunk(-2)
	gen_chunk(-1)
	gen_chunk(0)
	gen_chunk(1)
	gen_chunk(2)

	# Update

	while not crash:
		k = stdscr.getch()
		stdscr.clear()

		if k == ord("q"):
			crash = True

		if k == ord("w"):
			pl.move(kk[0])
		elif k == ord("s"):
			pl.move(kk[4])
		if k == ord("a"):
			pl.move(kk[6])
		elif k == ord("d"):
			pl.move(kk[2])

		# Setting camera origin to player position (inverting)
		cameraOrigin[0] = (pl.get_pos()[0] * -1) + int(h/2)
		cameraOrigin[1] = (pl.get_pos()[1] * -1) + int(w/2)

		draw_screen_all(stdscr, cameraOrigin)
		draw_all_entities(stdscr, cameraOrigin)
		stdscr.refresh()

curses.wrapper(main)