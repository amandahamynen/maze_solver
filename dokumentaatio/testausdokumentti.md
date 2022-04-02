# Testausdokumentti

Ohjelma on tällä hetkellä automaattisesti testattavissa unittesteillä. Unittestien testikattavuus vaihtelee 95-99% välillä, kun testataan Trémauxin algoritmia. Tämä johtuu siitä, että algoritmi hyödyntää satunnaisesti valittuja reittejä risteyksissä. Jos algoritmi löytääkin oikean polun heti, niin testikattavuus on alhaisempi, sillä se ei testaa niitä kohtia koodissa, joissa algoritmi olisikin mennyt väärää reittiä ensin. Left wall follower -algoritmin testaus on tällä hetkellä vielä hieman vaiheessa.

Testit löytyvät src/tests kansiosta. Testejä varten data-kansioon on valmiiksi luotu 5x5-labyrintti. Päädyin testaamaan valmiiksi luotua labyrinttia sen vuoksi, että useassa unittestissä tulee testata, osaako ohjelma tulkita oikein tiettyä ruutua labyrintissa. Jos labyrintti generoitaisiin satunnaisesti jokaisen testauksen yhteydessä, niin tämä testaus ei onnistuisi (tai en ainakaan tiedä tähän hätään, miten sen toteuttaisin). 

## Testauskattavuus
<img width="766" alt="coverage_report_week3" src="https://user-images.githubusercontent.com/55439398/161381706-54653c1a-3f62-4ec8-bb05-7ad0a3fc5c89.png">

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
