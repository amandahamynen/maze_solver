# Viikkoraportti 3

## Mitä olen tehnyt tällä viikolla
Tutustuin wall follower-ja dead end filling algoritmeihin. Wall followerista vaikutti mielestäni todella suoraviivaiselta ja helpolta toteuttaa, 
joten päädyin perehtymään siihen hieman tarkemmin. Tämän jälkeen lähdin ohjelmoimaan algoritmia, ja se olikin loppujen lopuksi melko vaivaton tehdä. 
Tällä hetkellä algoritmin koodi on todella toisteista, mutta mielestäni ymmärrettävää. Uskon palaavani parantelemaan tätä tulevilla viikoilla.
Seuraavana päivänä lisäsin koodiin docstringit ja tein koodille yksikkötestit. Lisäksi aloin laatimaan testausdokumenttia. Testikattavuus on nähtävillä
[tästä](https://github.com/amandahamynen/maze_solver/blob/main/dokumentaatio/coverage_report_week3.png) ja laadunseurannan voi nähdä pylintin avulla
esim. github actionsista.

## Mitä opin, mikä jäi epäselväksi ja mitä teen seuraavaksi?
Opin sen, että wall followerista on periaatteessa kaksi versiota (toinen seuraa vasenta seinää ja toinen oikeaa). Toteutin ohjelmassani niistä vain 
toisen, mutta toisen lisääminen ei pitäisi olla vaivanloista.
Epäselväksi ehkä jäi yksikkötestien toteuttaminen. Tällä hetkellä testikatettavuus on korkea (97%), mutta en ole varma, ovatko testini laadullisesti
tarpeeksi hyviä. Pohdin tätä samaa hieman alustavasti testausdokumentissa.
Seuraavaksi uskoisin toteuttavani vielä ainakin kolmannen algoritmin (dead end filling) ja lähden toteuttamaan käyttöliittymää ohjelmalle, sillä
tällä hetkellä käyttäjä joutuu itse kommentoimaan ja poistamaan kommentit niiden rivien edestä, jotka koskevat joko Trémauxin algoritmin tai
wall followerin käynnistämistä komennolla python3 src/index.py. Ajatuksena on nyt ainakin alustavasti luoda käyttöliittymä, jota hallitaan suoraan
komentoriviltä ja sen avulla voidaan generoida tietynlainen labyrintti ja valita, mitä algoritmia haluaa visualisoida.

## Työaika
Maanantai 28.3.2022: 1h

Perjantai 1.4.2022: 3h

Lauantai 2.4.2022: 2h
