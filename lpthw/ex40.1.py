class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            print('-' * 10)
            print("good job")

zugenbrecher_eins = Song(["""\nSchnecken erschrecken, wenn Schnecken,
an Schneken schlecken, weil zum,
Schrecken vieler Schneken, Schneken nicht schmecken.\n"""])


zugenbrecher_zwei = Song(["""\nWenn Fliegen hinter Fliegen fliegen,
fliegen Fliegen Fliegen hinterher.\n"""])


zugenbrecher_eins.sing_me_a_song()

zugenbrecher_zwei.sing_me_a_song()
