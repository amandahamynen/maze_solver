# Toteustusraportti

## Ohjelman yleisrakenne

## Työn mahdolliset puutteet ja parannusehdotukset

Alun perin tarkoitus oli ohjelman käynnistyksen yhteydessä se, että kerralla voi visualisoida useaa eri algoritmia. Tällä hetkellä voi ainoastaan valita
yhden algoritmin visualisoinnin, jonka jälkeen ohjelma päättyy ja se tulee käynnistää uudelleen komennolla python3 src/index.py. Tämä ongelma johtuu siitä,
että jos suoritti dead-end filler algoritmin, niin sen ensimmäinen suorittaminen kyllä onnistui kuten pitääkin, mutta tämän jälkeen minkään algoritmin visualisointi ei suostunut käynnistymään vaan labyrintti ilmestyi ruudulle, mutta mitään ei tapahtunut. Ilmeisesti ongelma johtuu siitä, että dead-end filler -algoritmin visualisoinnissa käytän kahta "agenttia" (peräisin pyamaze-moduulista). Jos suoritan algoritmeja, jotka käyttävät vain yhtä "agenttia", niin ongelmaa ei tule. Pyrin selvittämään tätä myöhemmin.
