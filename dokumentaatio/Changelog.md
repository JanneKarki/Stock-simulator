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
- Pakkausrakennetta parannettu
- Sisään kirjautuminen ja tunnuksen luominen toimivat nyt salasanan kanssa.
- Tekstiliittymä vaihdettu graafiseen liittymään. Näkymät ovat LoginView, CreateUserView, ActionView sekä PortoflioView.
- Tunnusta luodessa tarkistaa onko tunnus jo käytössä, onko jokin syöte tyhjä ja onko capital numeerinen. Jos jokin syöte ei ollut kelvollinen tunnuksen luonti ei onnistu. Jos syöte oli kelvollinen ja tunnus oli vapaa, aukeaa uusi ikkuna, joka kertoo onnistuneesta tunnuksen luonnista ja siinä olevasta OK näppäimestä tapahtuu paluu LoginView-näkymään.
- Sisään kirjautuessa väärällä tunnuksella ja/tai salasanalla tulostaa virhetekstin Invalid username or password.
- ActionView-näkymässä voi nyt:
  - hakea symbolin perusteella hinnan (tulostaa myös yrityksen nimen) 
  - hakea yritykesn infon
    -> info tulostuu tekstilaatikkoon 
  - ostaa/myydä osaketta 
  - siirtyä portfolio näkymään
  - kirjautua ulos
  - näkymässä näkyy myös kirjautunut käyttäjä ja vapaana oleva pääoma
 - PortfolioView- näkymässä näkyy:
    - Listaus osakkeista niiden määrästä ja hankinta hinnasta vieritettävässä tekstilaatikossa
    - Rank Listaus osakkeista ja tuotosta, tuoton mukaisessa järjestyksessä vieritettävässä tekstilaatikossa
- Testien suorittaminen tapahtuu nyt testitietokannassa eikä siten nollaa käyttäjiä testatessa


**Viikko 6**

- Nyt käyttäjätunnusta luodessa sovellus näyttää ikkunassa punaisella virheviestillä mikäli syöte on virheellinen. Nousevat virheilmoitukset ovat "Username exists", "Inputs cannot be empty" ja  "Invalid capital input".
- Tehty käyttöohje
- Arkkitehtuuriin lisätty pakkauskaavio ja pakkaus/luokkakaavio
- Virheellisellä symbolilla yrityksen infoa hakiessa tulostaa ikkunaan "Symbol not found".
- Docstringiä lisätty StockRepository, UserRepository, PortfolioServices, StockActions

**Viikko7**
- Nyt sovellus ei anna ostaa enemmän kuin on rahaa, eikä myydä enempää osakkeita kuin niitä on. Uudet nousevat virheet "StockNotInPortfolioError" ja "NotEnoughMoneyError".
- Symbol not found virheilmoituksen toimii nyt kaikilla toiminnoilla(Get Info, Get Price, Buy, Sell)

