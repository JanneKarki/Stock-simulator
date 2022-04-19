# ChangeLog

**Viikko 3**

Alustava versio luotu

Käyttäjä voi: 
- valita alkupääoman
- ostaa osakkeita syöttämällä osakkeen symbolin ja määrän
- myydä ostamiaan osakkeita
- katsoa portfolion

Testit testaa käyttäjän luomisen ja osakkeen oston, pääoman muuttumisen ja osakkeen siirtymisen portfolioon

Toistaiseksi sovellus vielä kaatuu jos symbolia ei löydy. Kotimaisia osakkeita on saatavilla huonosti.

**Viikko 4**

- Sovelluksen tiedot tallentuvat nyt pysyvästi tietokantaan, joka on suurin muutos.
- Investor luokka poistui, koska jäi turhaksi tietokantaoperaatioista vastaavien luokkien stock_repository ja user_repository sekä user jälkeen.
- Portfolio-luokka poistui ja toiminnot siirtyivä actions luokan alle, koska vaikutti toimivammalta ratkaisulta
- laskee nyt tietokannasta kokonaistuoton, ja lajittelee osakkeet erilliseen listaan tuoton mukaiseen järjestykseen
- uusia asioita on sisään kirjautuminen, valikko jossa voi valita kirjautuuko vai luo uuden käyttäjän, sekä päänäkymässä sisään kirjautuneen käyttäjän näyttäminen
- Sisäänkirjautuminen toimii, mutta salasanan voi olla mitä vain koska, sen tarkistus ei vielä toimi.
- 

**Viikko 5**
- Action-luokasta eriytettiin UserServices- ja PortfolioServices-luokat. UserServices vastaa nyt kaikista käyttäjiin liittyvistä toiminnoista ja PortfolioServices vastaa osakesalkkuun liittyvistä tuoton laskuista. Action-luokan nimi muutettu -> StockActions, johon jäivät osakkeiden osto, myynti, sekä yritysinfo.
- Sisään kirjautuminen ja tunnuksen luominen toimivat nyt salasanan kanssa
- Graafisen liittymän alustava runko rakennettu, mutta itse sovellus toimii vielä tekstikäyttöliittymällä
- Sovellus näyttää nyt sisäänkirjautuneen käyttäjän, vapaan pääoman määrän, portfolion arvon, nettotuoton, kokonaispääoman ja portfoliossa olevien osakkeiden rank-list:n
- Enter päivittää hinnat(pörssin ollessa kiinni hinnat eivät muutu)
- Testien suorittaminen tapahtuu nyt testitietokannassa eikä siten nollaa käyttäjiä testatessa

