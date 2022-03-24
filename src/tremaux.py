import random

class Tremaux:

    """ Luokka, joka vastaa Trémauxin algoritmin toteutuksesta. """

    def __init__(self, labyrintti, n):

        """ Luokan konstruktori.
        Args:
            labyrintti: moduulin Pyamaze avulla luotu olio, jolla on käytössä
            moduulin omat metodit.
            n: neliömuotoisen labyrintin leveys/korkeus.
        """

        self.labyrintti = labyrintti
        self.n = n
        self.aloitus = (n,n)
        self.maali = (1,1)
        self.maali_loytynyt = False
        self.nykyinen_ruutu = (self.aloitus[0], self.aloitus[1])
        self.jaljet = self._luo_ruudukko(self.n)
        self.tremaux_etsinta = []

    def _luo_ruudukko(self, n):

        """ Luo dictionary-tyyppisen ruudukon, jonka avulla seurataan labyrintissa 
        kuljettuja reittejä.

        Args:
            n: Labyrintin leveys/korkeus.
        Returns:
            ruudukko, tyypiltään dictionary. Ruudukon arvot ilmaisevat, onko kyseiseen ruutuun
            mahdollista kulkea.
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
                ruudukko[i] = 2
        return ruudukko

    def _laske_naapuriruudut(self, ruutu, arvo):

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

    def _mahdolliset_liikkeet(self, ruutu):

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

    def tremaux(self):

        """ Löytää reitin labyrintista noudattaen Trémauxin algoritmia.

        Returns:
            tremaux_etsinta: tyypiltään lista. Sisältää järjestyksessä ne ruudut, jotka
            algoritmi käy läpi etsiessään maaliruutua labyrintissa.
        """

        while not self.maali_loytynyt:

            self.tremaux_etsinta.append(self.nykyinen_ruutu)

            if self.nykyinen_ruutu == self.maali:
                self.maali_loytynyt = True
                break

            seinien_lkm = self._laske_naapuriruudut(self.nykyinen_ruutu, 0)

            if seinien_lkm >= 3:
                self.jaljet[self.nykyinen_ruutu[0], self.nykyinen_ruutu[1]] += 2
            else:
                self.jaljet[self.nykyinen_ruutu[0], self.nykyinen_ruutu[1]] += 1
            
            mahdolliset_liikkeet = self._mahdolliset_liikkeet(self.nykyinen_ruutu)

            if len(mahdolliset_liikkeet) >= 2:
                self.jaljet[self.nykyinen_ruutu[0], self.nykyinen_ruutu[1]] = 1

            ei_vierailtu = []
            on_vierailtu = []

            for i in mahdolliset_liikkeet:
                if i[2] == 0:
                    ei_vierailtu.append(i)
                if i[2] == 1:
                    on_vierailtu.append(i)

            ei_vierailtu_lkm = len(ei_vierailtu)
            on_vierailtu_lkm = len(on_vierailtu)

            seuraava_liike = []

            if ei_vierailtu_lkm > 0:
                seuraava_liike = ei_vierailtu[random.randint(0,ei_vierailtu_lkm-1)]
            else:
                seuraava_liike = on_vierailtu[random.randint(0,on_vierailtu_lkm-1)]

            self.nykyinen_ruutu = (seuraava_liike[0], seuraava_liike[1])

        return self.tremaux_etsinta