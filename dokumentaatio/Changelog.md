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

- Sovelluksen tiedot tallentuvat nyt tietokantaan, joka on suurin muutos, mutta ei näkyvä.
- Investor luokka poistui, koska jäi turhaksi tietokantaoperaatioista vastaavien luokkien stock_repository ja user_repository sekä user jälkeen.
- Portfolio-luokka poistui ja toiminnot siirtyivä actions luokan alle, koska vaikutti toimivammalta ratkaisulta
- laskee nyt tietokannasta kokonaistuoton, kokonaispääoman ja lajittelee osakkeet erilliseen listaan tuoton mukaan
- näkyvä uusi asia kokonaispääoma
- Sisäänkirjautuminen ei vielä toimi
- 

