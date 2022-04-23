class Leveyshaku:

    """ Luokka, joka vastaa leveyshakualgoritmin toteutuksesta. """

    def __init__(self, labyrintti, n):

        """ Luokan konstruktori.
        Args:
            labyrintti: moduulin Pyamaze avulla luotu olio, jolla on käytössä
            moduulin omat metodit.
            n: neliömuotoisen labyrintin leveys/korkeus. 
        """

        self.labyrintti = labyrintti
        self.aloitus = (n,n)
        self.maali = (1,1)
        self.etsinta = []
        self.mahdolliset = [self.aloitus]
        self.kayty = [self.aloitus]

    def BFS(self):

        """ Löytää reitin labyrintista noudattaen leveyshakualgoritmia.

        Returns:
            etsinta: tyypiltään lista. Sisältää järjestyksessä ne ruudut, jotka
            algoritmi käy läpi etsiessään maaliruutua labyrintissa.
        """

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
