# Viikkoraportti 4

## Mitä olen tehnyt tällä viikolla

Ensimmäisenä tutustuin dead-end filler algoritmin toimintaan, ja lähdin sitä toteuttamaan. Päädyin käyttämään ja kopioimaan hyväksi monia samoja metodeja, joita käytin Trémauxin algoritmissa, joten itse algoritmin toteutus oli melko nopeaa. Seuraavaksi päädyin testaamaan algoritmin toimintaa, ja huomasinkin siinä bugin, mikä tapahtuu sellaisilla labyrinteissä, joissa maaliruudun vieressä oleva ruutu on umpikuja. Tämä korjaantui kohtalaisen vaivattomasti lisäämällä muutama rivi koodia algoritmiin. Tämän jälkeen lähdin toteuttamaan komentorivillä toimivaa käyttöliittymää. Aluksi toteutin käyttöliittymän siten, että samalla suorituskerralla voi simuloida useamman algoritmin toiminnan. Kuitenkin suoritus kaatuu, jos yrittää visualisoida mitä tahansa sen jälkeen, kun on ensimmäisen kerran visualisoinnut dead-end filler -algoritmia. Tästä kirjoitin lisää toteutusraportissa. Päädyin siten tekemään käyttöliittymästä todella yksinkertaisen ja sen avulla voi suorittaa yhden algoritmin visualisoinnin kerralla ja tämän jälkeen ohjelma pitää käynnistää uudelleen komennolla python3 src/index.py. Tämän jälkeen tein unittestit (todella laiskasti, parantelen näitä myöhemmin) ja lähdin miettimään suorityskykytestausta. Päädyin testaamaan tätä yksinkertaisesti mittaamalla aikaa, joka kestää suorittaa algoritmit. 

Suorituskykytestaus toimii tällä hetkellä siten, että ensin luodaan sen kokoinen labyrintti, jonka käyttäjä valitsee, ja tässä samassa labyrintissa testataan jokaisen algoritmin suoritusnopeus. Huomasin heti, että suurilla syötteillä (esim. labyrintin koko 10000x10000) suorituskykytestaus kestää mahdottoman kauan (yli 10min ja tämänkin jälkeen se olisi jatkunut, mutta pakotin ohjelman keskeyttämään). En ole varma, mitä algoritmeja python moduuli pyamaze käyttää labyrinttien generoimiseen, mutta se ei ole kovin käyttökelpoinen hyvin suurilla syötteillä. Esim 2000x2000 labyrintin generoimisessa kesti 1.8 sekuntia kun taas jo 5000x5000 labyrintissä 12.8 sekuntia. Itse algoritmien kestoista lisää löytää testausdokumentista. 


## Mitä opin, mikä jäi epäselväksi ja mitä teen seuraavaksi?

Tällä viikolla opin sen, kuinka dead-end filler algoritmi toimii. Seuraavaksi ajattelin vielä mahdollisesti tehdä leveyshakualgoritmin, sillä sen tiedetään löytävän lyhyin reitti labyrintissä. Ajattelin käyttää tätä vertailukohteena muihin toteuttamiini algoritmeihin. Lisäksi teen paremmat testit, jotka toimivat satunnaisesti generoiduissa labyrinteissä. 

## Työaika

Keskiviikko 6.4.2022: 4h

Perjantai 8.4.2022: 2h

Lauantai 9.4.2022: 4h
