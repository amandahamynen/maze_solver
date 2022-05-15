# Toteustusraportti

## Ohjelman yleisrakenne

Ohjelma käynnistyy suorittamalla tiedosto index.py, joka tekee tarvittavat alustukset ja käynnistää app.py tiedoston.

Luokat
- IO, tiedostossa index.py. Huolehtii esimerkiksi io-kirjoittamisesta ja tulostuksesta.
- App, tiedostossa app.py. Sisältää ohjelman käyttöliittymän. Luokka kutsuu luokkia Tremaux, LeftWallFollower ja DeadEndFiller tarvittaessa.
- Tremaux, tiedostossa tremaux.py. Sisältää algoritmin toteutuksen, jolla labyrintistä löydetään maali noudattaen Trémauxin algoritmia. Luokassa lisäksi useampi apumetodi algoritmin toteutusta varten.
- LeftWallFollower, tiedostossa left_wall_follower.py. Sisältää algoritmin toteutuksen, jolla labyrintistä löydetään maali noudattaen Left Wall Follower algoritmia. Luokassa lisäksi useampi apumetodi algoritmin toteutusta varten.
- DeadEndFiller, tiedostossa dead_end_filler.py. Sisältää algoritmin toteutuksen, jolla labyrintistä löydetään maali noudattaen Dead-End Filler algoritmia. Luokassa lisäksi useampi apumetodi algoritmin toteutusta varten.
- Leveyshaku, tiedostossa bfs.py. Sisältää algoritmin toteutuksen, jolla labyrintistä löydetään maali noudattaen leveyshakualgoritmia.
- Lisäksi luokat, joilla testataan jokaista algoritmia.


## Saavutetut aika- ja tilavaativuudet

### Trémaux:

Aikavaativuus: O(n^2). Tilavaativuus O(n) sillä vieraillut ruudut tallennetaan muistiin.

### Left Wall Follower:

Aikavaativuus O(n+m), tilavaativuus O(n).

### Dead-End Filling:

Aikavaativuus O(n^2), sillä metodissa etsi_ja_merkitse_umpikujat on kaksi silmukkaa ja se on koodin hitain osa. Jälkeen päin mietittynä tämän olisi varmaan voinut toteuttaa tehokkaammalla tavalla. Tilavaativuus O(n) sillä vieraillut ruudut tallennetaan muistiin.

### Leveyshaku: 

Aikavaativuus O(n+m), tilavaativuus O(n).


## Suorituskyky ja O-analyysivertailu

Suorituskykytestissä huomataan, että neljästä algoritmista (Trémaux, left wall follower, dead-end filler ja leveyshaku) leveyshaku toimii kaikista nopeiten, ja sen heti sen jälkeen tulee left wall follower. Trémaux ja dead-end filler ovat huomattavasti hitaampia, varsinkin suurilla syötteillä.

## Työn mahdolliset puutteet ja parannusehdotukset

Alun perin tarkoitus oli ohjelman käynnistyksen yhteydessä se, että kerralla voi visualisoida useaa eri algoritmia. Tällä hetkellä voi ainoastaan valita
yhden algoritmin visualisoinnin, jonka jälkeen ohjelma päättyy ja se tulee käynnistää uudelleen komennolla python3 src/index.py. Tämä ongelma johtuu siitä,
että jos suoritti dead-end filler algoritmin, niin sen ensimmäinen suorittaminen kyllä onnistui kuten pitääkin, mutta tämän jälkeen minkään algoritmin visualisointi ei suostunut käynnistymään vaan labyrintti ilmestyi ruudulle, mutta mitään ei tapahtunut. Ilmeisesti ongelma johtuu siitä, että dead-end filler -algoritmin visualisoinnissa käytän kahta "agenttia" (peräisin pyamaze-moduulista). Jos suoritan algoritmeja, jotka käyttävät vain yhtä "agenttia", niin ongelmaa ei tule. Pyrin selvittämään tätä myöhemmin.
