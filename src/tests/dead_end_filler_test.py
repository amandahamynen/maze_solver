import unittest
from dead_end_filler import DeadEndFiller
from pyamaze import maze

class TestDeadEndFiller(unittest.TestCase):
    def setUp(self):
        self.m_55 = maze(5,5)
        self.m_55.CreateMaze(loadMaze="data/maze-55.csv")
        self.d = DeadEndFiller(self.m_55, 5)

    def test_loytaa_kaikki_umpikujat(self):
        self.d.etsi_ja_merkitse_umpikujat()
        self.assertEqual(len(self.d.umpikujat), 3)

    def test_loytaa_maaliin(self):
        self.d.maali_loytynyt = False
        self.d.dead_end_filling()
        self.assertEqual(self.d.maali_loytynyt, True)

