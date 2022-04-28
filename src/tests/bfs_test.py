import unittest
from bfs import Leveyshaku
from pyamaze import maze

class TestLeveyshaku(unittest.TestCase):
    def setUp(self):
        self.m_55 = maze(5,5)
        self.m_55.CreateMaze(loadMaze="data/maze-55.csv")
        self.b = Leveyshaku(self.m_55, 5)

    def test_loytaa_maaliin(self):
        maali_loytynyt = False
        self.b.BFS()
        if self.b.maali in self.b.kayty:
            maali_loytynyt = True
        self.assertEqual(maali_loytynyt, True)