class DeadEndFiller:

    """ Luokka, joka vastaa dead-end filling algoritmin toiminnasta. """

    def __init__(self, labyrintti, n):
        self.labyrintti = labyrintti
        self.aloitus = (n,n)
        self.maali = (1,1)
        self.n = n
        self.nykyinen_ruutu = (self.aloitus[0], self.aloitus[1])
        self.jaljet = self.luo_ruudukko(self.n)
        self.etsinta = []
        self.reitti = []
        self.umpikujat = []
        self.maali_loytynyt = False

    def luo_ruudukko(self, n):

        """ Luo dictionary-tyyppisen ruudukon, jonka avulla seurataan labyrintissa 
        kuljettuja reittejä.

        Args:
            n: Labyrintin leveys/korkeus.
        Returns:
            ruudukko, tyypiltään dictionary. Ruudukon arvot ilmaisevat, onko kyseiseen ruutuun
            mahdollista kulkea. Ulkoseinät saavat arvon 3.
        """

        rivit = [i for i in range(0,n+2)] * (n+2)
        sarakkeet = []
        x = 0
        while x <= n+1:
            for i in range(0,n+2):
                sarakkeet.append(x)
            x += 1
        arvot = [0] * (n+2) * (n+2)
        ruudukko = {(x,y): val for x, y, val in zip(rivit,sarakkeet,arvot)}
        for i in ruudukko:
            if i[0] == 0 or i [1]==0 or i[0] == n+1 or i[1] == n+1:
                ruudukko[i] = 3
        return ruudukko

    def etsi_ja_merkitse_umpikujat(self):
        for x in range(1, self.n + 1):
            for y in range(1, self.n + 1):
                if self.laske_naapuriruudut((x,y), 1) == 1 and (x,y) != self.maali and (x,y) != self.aloitus:
                    self.umpikujat.append((x,y))
                    self.labyrintti.markCells.append((x,y))

    def laske_naapuriruudut(self, ruutu, arvo):

        """ Laskee joko seinien tai avonaisten polkujen määrän tietyssä ruudussa.

        Args:
            ruutu: metodille annettava tuple-muotoinen arvo. Ensimmäinen arvo on ruudun
            x-koordinaatti ja toinen y-koordinaatti.
            arvo: Joko 0 tai 1. Jos 0, niin seinä, jos 1, niin avoin polku.
        Returns:
            lkm: tyypiltään integer. Seinien/avointen polkujen lukumäärä.
        """

        x = ruutu[0]
        y = ruutu[1]
        lkm = 0
        if self.labyrintti.maze_map[x,y]['N'] == arvo:
            lkm += 1
        if self.labyrintti.maze_map[x,y]['E'] == arvo:
            lkm += 1
        if self.labyrintti.maze_map[x,y]['W'] == arvo:
            lkm += 1
        if self.labyrintti.maze_map[x,y]['S'] == arvo:
            lkm += 1
        return lkm

    def mahdolliset_liikkeet(self, ruutu):

        """ Palauttaa listan, joka sisältää sellaiset ruudut, joihin on mahdollista
        kulkea tietystä ruudusta. Lisäksi ilmaisee jokaisen mahdollisen ruudun kohdalla,
        kuinka monta kertaa kyseisestä ruudusta on kuljettu.

        Args:
            ruutu: tuple-tyyppinen arvo, jonka ensimmäinen arvo on ruudun x-koordinaatti
            ja toinen y-koordinaatti.
        Returns:
            mahdolliset: tyypiltään lista, joka sisältää mahdolliset liikkeet. Jokaisen alkion
            nollas indeksi on kyseisen liikkeen x-koordinaatti, ensimmäinen y-koordinaatti ja
            toinen indeksi kertoo, kuinka monta kertaa kyseisessä ruudussa on käyty.
        """

        x = ruutu[0]
        y = ruutu[1]
        mahdolliset = []
        sallitut_liikkeet = [0,1]
        if self.labyrintti.maze_map[x,y]['N'] == 1 and self.jaljet[x-1,y] in sallitut_liikkeet:
            mahdolliset.append([x-1,y,self.jaljet[x-1,y]])
        if self.labyrintti.maze_map[x,y]['E'] == 1 and self.jaljet[x,y+1] in sallitut_liikkeet:
            mahdolliset.append([x,y+1,self.jaljet[x,y+1]])
        if self.labyrintti.maze_map[x,y]['W'] == 1 and self.jaljet[x,y-1] in sallitut_liikkeet:
            mahdolliset.append([x,y-1,self.jaljet[x,y-1]])
        if self.labyrintti.maze_map[x,y]['S'] == 1 and self.jaljet[x+1,y] in sallitut_liikkeet:
            mahdolliset.append([x+1,y,self.jaljet[x+1,y]])
        return mahdolliset

    def dead_end_filling(self):

        """ Löytää reitin labyrintista noudattaen dead-end filling algoritmia.

        Returns:
            etsinta: tyypiltään lista. Sisältää järjestyksessä ne ruudut, jotka
            algoritmi käy läpi umpikujista jättäen jäljelle reitin, joka ratkaisee
            labyrintin.
            reitti: labyrintin ratkaisu reitti, tyypiltään lista.
        """

        self.etsi_ja_merkitse_umpikujat()
        if self.umpikujat:
            self.nykyinen_ruutu = self.umpikujat[0]
        else:
            self.nykyinen_ruutu = self.aloitus

        while True:

            if self.nykyinen_ruutu == self.aloitus:
                if len(self.umpikujat) <= 1:
                    break
                elif len(self.umpikujat) >= 2:
                    self.umpikujat.pop(0)
                    self.nykyinen_ruutu = self.umpikujat[0]
            if self.nykyinen_ruutu == self.maali:
                self.etsinta.append(self.maali)
            if len(self.mahdolliset_liikkeet(self.nykyinen_ruutu)) == 1:
                self.etsinta.append(self.nykyinen_ruutu)
                self.jaljet[self.nykyinen_ruutu[0], self.nykyinen_ruutu[1]] = 2
                seuraava = self.mahdolliset_liikkeet(self.nykyinen_ruutu)
                self.nykyinen_ruutu = (seuraava[0][0], seuraava[0][1])
            else:
                self.umpikujat.pop(0)
                if len(self.umpikujat) == 0:
                    break
                self.nykyinen_ruutu = self.umpikujat[0]

        self.nykyinen_ruutu = self.aloitus

        while not self.maali_loytynyt:

            self.reitti.append(self.nykyinen_ruutu)
            self.jaljet[self.nykyinen_ruutu[0], self.nykyinen_ruutu[1]] = 2
            if self.nykyinen_ruutu == self.maali:
                self.maali_loytynyt = True
                break
            seuraava = self.mahdolliset_liikkeet(self.nykyinen_ruutu)
            self.nykyinen_ruutu = (seuraava[0][0], seuraava[0][1])

        if not self.etsinta:
            self.etsinta = [self.aloitus]


        return self.etsinta, self.reitti
        