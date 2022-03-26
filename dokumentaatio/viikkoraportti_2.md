# Viikkoraportti 2

## Mitä olen tehnyt tällä viikolla

Viikon aluksi sain tietää, että alkuperäinen suunnitelma bfs vs a* ei käy, joten olin yhteydessä ohjaajaan ja sain selvyyden asiaan. Päädyin siten etsimään
kaksi uutta algoritmia, ja päädyin Trémauxin algoritmiin ja joko wall follower-algoritmiin tai dead-end filling-algoritmiin. Yhden päivän käytin Trémauxin
algoritmin tutustumiseen, ja sen toiminnan hahmotteluun kynällä ja paperilla. Tämän jälkeen lähdin miettiään, miten toteutan sen pythonilla. Seuraavana
päivänä lähdin toteuttamaan algoritmia pythonilla, ja innostuinkin tämän toteuttamisesta niin paljon, etten halunnut lopettaa ennen kuin sain toimivan
ohjelman! Seuraavana päivänä lisäsin ohjelmistotekniikan kurssin materiaalin ohjeiden mukaisen docstring-dokumentaation luokalle. Tämän jälkeen lähdin
testejä, jotka jälkikäteen mietittynä olisi ollut järkevä lisätä algoritmin rakentamisen yhteydessä (...). Lisäksi lauantaina yritin saada testikattavuuden
toimimaan codecovin kautta, mutta github actions tuottaa tällä hetkellä ongelmia tkinterin kanssa. Testikattavuus on nähtävillä [tästä](https://github.com/amandahamynen/maze_solver/blob/main/dokumentaatio/coverage_report_week2.png). Pylint (koodin laatutarkistus) nähtävillä github actionsissa.

## Mitä opin, mikä jäi epäselväksi ja mitä teen seuraavaksi?

Opin esimerkiksi sen, että Trémauxin algoritmi on myöhemmin kehittynyt syvyyshauksi. Tällä hetkellä, jos haluaa simuloida algoritmin toimintaa esim. 100 x 100 -labyrintissa, niin
ohjelmassa kestää jonkin aikaa, ennen kuin se lähtee suorittamaan. En ole täysin varma, onko algoritmissani jotain, mikä hidastaa sitä tarpeettoman paljon,
vai onko kyse siitä, että Trémauxin algoritmi on ilmeisesti aikavaativuudeltaan O(n^k), jolloin isoilla syötteillä se on vain hidas. Pienimmillä syötteilla,
kuten 50 x 50 labyrintissa, ohjelma toimii moitteetta. Lisäksi en ole aivan 100% varma, että käyhän wall follower tai dead-end filling vertailtavaksi 
algoritmiksi. Toivoisin, että tähän saisin varmistuksen labtoolin palautteessa! Seuraavaksi alan toteuttaa labtoolin palautteen perusteella 
seuraavaa algoritmia.

## Työaika
Tiistai 22.3.2022: 4h

Keskiviikko 23.3.2022: 6h

Torstai 24.3.2022 2h

Perjantai 25.3.2022: 2h

Lauantai 26.3.2022: 2h
