import unittest
from bfs import Leveyshaku
from pyamaze import maze
from random import randint

class TestLeveyshaku(unittest.TestCase):
    def setUp(self):
        self.m_55 = maze(5,5)
        self.m_55.CreateMaze(loadMaze="data/maze-55.csv")
        self.b = Leveyshaku(self.m_55, 5)

        koko = randint(10,50)
        self.satunnainen = maze(koko,koko)
        self.satunnainen.CreateMaze()
        self.leveyshaku = Leveyshaku(self.satunnainen, koko)

    def test_loytaa_maaliin_valmiiksi_maaratyssa_labyrintissa(self):
        maali_loytynyt = False
        self.b.BFS()
        if self.b.maali in self.b.kayty:
            maali_loytynyt = True
        self.assertEqual(maali_loytynyt, True)

    def test_loytaa_maaliin_satunnaisessa_labyrintissa(self):
        maali_loytynyt = False
        self.leveyshaku.BFS()
        if self.leveyshaku.maali in self.leveyshaku.kayty:
            maali_loytynyt = True
        self.assertEqual(maali_loytynyt, True)