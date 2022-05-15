# Testausdokumentti

Ohjelma on tällä hetkellä automaattisesti testattavissa unittesteillä. Unittestien testikattavuus vaihtelee 95-99% välillä, kun testataan Trémauxin algoritmia. Tämä johtuu siitä, että algoritmi hyödyntää satunnaisesti valittuja reittejä risteyksissä. Jos algoritmi löytääkin oikean polun heti, niin testikattavuus on alhaisempi, sillä se ei testaa niitä kohtia koodissa, joissa algoritmi olisikin mennyt väärää reittiä ensin.

Testit löytyvät src/tests kansiosta. Testejä varten data-kansioon on valmiiksi luotu 5x5-labyrintti. Päädyin testaamaan valmiiksi luotua labyrinttia sen vuoksi, että useassa unittestissä tulee testata, osaako ohjelma tulkita oikein tiettyä ruutua labyrintissa. Jos labyrintti generoitaisiin satunnaisesti jokaisen testauksen yhteydessä, niin tämä testaus ei onnistuisi. Lisäksi jokaisen algoritmin kohdalla nyt testataan, että löydetäänkö satunnaisen kokoisessa (kooksi asetetaan satunnainen kokonaisluku välillä 10-50) labyrintissä reitti lähtöruudusta maaliin. 

Suorituskykytestaus toimii komennolla python3 src/suorituskykytestaus.py. Tällä hetkellä tapa testata suorituskykyä on antamalla haluama labyrintin koko,
jonka jälkeen jokaisen algoritmin suoritusnopeus mitataan samassa, satunnaisesti generoidussa, labyrintissa. Tulokset tulostuvat komentoriville, ja
suoritusnopeus ilmoitetaan sekunteina. Huomattavaa on, että labyrintin generoimisessa myös kestää jonkin aikaa varsinkin suurilla syötteillä (labyrintin
kooksi valittu > 5000), joten lisäsin tulostukseen tähän kuluvan ajan. Labyrinttien generoiminen tapahtuu python-moduulin Pyamaze avulla.

## Millaisilla syötteillä suorituskykytestaus tehtiin

Tällä hetkellä on testattu algoritmien toiminta 10x10, 100x100, 500x500, 1000x1000, 2000x2000 ja 5000x5000 labyrinteissä. Suurimmilla syötteillä labyrintin
generoimisessa kestää pitkä aika, joten en ole näitä testejä vielä tehnyt. Alla taulukko tuloksista.

| Labyrintin koko | Trémaux    | Left Wall Follower | Dead-End Filler | Leveyshaku |
|-----------------|------------|--------------------|-----------------|------------|
| 10 x 10         | 0.0003530s | 0.0008380s         | 0.0003199s      | 0.0000072s |
| 100 x 100       | 0.0074510s | 0.0000131s         | 0.0059859s      | 0.0000041s |
| 500 x 500       | 0.0730552s | 0.0000141s         | 0.0696218s      | 0.0000038s |
| 1000 x 1000     | 0.3268811s | 0.0000200s         | 0.3237721s      | 0.0000100s |
| 2000 x 2000     | 1.6663661s | 0.0000147s         | 1.6293396s      | 0.0000193s |
| 5000 x 5000     | 14.601413s | 0.0007209s         | 16.522065s      | 0.0003058s |


![tiralabra](https://user-images.githubusercontent.com/55439398/168474945-fdc63f69-eda1-4c58-9e68-754943605028.png)


## Testauskattavuus

<img width="817" alt="coverage_report_week6" src="https://user-images.githubusercontent.com/55439398/166112744-cdc9a05b-1ee2-4aec-bd3f-266a476151bd.png">


## Miten testata unittestit omalla koneella

Kun olet projektin virtuaaliympäristössä, testikattavuuden kerääminen onnistuu komennolla
```python
coverage run --branch -m pytest src
```

Komennon suorittamisen jälkeen kattavuusraportin voi muodostaa komennolla 
```python
coverage html
```

Komennon suorittaminen luo projektin juurihakemistoon hakemiston htmlcov. Avaamalla hakemiston tiedoston index.html selaimessa aukeaa testikattavuusraportti.

## Miten suorittaa suorituskykytestaus

Kun olet projektin virtuaaliympäristössä, suorituskykytestaus onnistuu komennolla
```python
python3 src/suorituskykytestaus.py
```

Komennon suorittamisen jälkeen tulee syöttää labyrintin koko antamalla yksi kokonaislukuarvo.

Suorituskykytestien toisto onnistuu käynnistämällä suorituskykytestaus edellä mainitulla tavalla ja syöttämällä eri arvoja labyrintin kooksi.
