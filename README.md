# Stock-Simulator

Sovelluksella voi sijoittaa leikisti osakkeisiin reaaliaikaisilla hinnoilla. Sovelluksella on myös mahdollista hakea yrityksen esittelytietoja. Osakkeden osto, myynti ja esittelytietojen hakeminen tapahtuu osakkeen symbolin avulla, joita voi etsiä kätevästi vaikka täältä https://finance.yahoo.com/. 

**Dokumentaatio**

[Vaatimusmäärittely](https://github.com/JanneKarki/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/JanneKarki/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

[ChangeLog](https://github.com/JanneKarki/ot-harjoitustyo/blob/main/dokumentaatio/Changelog.md)

[Arkkitehtuuri](https://github.com/JanneKarki/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

[Käyttöohje](https://github.com/JanneKarki/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)

[Testausdokumentti](https://github.com/JanneKarki/ot-harjoitustyo/blob/main/dokumentaatio/testausdokumentti.md)


____________________________________________
## Releases
[Release 1 - Viikon 5 deadline](https://github.com/JanneKarki/ot-harjoitustyo/releases/Viikon5)

[Loppupalautus](https://github.com/JanneKarki/ot-harjoitustyo/releases/tag/Loppupalautus)
__________________________

## Asennus

Sovellus käyttää riippuvuuksien hallintaan poetrya, joten se tulee olla asennettuna koneelle.

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

## Testaus
Testaus voidaan suorittaa komennolla:

```bash
poetry run invoke test
```

## Testikattavuus
Testikattavuusraportin generointi tapahtuu komennolla:

```bash
poetry run invoke coverage-report
```

Raportti löytyy htmlcov-hakemistosta nimellä index.html. 

## Pylint
Pylint-tarkastukset voidaan suorittaa komennolla:

```bash
poetry run invoke lint
```

