# Viikkoraportti 4

## Mitä olen tehnyt tällä viikolla

Ensimmäisenä tutustuin dead-end filler algoritmin toimintaan, ja lähdin sitä toteuttamaan. Päädyin käyttämään ja kopioimaan hyväksi monia samoja metodeja, joita käytin Trémauxin algoritmissa, joten itse algoritmin toteutus oli melko nopeaa. Seuraavaksi päädyin testaamaan algoritmin toimintaa, ja huomasinkin siinä bugin, mikä tapahtuu sellaisilla labyrinteissä, joissa maaliruudun vieressä oleva ruutu on umpikuja. Tämä korjaantui kohtalaisen vaivattomasti lisäämällä muutama rivi koodia algoritmiin. Tämän jälkeen lähdin toteuttamaan komentirivillä toimivaa käyttöliittymää. Aluksi toteutin käyttöliittymän siten, että samalla suorituskerralla voi simuloida useamman algoritmin toiminnan. Kuitenkin suoritus kaatuu, jos yrittää visualisoida mitä tahansa sen jälkeen, kun on ensimmäisen kerran visualisoinnut dead-end filler -algoritmia. Tästä kirjoitin lisää toteutusraportissa. Päädyin siten tekemään käyttöliittymästä todella yksinkertaisen ja sen avulla voi suorittaa yhden algoritmin visualisoinnin kerralla ja tämän jälkeen ohjelma pitää käynnistää uudelleen komennolla python3 src/index.py. Tämän jälkeen tein unittestit (todella laiskasti, parantelen näitä myöhemmin) ja lähdin miettimään suorityskykytestausta.

## Mitä opin, mikä jäi epäselväksi ja mitä teen seuraavaksi?

## Työaika

Keskiviikko 6.4.2022: 4h

Perjantai 8.4.2022: 2h

Lauantai 9.4.2022: 3h
