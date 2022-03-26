import unittest
from tremaux import Tremaux
from pyamaze import maze

class TestTremaux(unittest.TestCase):
    def setUp(self):
        self.m_55 = maze(5,5)
        self.m_55.CreateMaze(loadMaze="data/maze-55.csv")
        self.t = Tremaux(self.m_55, 5)

    def test_luo_ruudukon_jossa_oikea_maara_avaimia(self):
        n = 5
        ruudukko = self.t.luo_ruudukko(n)
        self.assertEqual(len(ruudukko), 49)

    def test_laskee_seinien_maaran_oikein_kun_seinia_N_E(self):
        ruutu = (3,3)
        seinien_lkm = self.t.laske_naapuriruudut(ruutu, 0)
        self.assertEqual(seinien_lkm, 2)

    def test_laskee_seinien_maaran_oikein_kun_seinia_E_W(self):
        ruutu = (3,5)
        seinien_lkm = self.t.laske_naapuriruudut(ruutu, 0)
        self.assertEqual(seinien_lkm, 2)
    
    def test_laskee_avointen_seinien_maaran_oikein_kun_avoimia_E_W_S(self):
        ruutu = (2,4)
        avointen_seinien_lkm = self.t.laske_naapuriruudut(ruutu, 1)
        self.assertEqual(avointen_seinien_lkm, 3)

    def test_laskee_avointen_seinien_maaran_oikein_kun_avoimia_N(self):
        ruutu = (5,1)
        avointen_seinien_lkm = self.t.laske_naapuriruudut(ruutu, 1)
        self.assertEqual(avointen_seinien_lkm, 1)

    def test_palauttaa_oikean_maaran_mahdollisia_liikkeita_kun_voi_liikkua_N_W(self):
        ruutu = (5,5)
        mahdolliset = self.t.mahdolliset_liikkeet(ruutu)
        self.assertAlmostEqual(len(mahdolliset), 2)

    def test_palauttaa_oikean_maaran_mahdollisia_liikkeita_kun_voi_liikkua_E_S(self):
        ruutu = (1,2)
        mahdolliset = self.t.mahdolliset_liikkeet(ruutu)
        self.assertAlmostEqual(len(mahdolliset), 2)

    def test_algoritmi_palauttaa_listan_jonka_ensimmainen_alkio_on_lahtoruutu_ja_viimeinen_maali(self):
        reitti = self.t.tremaux()
        viimeinen_indeksi = len(reitti) - 1
        self.assertAlmostEqual(reitti[0], (5,5))
        self.assertAlmostEqual(reitti[viimeinen_indeksi], (1,1))