# Käyttöohje

Lataa viimeisimmän [releasen](https://github.com/JanneKarki/ot-harjoitustyo/releases/tag/Loppupalautus) lähdekoodi valitsemalla Assets-osion alta Source code.

## Konfigurointi

Tietokantatiedosto tallentuu _data_-hakemistoon ja sen nimeä voi halutessaan konfiguroida käynnistyshakemiston .env-tiedostossa. Tiedoston muoto on seuraava:
```bash
DATABASE_FILENAME=database.sqlite
```

## Ohjelman käynnistäminen

Ennen sovelluksen käynnistämistä, suorita komentoriviltä ot-harjoitustyo-hakemistossa seuraavat komennot:

1. Asenna sovelluksen tarvitsemat riippuvuudet komennolla:
```bash
poetry install
```
2. Suorita alustustoimet ennen sovelluksen käynnistämistä komennolla:
```bash
poetry run invoke build
```
3. Käynnistä sovellus komennoilla:

```bash
poetry run invoke start
```

## Kirjautuminen

Kirjaudu sisään antamalla käyttäjätunnus, salasana ja paina "Login".


![](./kuvat/kayttoohjeen_kuvat/login_user_view.png)

## Tunnuksen luominen
Uuden tunnukset pääset luomaan painamalla alkunäkymästä "New user". Syötä käyttäjänimi, salasana, sekä valitsemasi pääoman määrä. Käyttäjän luonti tapahtuu "Create"-näppäimestä. Jos haluat peruuttaa tunnuksen luonnin ja siirtyä takaisin kirjautumisnäkymään onnistuu se näppäimestä "Back". 

![](./kuvat/kayttoohjeen_kuvat/create_user_view.png)

Onnistuneesta tunnuksen luomisesta ilmoittaa uusi avautuu ikkuna.

![](./kuvat/kayttoohjeen_kuvat/User_created_ok.png)

"Ok"- näppäin siirtää takaisin sovelluksen kirjautumisnäkymään.


## Osakkeen hinnan ja yritystietojen hakeminen

Osakkeen hinnan saat syöttämällä osakkeen symbolin "Symbol:"-kenttään ja painamalla "Get Price". Osakkeen hinta ja -nimi tulostuvat ikkunan yläriville. Yrityken tiedot saat esiin "Get Info"- näppäimestä. Tiedot tulostuvat ikkunan alaosassa olevaan tekstikenttään. Ikkunan alareunassa on linkki yahoofinance-nettisivulle, josta voi etsiä osakkeita ja niiden tunnuksia.

![](./kuvat/kayttoohjeen_kuvat/action_view.png)


Portfoliossa olevia osakkeita pääsee tarkastelemaan "Portfolio"- näppäimestä. Käyttäjän voi kirjata ulos sovelluksesta "Logout"-näppäimellä.
  
## Osakkeen ostaminen ja myyminen

Osakkeen ostaminen ja myyminen sovelluksella on helppoa. Syötä osakkeen tunnus "Symbol"-kenttään ja haluamasi määrä "Amount"- kenttään ja paina "Buy" ostaaksesi ja "Sell"-myydäksesi osaketta. Sovellus hakee aina viimeisimmän hinnan osakkeelle toimeksiannon yhteydessä. 

![](./kuvat/kayttoohjeen_kuvat/buy_view.png)

Onnistuneesta myynti- ja ostotapahtumasta avautuu siitä ilmoittava ikkuna.


![](./kuvat/kayttoohjeen_kuvat/success_view.png)

"OK"-näppäin sulkee avautuneen ikkunan.


## Portfolion tarkastelu

Portfolio näkymässä, vasemmanpuoleisessa "Portfolio"- listassa näkyvät osakkeiden määrät ja niiden keskimääräiset hankintahinnat. Oikean puoleisessa "Rank List"- listassa osakkeet ovat lajiteltuna tuoton mukaiseen järjestykseen, ylimpänä eniten tuottanut ja alimpana eniten tappiolla oleva. Näkymässä näkyvät myös portfolion arvo, omistusten nettotuotto, vapaan pääoman määrä, kokonaispääoma, aloituspääoma, sekä nettotulos. Takaisin päänäkymään pääset "Back"- näppäimestä.

  
![](./kuvat/kayttoohjeen_kuvat/portfolio_view3.png)




