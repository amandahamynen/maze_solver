# Maze solver

![GitHub Actions](https://github.com/amandahamynen/maze_solver/workflows/CI/badge.svg)

Ohjelma toteutettu kurssilla tiralabra keväällä 2022.


## Dokumentaatio
[Määrittelydokumentti](https://github.com/amandahamynen/maze_solver/blob/main/dokumentaatio/maarittelydokumentti.md)

[Testausdokumentti](https://github.com/amandahamynen/maze_solver/blob/main/dokumentaatio/testausdokumentti.md)

[Toteutusraportti](https://github.com/amandahamynen/maze_solver/blob/main/dokumentaatio/toteutusraportti.md)

[Käyttöohje](https://github.com/amandahamynen/maze_solver/blob/main/dokumentaatio/kayttoohje.md)

## Viikkoraportit
[Viikkoraportti 1](https://github.com/amandahamynen/maze_solver/blob/main/dokumentaatio/viikkoraportti_1.md)

[Viikkoraportti 2](https://github.com/amandahamynen/maze_solver/blob/main/dokumentaatio/viikkoraportti_2.md)

[Viikkoraportti 3](https://github.com/amandahamynen/maze_solver/blob/main/dokumentaatio/viikkoraportti_3.md)

[Viikkoraportti 4](https://github.com/amandahamynen/maze_solver/blob/main/dokumentaatio/viikkoraportti_4.md)

[Viikkoraportti 5](https://github.com/amandahamynen/maze_solver/blob/main/dokumentaatio/viikkoraportti_5.md)

[Viikkoraportti 6](https://github.com/amandahamynen/maze_solver/blob/main/dokumentaatio/viikkoraportti_6.md)

## Testikattavuus

[Viikko 2](https://github.com/amandahamynen/maze_solver/blob/main/dokumentaatio/coverage_report_week2.png)

[Viikko 3](https://github.com/amandahamynen/maze_solver/blob/main/dokumentaatio/coverage_report_week3.png)

[Viikko 4](https://github.com/amandahamynen/maze_solver/blob/main/dokumentaatio/coverage_report_week4.png)

[Viikko 5](https://github.com/amandahamynen/maze_solver/blob/main/dokumentaatio/coverage_report_week5.png)

[Viikko 6](https://github.com/amandahamynen/maze_solver/blob/main/dokumentaatio/coverage_report_week6.png)

## Asennusohje

HUOM. Jotta projekti toimisi Linuxilla, katso [issue 3](https://github.com/amandahamynen/maze_solver/issues/3). MacOs ja Windows 10 kaikki vaikuttaa toimivan.


Projekti on tehty pythonin versiolla 3.8.10. Muilla python versioilla projektin toimivuutta ei ole taattu. 

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

## Muuta

En suosittele yrittämään visualisoimaan labyrintteja, joiden koko on yli 100x100, sillä niiden alustaminen kestää jonkin aikaa. Samoin suorituskykytestaus hidastuu selvästi, kun yritetään testata yli 2000x2000 labyrinttejä.

Suorituskykytestit voi suorittaa komennolla

```python
python3 src/suorituskykytestaus.py
```

Tällä hetkellä ohjelmassa on mitä luultavimmin bugeja, mitkä tulevat esiin virheellisillä syötteillä. Nämä korjataan myöhemmin.
