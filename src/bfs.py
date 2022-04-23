class Leveyshaku:
    def __init__(self, labyrintti, n):
        self.labyrintti = labyrintti
        self.aloitus = (n,n)
        self.maali = (1,1)
        self.etsinta = []
        self.mahdolliset = [self.aloitus]
        self.kayty = [self.aloitus]

    def BFS(self):
        while len(self.mahdolliset) > 0:
            nykyinen = self.mahdolliset.pop()
            if nykyinen == self.maali:
                break
            for suunta in 'NEWS':
                if self.labyrintti.maze_map[nykyinen][suunta] == 1:
                    if suunta == 'N':
                        seuraava = (nykyinen[0]-1, nykyinen[1])
                    if suunta == 'E':
                        seuraava = (nykyinen[0], nykyinen[1]+1)
                    if suunta == 'W':
                        seuraava = (nykyinen[0], nykyinen[1]-1)
                    if suunta == 'S':
                        seuraava = (nykyinen[0]+1, nykyinen[1])
                    if seuraava in self.kayty:
                        continue
                    self.mahdolliset.append(seuraava)
                    self.kayty.append(seuraava)
                    self.etsinta.append(seuraava)

        return self.etsinta
