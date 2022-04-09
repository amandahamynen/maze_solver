from pyamaze import maze, agent, COLOR
from tremaux import Tremaux
from left_wall_follower import LeftWallFollower
from dead_end_filler import DeadEndFiller
import os

class App:
    def __init__(self, io):
        self.io = io
        self.komennot = {
            1: self.visualise_tremaux,
            2: self.visualise_left_wall_follower,
            3: self.visualise_dead_end_filler,
            4: self.lopeta
        }

    def visualise_tremaux(self):
        while True:
            koko = int(self.io.read("Labyrintin koko (anna yksi kokonaisluku): ").strip())
            if koko >= 1:
                break
            else:
                self.io.write("Koon tulee olla >= 1.")
        while True:
            nopeus = int(self.io.read("Simuloinnin nopeus millisekunteina (suositeltu 50): ").strip())
            if nopeus >= 1:
                break
            else:
                self.io.write("Nopeuden tulee olla >= 1.")
        m = maze(koko,koko)
        m.CreateMaze()
        print(m.maze_map)
        t = Tremaux(m, koko)
        tremaux_reitti = t.tremaux()
        a=agent(m,filled=True,footprints=True)
        m.tracePath({a:tremaux_reitti}, delay=nopeus)
        m.run()

    def visualise_left_wall_follower(self):
        while True:
            koko = int(self.io.read("Labyrintin koko (anna yksi kokonaisluku): ").strip())
            if koko >= 1:
                break
            else:
                self.io.write("Koon tulee olla >= 1.")
        while True:
            nopeus = int(self.io.read("Simuloinnin nopeus millisekunteina (suositeltu 50): ").strip())
            if nopeus >= 1:
                break
            else:
                self.io.write("Nopeuden tulee olla >= 1.")
        m = maze(koko,koko)
        m.CreateMaze()
        f = LeftWallFollower(m, koko)
        wall_follower_reitti = f.wall_follower()
        a=agent(m,filled=True, shape='arrow')
        m.tracePath({a:wall_follower_reitti}, delay=nopeus)
        m.run()

    def visualise_dead_end_filler(self):
        while True:
            koko = int(self.io.read("Labyrintin koko (anna yksi kokonaisluku): ").strip())
            if koko >= 1:
                break
            else:
                self.io.write("Koon tulee olla >= 1.")
        while True:
            nopeus = int(self.io.read("Simuloinnin nopeus millisekunteina (suositeltu 50): ").strip())
            if nopeus >= 1:
                break
            else:
                self.io.write("Nopeuden tulee olla >= 1.")
        m = maze(koko,koko)
        m.CreateMaze()
        d = DeadEndFiller(m, koko)
        dead_end_filler_etsinta, dead_end_filler_reitti = d.dead_end_filling()
        a=agent(m,filled=True,footprints=True, color=COLOR.red)
        b=agent(m,filled=True,footprints=True, color=COLOR.green)
        m.tracePath({a:dead_end_filler_etsinta},showMarked=True, delay=nopeus)
        m.tracePath({b:dead_end_filler_reitti},showMarked=True, delay=nopeus)
        m.run()

    def lopeta(self):
        raise SystemExit()

    def clearConsole(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    def tulosta_komennot(self):
        self.clearConsole()
        self.io.write("Valitse haluamasi algoritmi, jonka toiminnan haluat visualisoida, tai lopeta ohjelma: \n")
        self.io.write(" 1. Trémaux")
        self.io.write(" 2. Left Wall Follower")
        self.io.write(" 3. Dead End Filler")
        self.io.write(" 4. Lopeta ohjelma\n")

    def run(self):
        self.clearConsole()
        while True:
            self.tulosta_komennot()
            komento = self.io.read("Valitse toiminto (syötä kokonaisluku): ")
            try:
                komento_id = int(komento.strip())
                toiminta = self.komennot.get(komento_id)
                if toiminta:
                    toiminta()
                    self.lopeta()
                else:
                    self.io.write("Virheellinen syöte \n")
                    self.tulosta_komennot()
            except Exception as error:
                self.io.write("Virheellinen syöte \n")
            except SystemExit:
                break