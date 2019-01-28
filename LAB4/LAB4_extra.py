

class Song(object):

	def __init__(self,lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		print(self.lyrics)

beatles_song = Song(["Here comes the sun duru duru" ])
beatles_song.sing_me_a_song()