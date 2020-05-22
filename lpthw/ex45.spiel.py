
from textwrap import dedent
from random import randint
from sys import exit

print(dedent("""
      Die Menschen sind interplanetare Arten geworden
      ,sie haben große Städte auf dem Mars zu bauen angefangen.
      Der Mars ist für alle Menschen auf der Erde zu einem
      bewohnbaren Planeten geworden. Das Fliegen ist jetzt von Hamburg
      nach Abu Dhabi dauert nur 30 Minuten. Jeder kann Mars innerhalb
      der Woche erreichen. Dies ist eine große Leistung in der Geschichte
      der Menschheit.

      Aber, es tritt jedoch ein Problem auf. Einige Bewohner der
      fremden Galaxie haben die menschlichen Städte auf dem Mars
      angegriffen.
      Du bist der einzige menschliche Überlebende auf dem Mars.
      Deine Aufgabe ist es, die Festung dieser Ching Chu-Außerirdischen in die
      Luft zu jagen und den Mars zu retten.
      """))

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter()")
        exit(1)

class Engine():

    def __init__(self, scene_navibot):
        self.scene_navibot = scene_navibot

    def play(self):
        current_scene = self.scene_navibot.opening_scene()
        last_scene = self.scene_navibot.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_navibot.next_scene(next_scene_name)

        # be sure to print out the last name
        current_scene.enter()


class Tod(Scene):

    stitchwort = [
            "Not kennt kein Gebot.",
            "Ein boeser Geselle fuehrt den andern zur Hoelle.",
            "Ehrgeiz und Floehe springen gern in die Hoehe.",
            "Mit Luegen und Listen fuell nicht deine Kisten",
            "Fischers Fritz fischt frische Fische. Frische Fische fischt Fischers Fritz."
    ]

    def enter(self):
        print(Tod.stitchwort[randint(0, len(self.stitchwort)-1)])
        exit(1)


class Schluessel(Scene):

    def enter(self):
        print(dedent("""
              Dieses Zimmer haben viele Schluessel und dort siehst du..
              Die Leute des Mars im Gefaengnis. Jetzt musst du die Aliens töten,
              um die Leute zu befreien.
              Du gehst in das Zimmer des Schluessel, das im grossen Schloss ist, aber
              sofort kam einer ausseridischer da und er regte sich auf.
              Was wirst du machen jetzt? Ach ja, du hast Status Beam Machine mit dir.
              """))

        action = input("> ")

        if action == "schiessen" or "jagen":
            print(dedent("""
                  Du nimmst die Schluessel und erfreist die Leute. Gerade hast du eine grosse Armee
                  bei dir. Und du triffst mit dem Befehlshaber der Armee. Die anderen Leuten des
                  Mars muessen retten. Deshalb befiehlt der Befehlshaber Herr Mueller den einigen
                  Soldaten, die Leute vom Schloss zu retten.
                  Dann diskutierst du mit dem Befehlshaber die Karte des Schlosses und beide
                  bilden die Strategie zusammen.
                  Die Soldaten sind fertig für die Kaempfen gegenueber der Aliens.
                  Unser Ziel ist es, die Maschine zu zerstören, die die neuen Roboter produziert.
                  Jetzt gehen alle zum Zimmer 2"""))
            return 'gefaengnis_und_waffen'

        elif action == "rennen":
            print(dedent("""
                  Die Aliens sind gegen dich gekommen und habe deine Status Beam Machine
                  genommen und jetzt bist du in einer gefaehrlichen Situation. Du musst
                  unbeding was machen sonst zerstoeren dich die ausseridischer.
                  Zum Glueck erinnerst du dich ein stitchwort...
                  Als die Aliens kamen naeher sagst du Scherz, 'Zwischen zweiundzwanzig
                  schwankenden Zwetschenzweigne schwirren zweiundzwanzig schwarze,
                  zwitschernde Schwalben.'
                  """))
            return 'tod'

        else:
            print(dedent("""
                  Was?! Du hast keine Idee, was gerade passiert ist.
                  Das ist wirklich schade. Bitte lern das Spiel noch mal!
                  Bis dann Tschuess. Berechnet nicht."""))
            return 'schluessel'


class GefaengnisUndWaffen(Scene):

    def enter(self):
        print(dedent("""
              Hier sind auch mehrere Soldaten und du erfriest diese zusammen mit den
              anderen Soldaten. Jetzt ist die Armee sehr stark geworden worden.
              Alle muessen schnell wie moeglich zur Maschine gehen.
              Hier gibt zwei Tuer. Welche Tuer waehlst du?"""))

        action = input("> ")
        if action == 'one':
            print("Jetzt gehen sie in das naechste Zimmer...")
            return 'die_soldaten_kaempfen_mit_ausserirdischen'

        else:
            print("Gott sei Dank, das ist eine falsche Tuer, Mensch!")
            return 'tod'


class DieSoldatenKaempfenMitAusserirdischen(Scene):

    def enter(self):
        print(dedent("""
              Hier ist die Verbindung, wo es zahlreiche Aliens gibt.
              Deine Soldaten und du musst gegen sie kämpfen.
              Sie benötigen mehr Autos und Raumschiffe,
              um die Bürger des Mars sicher zu retten. Die Aliens sind sehr Aerger.
              Du und deine Soldaten haben jetzt gekaempft.
              Sofort kommen zwei Aliens zu dir und schiessen dir.
              Was wirst du machen?"""))

        action = input("> ")

        if action == 'hocken':
            print(dedent("""
                  Gut getan. Dann hast du die anderen Aliens getoetet. Nun
                  musst du in das naechste Zimmer gehen. Die Soldaten haben die
                  Einwohner des Mars wie Damen und Kinder gerettet.
                  Du rennst schnell wie moeglich zum Loch Raum."""))
            return 'loch_raum'

        else:
            print(dedent("""
                  Oh! Scheisse, du musst jetzt das Krieg vom Beginnen starten.
                  Das ist nicht gut. Die Soldaten brauchen einen Leiter und der
                  Befehlshaber Herr Mueller ist dafuer nicht mehr geeignet."""))
            return 'schluessel'



class LochRaum(Scene):

    def enter(self):
        print(dedent("""
              Hier gibt es ein staerker unterschuetzer Sicher, den du dekodieren
              musst. Dieses Raum musst du einschalten, weil die Soldaten sehr
              hungrig sind und die Leute auch brauchen etwas zum Essen und Trinken.
              Die Tuer verlangt fuer das Passwort und dieses besteht aus vier
              Zeichnen."""))

        code = f"{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}"
        print(code)

        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 9:
            print("UNGULTIG!!!!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                  Die Tuer wird eingeschaltet. Es klingt etwas und die Soldaten waren
                  begeistert. Aber, an diesem Moment kommt eine Frage
                  'Was ist diese Nummer sogennate?'"""))

            antwort = input("> ")
            if antwort == "Ramanujans Nummer":
                print("Die Tuer ist jetzt eingeschaltet worden.")
                return 'essen_und_trinken'

            else:
                print("Bitte versuchen Sie nach 10 Minuten.")
                return 'schluessel'

            return 'essen_und_trinken'

        else:
            print(dedent("""
                  Das Loch klagt ein bisschen und dann das Nuclearwaffen ist
                  explodiert worden. Die allen Soldaten sind getoetet worden."""))
            return 'schluessel'



class EssenUndTrinken(Scene):

    def enter(self):
        print(dedent("""
              Die Soldaten sind sehr hungrig und deshalb essen sie so viel. Du
              musst jetzt die Karte ansehen, um den Chef zu fangen und die
              Maschine zu zerstoeren."""))
        return 'treppe_raum'


class TreppeRaum(Scene):

    def enter(self):
        print(dedent("""
              Jetzt gehen du und der Befehlshaber zum Zimmer, in dem der Chef mit
              der Maschine diese Aliens herstellt. Du hast der Befehlshaber der
              Aliens getoetet und Fingurdruck genommen. Die Tuer zum Zimmer des Chefs
              braucht ein Fingurdruck. Aber dann musst du auch ein Zungenbrecher
              drucken.
              """))
        print(dedent("""
              Befehlshaber: Druck 'Frischers Fritz fischt frische Fische.
              Frische Fische fischt Frischers Fritz.'"""))

        action = input("> ")
        zungenbrecher = """Frischers Fritz fischt frische Fische. Frische Fische fischt Frischers Fritz."""

        if action == zungenbrecher:
            print("Die Tuer ist geoeffnet worden und der Chef ist getoetet worden.")
            return 'die_maschine_raum'
        else:
            return 'tod'



class DieMaschineRaum(Scene):

    def enter(self):

        print(dedent("""
              Jetzt hast du die Maschine, die die Aliens hergestellt hast,
              zerstoert. Du bist wirklich Helder! Du hast der Mars gerettet."""))

        return 'finished'

class Finished(Scene):

    def enter(self):
        print("Du hast gewonnen. Sehr gut.")
        return 'finished' 

class Navibot(object):

    scenes = {
        'schluessel': Schluessel(),
        'gefaengnis_und_waffen': GefaengnisUndWaffen(),
        'tod': Tod(),
        'die_soldaten_kaempfen_mit_ausserirdischen': DieSoldatenKaempfenMitAusserirdischen(),
        'loch_raum': LochRaum(),
        'essen_und_trinken': EssenUndTrinken(),
        'treppe_raum': TreppeRaum(),
        'die_maschine_raum': DieMaschineRaum()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Navibot.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_navibot = Navibot('schluessel')
a_spiel = Engine(a_navibot)
a_spiel.play()
