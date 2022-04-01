class LeftWallFollower:

    def __init__(self, labyrintti, n):
        self.labyrintti = labyrintti
        self.aloitus = [n,n]
        self.maali = [1,1]
        self.katseen_suunta = 'W'
        self.nykyinen_ruutu = [self.aloitus[0], self.aloitus[1]]
        self.maali_loytynyt = False
        self.etsinta = []

    def vasen_seina(self, ruutu):
        x = ruutu[0]
        y = ruutu[1]
        if self.katseen_suunta == 'N':
            return self.labyrintti.maze_map[x,y]['W'] == 0
        elif self.katseen_suunta == 'E':
            return self.labyrintti.maze_map[x,y]['N'] == 0
        elif self.katseen_suunta == 'W':
            return self.labyrintti.maze_map[x,y]['S'] == 0
        elif self.katseen_suunta == 'S':
            return self.labyrintti.maze_map[x,y]['E'] == 0

    def seina_edessa(self, ruutu):
        x = ruutu[0]
        y = ruutu[1]
        if self.katseen_suunta == 'N':
            return self.labyrintti.maze_map[x,y]['N'] == 0
        elif self.katseen_suunta == 'E':
            return self.labyrintti.maze_map[x,y]['E'] == 0
        elif self.katseen_suunta == 'W':
            return self.labyrintti.maze_map[x,y]['W'] == 0
        elif self.katseen_suunta == 'S':
            return self.labyrintti.maze_map[x,y]['S'] == 0

    def kaanny_vasemmalle(self):
        if self.katseen_suunta == 'N':
            self.katseen_suunta = 'W'
        elif self.katseen_suunta == 'E':
            self.katseen_suunta = 'N'
        elif self.katseen_suunta == 'W':
            self.katseen_suunta = 'S'
        elif self.katseen_suunta == 'S':
            self.katseen_suunta = 'E'

    def kaanny_oikealle(self):
        if self.katseen_suunta == 'N':
            self.katseen_suunta = 'E'
        elif self.katseen_suunta == 'E':
            self.katseen_suunta = 'S'
        elif self.katseen_suunta == 'W':
            self.katseen_suunta = 'N'
        elif self.katseen_suunta == 'S':
            self.katseen_suunta = 'W'

    def mene_eteenpain(self):
        x = self.nykyinen_ruutu[0]
        y = self.nykyinen_ruutu[1]
        if self.katseen_suunta == 'N':
            self.nykyinen_ruutu = [x-1, y]
        elif self.katseen_suunta == 'E':
            self.nykyinen_ruutu = [x, y+1]
        elif self.katseen_suunta == 'W':
            self.nykyinen_ruutu = [x, y-1]
        elif self.katseen_suunta == 'S':
            self.nykyinen_ruutu = [x+1, y]

    def wall_follower(self):

        while not self.maali_loytynyt:

            if self.nykyinen_ruutu == self.maali:
                self.maali_loytynyt = True
                break

            vasen = self.vasen_seina(self.nykyinen_ruutu)
            edessa = self.seina_edessa(self.nykyinen_ruutu)

            if not vasen:
                self.kaanny_vasemmalle()
                self.mene_eteenpain()
                self.etsinta.append(self.nykyinen_ruutu)
                continue
            elif not edessa:
                self.mene_eteenpain()
                self.etsinta.append(self.nykyinen_ruutu)
                continue
            else:
                self.kaanny_oikealle()

        return self.etsinta