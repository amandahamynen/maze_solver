# Viikkoraportti 5

## Mitä olen tehnyt tällä viikolla

Tällä viikolla olen toteuttanut leveyshakualgoritmin, mikä osoittautui todella helpoksi tehdä, sillä se oli jo minulle tuttu. Lisäksi tutustuin
vertaisarvioitavaan projektiin ja kirjoitin siitä vertaisarvion. Lisäksi perehdyin omaan saamaani vertaisarvioon. Saamassani vertaisarvioinnissa ilmeni
todella tärkeä asia, nimittäin yrittäessä asentaa projektin tarvitsemia kirjastoja (ilmeisesti linuxilla) tulee errori. Tätä selvitellessä meni pidemmän
aikaa, eikä sen syy ole vielä selvillä. Itse testasin ja projekti toimii kuten pitääkin MacOs ja Windows 10 käyttöjärjestelmillä (windowsilla virtuaaliympäristön
aktivoiminen ei toimi aivan kuten READMEssä on mainittu, mutta nopeasti googlettamalla sen sai toimimaan). Linuxilla ongelma vaikuttaa jollain tavalla ehkä
liittyvän setuptools-kirjastoon, selvittelen tätä ongelmaa piakkoin. Tämän vuoksi (ja oman huonon aikatauluttamisen takia...) en tällä viikolla saanut
yhtä paljon aikaiseksi, kuin olen saanut edellisillä viikoilla. Esimerkiksi testejä en ole kerennyt tekemään/parantelemaan, vaikka niin oli alun perin tarkoitus.
Dokumentaatiota sain hieman edistettyä.

## Mitä opin, mitä jäi epäselväksi ja mitä teen seuraavaksi?
Opin, ettei projektini 100% varmuudella toimikaan ilmeisesti ainakaan linuxilla. Toivoisin saavani varmistuksen labtoolin palautteessa, että 
toimiiko projekti kuten pitää vai onko siinä toisiaankin ongelma. Seuraavaksi alan tekemään testejä ja koitan selvitellä edellä mainittua ongelmaa. 

EDIT. Testasin VMware Horizonin avulla Cubbli Linux 18, ja ongelma vaikuttaa korjaantuvan, jos käyttää komentoa pip install wheel ennen komentoa pip install -r requirements.txt. Toisaalta itse visualisointi ei näytä toimivan, sillä tkinter ikkuna on tyhjä (kuva alla). En ole varma, mistä ongelma johtuu.

<img width="666" alt="Näyttökuva 2022-4-23 kello 21 59 53" src="https://user-images.githubusercontent.com/55439398/164942730-2f2b8194-e1f0-4a22-a196-2d7ce772f354.png">


## Työaika
Perjantai 22.4.2022: 3h

Lauantai 23.4.2022: 4h
