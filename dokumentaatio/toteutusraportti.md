# Toteustusraportti

## Ohjelman yleisrakenne

Ohjelma käynnistyy suorittamalla tiedosto index.py, joka tekee tarvittavat alustukset ja käynnistää app.py tiedoston.

Luokat
- IO, tiedostossa index.py. Huolehtii esimerkiksi io-kirjoittamisesta ja tulostuksesta.
- App, tiedostossa app.py. Sisältää ohjelman käyttöliittymän. Luokka kutsuu luokkia Tremaux, LeftWallFollower ja DeadEndFiller tarvittaessa.
- Tremaux, tiedostossa tremaux.py. Sisältää algoritmin toteutuksen, jolla labyrintistä löydetään maali noudattaen Trémauxin algoritmia. Luokassa lisäksi useampi apumetodi algoritmin toteutusta varten.
- LeftWallFollower, tiedostossa left_wall_follower.py. Sisältää algoritmin toteutuksen, jolla labyrintistä löydetään maali noudattaen Left Wall Follower algoritmia. Luokassa lisäksi useampi apumetodi algoritmin toteutusta varten.
- DeadEndFiller, tiedostossa dead_end_filler.py. Sisältää algoritmin toteutuksen, jolla labyrintistä löydetään maali noudattaen Dead-End Filler algoritmia. Luokassa lisäksi useampi apumetodi algoritmin toteutusta varten.
- Lisäksi luokat, joilla testataan jokaista algoritmia.

## Työn mahdolliset puutteet ja parannusehdotukset

Alun perin tarkoitus oli ohjelman käynnistyksen yhteydessä se, että kerralla voi visualisoida useaa eri algoritmia. Tällä hetkellä voi ainoastaan valita
yhden algoritmin visualisoinnin, jonka jälkeen ohjelma päättyy ja se tulee käynnistää uudelleen komennolla python3 src/index.py. Tämä ongelma johtuu siitä,
että jos suoritti dead-end filler algoritmin, niin sen ensimmäinen suorittaminen kyllä onnistui kuten pitääkin, mutta tämän jälkeen minkään algoritmin visualisointi ei suostunut käynnistymään vaan labyrintti ilmestyi ruudulle, mutta mitään ei tapahtunut. Ilmeisesti ongelma johtuu siitä, että dead-end filler -algoritmin visualisoinnissa käytän kahta "agenttia" (peräisin pyamaze-moduulista). Jos suoritan algoritmeja, jotka käyttävät vain yhtä "agenttia", niin ongelmaa ei tule. Pyrin selvittämään tätä myöhemmin.
