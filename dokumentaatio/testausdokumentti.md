# Testausdokumentti

## Sovelluslogiikka

- Sovelluslogiikasta vastaavaa StockActions-luokkaa testataan TestAction-testiluokalla.
- Käyttäjjään liittyvistä toiminnoista vastaavaa UserServices-luokkaa testataan TestUserServices-testiluokalla.
- Portfolioon liittyvistä toiminnoista vastaavaa PortolioServices-luokkaa testataan TestPortfolioServices-testiluokalla.



## Repositoriot

Tietojen pysyväistallennuksesta vastaavia StockRepository ja UserRepository-luokkia testataan TestStockRepositotry ja TestUserRepository -testiluokissa. 
Testeissä käytetään erillistä testitietokantaa, joka on määritelty .env.test-konfiguraatiotiedostossa.

## Automatisoidut yksikkö- ja integraatiotestit

Käyttöliittymäkerrosta lukuunottamatta testien haarautumakattavuus on 99%.

![](./kuvat/coverage-report.png)




## Järjestelmätestaus

Kaikki [vaatimusmäärittelyn](https://github/vaatimusmaarittely.md) 
mukaiset toiminnot on testattu monipuolisesti manuaalisesti ja myös virheellisillä syötteillä.

## Asennus ja konfigurointi

Sovelluksen käyttöä on testattu Linux-ympäristössä omalla koneella, sekä yliopiston Cubbli Linux-virtuaalikoneella.

##  Sovellukseen jääneet laatuongelmat

- Mikäli internet yhteyttä ei ole eikä sovellus voi käyttää yfinance kirjastoa, sovellus ei anna siitä järkevää virheilmoiusta. Sovellus käynnistyy, mutta portfoliota ei voi silloin tarkastella. Ilmoittaa myös toimintojen yhteydessä "Symbol not found"-virheen.

- Mikäli SQLite tietokantaa ei ole alustettu, sovellus ei anna siitä järkevää virheilmoitusta.
