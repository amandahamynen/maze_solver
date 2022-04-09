# Testausdokumentti

Ohjelma on tällä hetkellä automaattisesti testattavissa unittesteillä. Unittestien testikattavuus vaihtelee 95-99% välillä, kun testataan Trémauxin algoritmia. Tämä johtuu siitä, että algoritmi hyödyntää satunnaisesti valittuja reittejä risteyksissä. Jos algoritmi löytääkin oikean polun heti, niin testikattavuus on alhaisempi, sillä se ei testaa niitä kohtia koodissa, joissa algoritmi olisikin mennyt väärää reittiä ensin. Left wall follower -algoritmin testaus on tällä hetkellä vielä hieman vaiheessa.

Testit löytyvät src/tests kansiosta. Testejä varten data-kansioon on valmiiksi luotu 5x5-labyrintti. Päädyin testaamaan valmiiksi luotua labyrinttia sen vuoksi, että useassa unittestissä tulee testata, osaako ohjelma tulkita oikein tiettyä ruutua labyrintissa. Jos labyrintti generoitaisiin satunnaisesti jokaisen testauksen yhteydessä, niin tämä testaus ei onnistuisi (tai en ainakaan tiedä tähän hätään, miten sen toteuttaisin). 

Suorituskykytestaus toimii komennolla python3 src/suorituskykytestaus.py. Tällä hetkellä tapa testata suorituskykyä on antamalla haluama labyrintin koko,
jonka jälkeen jokaisen algoritmin suoritusnopeus mitataan samassa, satunnaisesti generoidussa, labyrintissa. Tulokset tulostuvat komentoriville, ja
suoritusnopeus ilmoitetaan sekunteina. Huomattavaa on, että labyrintin generoimisessa myös kestää jonkin aikaa varsinkin suurilla syötteillä (labyrintin
kooksi valittu > 5000), joten lisäsin tulostukseen tähän kuluvan ajan. Labyrinttien generoiminen tapahtuu python-moduulin Pyamaze avulla.

## Millaisilla syötteillä suorituskykytestaus tehtiin

Tällä hetkellä on testattu algoritmien toiminta 10x10, 100x100, 500x500, 1000x1000, 2000x2000 ja 5000x5000 labyrinteissä. Suurimmilla syötteillä labyrintin
generoimisessa kestää pitkä aika, joten en ole näitä testejä vielä tehnyt. Alla taulukko tuloksista.

| Labyrintin koko | Trémaux    | Left Wall Follower | Dead-End Filler |
|-----------------|------------|--------------------|-----------------|
| 10 x 10         | 0.0002551s | 0.0000209s         | 0.0004391s      |
| 100 x 100       | 0.0066938s | 0.0000059s         | 0.0058770s      |
| 500 x 500       | 0.0691401s | 0.0000038s         | 0.0665140s      |
| 1000 x 1000     | 0.3205120s | 0.0000166s         | 0.3154828s      |
| 2000 x 2000     | 1.5130481s | 0.0000162s         | 1.5196189s      |
| 5000 x 5000     | 11.760847s | 0.0003209s         | 13.079458s      |


## Testauskattavuus

<img width="828" alt="coverage_report_week4" src="https://user-images.githubusercontent.com/55439398/162578722-90e22d6a-3cf6-40db-98ab-160e3d457e6a.png">


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

