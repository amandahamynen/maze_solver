
# Käyttöohje

Projekti ei vaikuta toimivan tällä hetkellä Linuxilla, katso [issue](https://github.com/amandahamynen/maze_solver/issues/1). MacOs ja Windows 10 kaikki vaikuttaa toimivan.

Projekti on tehty pythonin versiolla 3.8.10. Muilla python versioilla projektin toimivuutta ei ole taattu. 

## Miten eri toiminnallisuuksia käytetään

Ohjelman käynnistettyä komennolla python3 src/index.py avautuu tekstikäyttöliittymä, jonka avulla ohjelman suoritusta voidaan hallita. 
Mahdollisuutena on valita, minkä algoritmin visualisoinnin haluaa suorittaa syötteellä 1-4, ja ohjelma on mahdollista lopettaa syötteellä 5. 
Virheellisillä syötteillä ohjelman ei tulisi kaaduta.

<img width="1440" alt="Näyttökuva 2022-4-28 kello 14 57 44" src="https://user-images.githubusercontent.com/55439398/165747918-0423040a-8fd3-49e0-b41b-2a86c68a7fb7.png">

Tämän jälkeen aukeaa Tkinter-ikkuna, jossa visualisointi tapahtuu. Ikkuna tulee itse sulkea algoritmin päätyttyä, ja tämän jälkeen komentorivillä 
näkyy kyseisen algoritmin suorituksessa kulunut aika.

<img width="1440" alt="Näyttökuva 2022-4-28 kello 14 58 13" src="https://user-images.githubusercontent.com/55439398/165747982-49f9c487-e2e0-4177-b4d4-58f2f358a9e5.png">
<img width="1440" alt="Näyttökuva 2022-4-28 kello 14 58 21" src="https://user-images.githubusercontent.com/55439398/165748005-e44495a8-2638-4dad-9ca4-10c8616e2271.png">


Suorituskykytestaus suoritetaan komennolla

```python
python3 src/suorituskykytestaus.py
```

Tämän jälkeen komentorivillä aukeaa tekstikäyttöliittymä, johon tulee syöttää halutun labyrintin koko (yksi kokonaisluku). Tämän jälkeen
suorituskykytestaus alkaa, ja komentoriville ilmestyy tähän liittyvät tiedot.

<img width="1440" alt="Näyttökuva 2022-4-28 kello 14 59 10" src="https://user-images.githubusercontent.com/55439398/165748392-98c6994e-d9d9-4310-9fed-f4f2627ccfa0.png">

## Video projektissa käytettyjen algoritmien visualisoinnista

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/ig3_0bgtnF8/maxresdefault.jpg)](https://youtu.be/ig3_0bgtnF8)


## Asennusohje

1. Lataa projekti koneellesi komennolla

```python
git clone git@github.com:amandahamynen/maze_solver.git
```

2. Siirry projektikansioon

```python
cd maze_solver
```

3. Luo itsellesi virtuaaliympäristö ja aktivoi se

```python
python3 -m venv venv
```
Linux/MacOs:

```python
source venv/bin/activate
```

Windows:

```python
venv\Scripts\activate
```

Huom. Jos tulee virhe "Running Scripts Is Disabled On This System", niin itselläni toimi seuraavan ohjeen seuraaminen:
https://www.stanleyulili.com/powershell/solution-to-running-scripts-is-disabled-on-this-system-error-on-powershell/

4. Asenna projektin tarvitsemat kirjastot virtuaaliympäristössä komennolla

```python
pip install -r requirements.txt
```

5. Suorita ohjelma komennolla

```python
python3 src/index.py
```
