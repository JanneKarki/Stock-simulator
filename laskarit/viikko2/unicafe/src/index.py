from maksukortti import Maksukortti
from kassapaate import Kassapaate

unicafe_exactum = Kassapaate()
kortti = Maksukortti(10000)
        
unicafe_exactum.syo_edullisesti_kortilla(kortti)
        
print(unicafe_exactum.edulliset)
print(kortti)