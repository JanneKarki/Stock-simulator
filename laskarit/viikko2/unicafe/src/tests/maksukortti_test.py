import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_kortin_saldo_kasvaa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")

    def test_ota_rahaa_vahentaa_saldoa_oikein(self):
        self.maksukortti.ota_rahaa(700)
        self.assertEqual(str(self.maksukortti), "saldo: 3.0")

    def test_saldo_ei_vahene_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_ota_rahaa_palauttaa_true_jos_rahaa_on_tarpeeksi(self):
        a = self.maksukortti.ota_rahaa(200)
        self.assertEqual(a, True)