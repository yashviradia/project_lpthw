class Song(object):

    def __init__(self, lyrics): # initialize your newly created object
        self.lyrics = lyrics    # 'self' for empty objects, set variables on it . Instance attribute, created mini-module is a object 

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally aroud the family",
                    "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
