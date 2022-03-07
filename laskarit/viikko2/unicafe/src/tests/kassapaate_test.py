import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(100000)
        self.tyhjakortti = Maksukortti(100)

    def test_kassan_rahamaara_on_alussa_oikein(self):
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")

    def test_edullisia_myyty_0(self):
        self.assertEqual(str(self.kassapaate.edulliset), "0")    
    
    def test_maukkaita_myyty_0(self):
        self.assertEqual(str(self.kassapaate.edulliset), "0")

#käteisosto, rahaa tarpeeksi:
    def test_edullinen_lounas_kateisosto_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(250)        
        self.assertEqual(vaihtoraha, 10 )

    def test_edullinen_lounas_kateisosto_myynti_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(str(self.kassapaate.edulliset), "1")

    def test_maukas_lounas_kateisosto_vaihtoraha_oikein(self):
        vaihtoraha =self.kassapaate.syo_maukkaasti_kateisella(410)
        self.assertEqual(vaihtoraha, 10)

    def test_maukas_lounas_kateisosto_myynti_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(410)
        self.assertEqual(str(self.kassapaate.maukkaat), "1")

#käteisosto, ei tarpeeksi rahaa:
    def test_edullinen_lounas_kateisosto_ei_tarpeeksi_rahaa_palautus_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)

    def test_edullinen_lounas_kateisosto_ei_tarpeeksi_rahaa_ei_myyntiä_tai_rahaa_kassaan(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(str(self.kassapaate.edulliset), "0")

    def test_edullinen_lounas_kateisosto_ei_tarpeeksi_rahaa_ei_rahaa_kassaan(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")


#käteinen, ei rahaa tarpeeksi, maukas lounas:
    def test_maukas_lounas_kateisosto_ei_tarpeeksi_rahaa_ei_myyntiä_tai_rahaa_kassaan(self):
        vaihtoraha =self.kassapaate.syo_maukkaasti_kateisella(350)
        self.assertEqual(vaihtoraha, 350)

    def test_maukas_lounas_kateisosto_ei_tarpeeksi_rahaa_ei_myyntiä(self):
        self.kassapaate.syo_maukkaasti_kateisella(350)
        self.assertEqual(str(self.kassapaate.maukkaat), "0")

    def test_maukas_lounas_kateisosto_ei_tarpeeksi_rahaa_ei_rahaa_kassaan(self):
        vaihtoraha =self.kassapaate.syo_maukkaasti_kateisella(350)    
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        
    
#rahaa kortilla, edullinen lounas:     
    def test_edullinen_lounas_korttiosto_rahaa_tarpeeksi_myynti_oikein(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.edulliset), "1")

    def test_edullinen_lounas_korttiosto_rahaa_tarpeeksi_kortin_saldo_oikein(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 997.6")

    def test_edullinen_lounas_korttiosto_rahaa_tarpeeksi_myyty_true(self):
        a = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(a, True)

    def test_edullinen_lounas_korttiosto_rahaa_tarpeeksi_kassan_saldo_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")


#rahaa kortilla, maukas lounas:
    def test_maukas_lounas_korttiosto_rahaa_tarpeeksi_myynti_oikein(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.maukkaat), "1")

    def test_maukas_lounas_korttiosto_rahaa_tarpeeksi_kortti_saldo_oikein(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)   
        self.assertEqual(str(self.maksukortti), "saldo: 996.0")

    def test_maukas_lounas_korttiosto_rahaa_tarpeeksi_myy_true(self):
        a = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(a, True)

    def test_maukas_lounas_korttiosto_rahaa_tarpeeksi_kassa_saldo_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")


#ei rahaa kortilla, maukas lounas:
    def test_maukas_lounas_korttiosto_ei_rahaa_tarpeeksi_kortin_saldo_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.tyhjakortti)
        self.assertEqual(str(self.tyhjakortti), "saldo: 1.0")

    def test_maukas_lounas_korttiosto_ei_rahaa_tarpeeksi_myyty_0(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.tyhjakortti)
        self.assertEqual(str(self.kassapaate.maukkaat), "0")


    def test_maukas_lounas_korttiosto_ei_rahaa_kassa_saldo_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.tyhjakortti)  
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")

    def test_maukas_lounas_korttiosto_ei_rahaa_kassa_saldo_ei_muutu(self):
        a = self.kassapaate.syo_maukkaasti_kortilla(self.tyhjakortti)
        self.assertEqual(a, False)

    
 #ei rahaa kortilla, edullinen lounas:   
    def test_edullinen_lounas_korttiosto_ei_rahaa_tarpeeksi_kortin_saldo_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.tyhjakortti)
        self.assertEqual(str(self.tyhjakortti), "saldo: 1.0")

    def test_edullinen_lounas_korttiosto_ei_rahaa_tarpeeksi_myyty_0(self):
        self.kassapaate.syo_edullisesti_kortilla(self.tyhjakortti)
        self.assertEqual(str(self.kassapaate.edulliset), "0")


    def test_edullinen_lounas_korttiosto_ei_rahaa_kassa_saldo_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.tyhjakortti)  
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")

    def test_edullinen_lounas_korttiosto_ei_rahaa_kassa_saldo_ei_muutu(self):
        a = self.kassapaate.syo_edullisesti_kortilla(self.tyhjakortti)
        self.assertEqual(a, False)


#kortin lataus:
    def test_rahan_lataus_kortille_kassan_ja_kortin_saldo_muuttuu_oikein(self):
        
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,1000)
        self.assertEqual(str(self.maksukortti), "saldo: 1010.0")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "101000")



    
        