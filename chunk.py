class Chunk:
	def __init__(self, chunkID, chunkContents):
		self.chunkID = chunkID
		self.chunkContents = chunkContents

	def getChunkID(self):
		return self.chunkID

	def getContents(self):
		return self.chunkContents