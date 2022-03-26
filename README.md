# Maze solver

Ohjelma toteutettu kurssilla tiralabra keväällä 2022.

## Dokumentaatio
[Määrittelydokumentti](https://github.com/amandahamynen/maze_solver/blob/main/dokumentaatio/maarittelydokumentti.md)

## Viikkoraportit
[Viikkoraportti 1](https://github.com/amandahamynen/maze_solver/blob/main/dokumentaatio/viikkoraportti_1.md)

[Viikkoraportti 2](https://github.com/amandahamynen/maze_solver/blob/main/dokumentaatio/viikkoraportti_2.md)

## Käyttöohje

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

```python
source venv/bin/activate
```

4. Asenna projektin tarvitsemat kirjastot virtuaaliympäristössä komennolla

```python
pip install -r requirements.txt
```

5. Suorita ohjelma komennolla

```python
python3 src/index.py
```

Tällä hetkellä tapa, millä labyrintin kokoon voi vaikuttaa, on muokkaamalla tiedostossa index.py rivillä 15 olevan muuttujan x arvoa. Lisäksi
simuloinnin nopeutta voi säätää muokkaamalla delay-arvoa rivillä 11 (tällä hetkellä 100ms)
