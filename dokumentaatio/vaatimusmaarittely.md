# Stock-Simulator

## Vaatimusmäärittely

Sovelluksen idea on simuloida osakkeisiin sijoittamista haluamansa suuruisella pääomalla reaaliaikaisilla hinnoilla. 
Osakkeiden hinta- ja yritystiedot sovellukselle tulevat yfinance-moduulista. Sovelluksella on graafinen käyttöliittymä.

## Käyttäjät

Sovelluksella on ainoastaan yksi käyttäjärooli.

## Käyttöliittymä

Sovellus koostuu neljästä eri näkymästä:
- LoginView -kirjautumisnäkymä
- CreateUserView -tunnuksenluontinäkymä
- ActionView -osakkeiden osto/myynti/info-näkymä
- PortfolioView -portfolion tarkastelunäkymä


## Sovelluksen toiminnallisuus:

**Sovelluksessa käyttäjä voi:**


- Luoda käyttäjätilin ja valita haluamansa suuruisen pääoman
    - Käyttäjätunnusksen tulee olla uniikki.
    - Syötteet eivät voi olla tyhjiä ja pääoman tulee olla numeerinen.
- Kirjautua sovellukseen
    - Jos salasana on väärin tai tunnusta ei löydy kirjautuminen ei onnistu.
- Hakea osakkeen hinnan symbolin avulla
    - Mikäli symbolia ei löydy sovellus ilmoittaa siitä
- Ostaa osakkeita osakesalkkuunsa, jolloin pääoma pienenee ostoksen verran.
    -  Mikäli symbolia ei löydy sovellus ilmoittaa siitä
    - Jos pääoma ei riitä ostokseen, ostaminen ei onnistu ja sovellus ilmoittaa siitä

- Myydä ostamiaan osakkeita, jolloin pääoma kasvaa osakkeiden hinnasta muodostuvan summan verran
    - Mikäli jokin syöte on tyhjä/virheellinen tai symbolia ei löydy sovellus ilmoittaa siitä
    - Myytävien osakkeiden määrän syöte ei voi olla suurempi kuin omistettavien osakkeiden määrä. 
- Hakea yrityksen esittelytiedot osakkeen symbolin avulla
    - Mikäli symbolia ei löydy sovellus ilmoittaa siitä
- Tarkastella osakesalkkua ja sen kehittymistä. Nähtävissä on:
    - Omistuksessa olevat osakkeet, niiden määrä ja keskimääräinen hankinta hinta
    - Osakkeet järjestettynä tuoton mukaiseen suurusjärjestykseen
    - Osakesalkun kokonaistuotto/-tappio
    - Avoin pääoma
    - Kokonaisoääoma
    


**Laajennusideoita:**

- osakkeiden lyhyeksimyynti mahdollisuus
- käyttäjien ranking list
- käyttäjä näkee pörssin aukioloajat
