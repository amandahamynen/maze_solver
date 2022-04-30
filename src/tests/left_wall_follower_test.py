import unittest
from left_wall_follower import LeftWallFollower
from pyamaze import maze
from random import randint

class TestLeftWallFollower(unittest.TestCase):
    def setUp(self):
        self.m_55 = maze(5,5)
        self.m_55.CreateMaze(loadMaze="data/maze-55.csv")
        self.f = LeftWallFollower(self.m_55, 5)

        koko = randint(10,50)
        self.satunnainen = maze(koko,koko)
        self.satunnainen.CreateMaze()
        self.wallfollower = LeftWallFollower(self.satunnainen, koko)

    def test_palauttaa_oikean_tiedon_vasemmasta_seinasta_kun_katse_E(self):
        self.f.katseen_suunta = 'E'
        self.f.nykyinen_ruutu = [4,2]
        seina = self.f.vasen_seina(self.f.nykyinen_ruutu)
        self.assertEqual(seina, True)

    def test_palauttaa_oikean_tiedon_vasemmasta_seinasta_kun_katse_N(self):
        self.f.katseen_suunta = 'N'
        self.f.nykyinen_ruutu = [4,2]
        seina = self.f.vasen_seina(self.f.nykyinen_ruutu)
        self.assertEqual(seina, False)

    def test_palauttaa_oikean_tiedon_vasemmasta_seinasta_kun_katse_S(self):
        self.f.katseen_suunta = 'S'
        self.f.nykyinen_ruutu = [4,2]
        seina = self.f.vasen_seina(self.f.nykyinen_ruutu)
        self.assertEqual(seina, True)

    def test_palauttaa_oikean_tiedon_vasemmasta_seinasta_kun_katse_W(self):
        self.f.katseen_suunta = 'W'
        self.f.nykyinen_ruutu = [4,2]
        seina = self.f.vasen_seina(self.f.nykyinen_ruutu)
        self.assertEqual(seina, False)

    def test_palauttaa_oikean_tiedon_edessa_olevasta_seinasta_kun_katse_E(self):
        self.f.katseen_suunta = 'E'
        self.f.nykyinen_ruutu = [4,2]
        seina = self.f.seina_edessa(self.f.nykyinen_ruutu)
        self.assertEqual(seina, True)

    def test_palauttaa_oikean_tiedon_edessa_olevasta_seinasta_kun_katse_N(self):
        self.f.katseen_suunta = 'N'
        self.f.nykyinen_ruutu = [4,2]
        seina = self.f.seina_edessa(self.f.nykyinen_ruutu)
        self.assertEqual(seina, True)

    def test_palauttaa_oikean_tiedon_edessa_olevasta_kun_katse_S(self):
        self.f.katseen_suunta = 'S'
        self.f.nykyinen_ruutu = [4,2]
        seina = self.f.seina_edessa(self.f.nykyinen_ruutu)
        self.assertEqual(seina, False)

    def test_palauttaa_oikean_tiedon_edessa_olevasta_kun_katse_W(self):
        self.f.katseen_suunta = 'W'
        self.f.nykyinen_ruutu = [4,2]
        seina = self.f.seina_edessa(self.f.nykyinen_ruutu)
        self.assertEqual(seina, False)

    def test_katse_oikeassa_suunnassa_kun_kaantyy_vasemmalle_ja_ensin_katse_N(self):
        self.f.katseen_suunta = 'N'
        self.f.kaanny_vasemmalle()
        self.assertEqual(self.f.katseen_suunta, 'W')

    def test_katse_oikeassa_suunnassa_kun_kaantyy_vasemmalle_ja_ensin_katse_E(self):
        self.f.katseen_suunta = 'E'
        self.f.kaanny_vasemmalle()
        self.assertEqual(self.f.katseen_suunta, 'N')

    def test_katse_oikeassa_suunnassa_kun_kaantyy_vasemmalle_ja_ensin_katse_W(self):
        self.f.katseen_suunta = 'W'
        self.f.kaanny_vasemmalle()
        self.assertEqual(self.f.katseen_suunta, 'S')

    def test_katse_oikeassa_suunnassa_kun_kaantyy_vasemmalle_ja_ensin_katse_S(self):
        self.f.katseen_suunta = 'S'
        self.f.kaanny_vasemmalle()
        self.assertEqual(self.f.katseen_suunta, 'E')

    def test_katse_oikeassa_suunnassa_kun_kaantyy_oikealle_ja_ensin_katse_N(self):
        self.f.katseen_suunta = 'N'
        self.f.kaanny_oikealle()
        self.assertEqual(self.f.katseen_suunta, 'E')

    def test_katse_oikeassa_suunnassa_kun_kaantyy_oikealle_ja_ensin_katse_E(self):
        self.f.katseen_suunta = 'E'
        self.f.kaanny_oikealle()
        self.assertEqual(self.f.katseen_suunta, 'S')

    def test_katse_oikeassa_suunnassa_kun_kaantyy_oikealle_ja_ensin_katse_W(self):
        self.f.katseen_suunta = 'W'
        self.f.kaanny_oikealle()
        self.assertEqual(self.f.katseen_suunta, 'N')

    def test_katse_oikeassa_suunnassa_kun_kaantyy_oikealle_ja_ensin_katse_S(self):
        self.f.katseen_suunta = 'S'
        self.f.kaanny_oikealle()
        self.assertEqual(self.f.katseen_suunta, 'W')

    def test_menee_oikeaan_ruutuun_kun_katse_N(self):
        self.f.katseen_suunta = 'N'
        self.f.nykyinen_ruutu = [5,2]
        self.f.mene_eteenpain()
        self.assertEqual(self.f.nykyinen_ruutu, [4,2])

    def test_menee_oikeaan_ruutuun_kun_katse_E(self):
        self.f.katseen_suunta = 'E'
        self.f.nykyinen_ruutu = [4,1]
        self.f.mene_eteenpain()
        self.assertEqual(self.f.nykyinen_ruutu, [4,2])

    def test_menee_oikeaan_ruutuun_kun_katse_W(self):
        self.f.katseen_suunta = 'W'
        self.f.nykyinen_ruutu = [4,2]
        self.f.mene_eteenpain()
        self.assertEqual(self.f.nykyinen_ruutu, [4,1])

    def test_menee_oikeaan_ruutuun_kun_katse_S(self):
        self.f.katseen_suunta = 'S'
        self.f.nykyinen_ruutu = [4,2]
        self.f.mene_eteenpain()
        self.assertEqual(self.f.nykyinen_ruutu, [5,2])

    def test_algoritmi_loytaa_maalin(self):
        self.f.maali_loytynyt = False
        self.f.wall_follower()
        self.assertEqual(self.f.maali_loytynyt, True)

    def test_algoritmi_loytaa_maalin_satunnaisessa_labyrintissa(self):
        self.wallfollower.maali_loytynyt = False
        self.wallfollower.wall_follower()
        self.assertEqual(self.wallfollower.maali_loytynyt, True)