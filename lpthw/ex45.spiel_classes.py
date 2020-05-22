class Scene(object):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_navibot):
        pass

    def play(self):
        pass

class Tod(Scene):

    def enter(self):
        pass

class Schluessel(Scene):

    def enter(self):
        pass

class GefaengnisUndWaffen(Scene):

    def enter(self):
        pass

class DieSoldatenKaempfenMitAusserirdischen(Scene):

    def enter(self):
        pass

class LochRaum(Scene):

    def enter(self):
        pass

class EssenUndTrinken(Scene):

    def enter(self):
        pass

class TreppeRaum(Scene):

    def enter(self):
        pass

class DieMaschineRaum(Scene):

    def enter(self):
        pass

class Navibot(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_navibot = Navibot('Schluessel')
a_spiel = Engine(a_navibot)
a_spiel.play()
