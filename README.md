# flugbetrieb-metzingen
Daten Sammlung und Analyse

[TOC]

## Sondertage

| Tag | Bemerkung |
|---------:|-----------------------------------------|
|      17.03.| Gutes Wetter, 2 Piloten mit gelb angemeldet [Screenshot von Akos](https://photos.app.goo.gl/czVUtiKxn8uRpdnp6) |
|      21.04.| Kräftiger Wind, 4 Starts. Ohne Dienstplan hätten wir wahrscheinlich kein Betrieb. |
|27. & 28.04.| Am 27.04. (Samstag) hätten wir wahrscheinlich fliegen können, es gab Freitag noch gar keine Anmeldungen. Für Sonntag wurde mehr Wind vorhergesagt. |
|      11.05.| Windenseminar mit Ines |
|25. & 26.05.| Pilotinnentreff |
|07. & 08.09.| Beiden Tagen hätten fliegbar gewesen, Pilotenmangel. |
|      29.09.| Schönes Wetter, ohne Dienstplan hätten wir wahrscheinlich anderswo geflogen. |

## Statistik 

![Auswertung der Schlepps](./schlepps-2024.svg)


Flugtage im DHV XC bzw Xcontest ab 2017 aus dem [notebook](./flight_days_checks.ipynb)

| Jahr   | Montag | Dienstag | Mittwoch | Donnerstag | Freitag | Samstag | Sonntag |  Total |
|:-------|------------------------:|-------------------------:|---------------------------:|--------------------------:|------------------------:|--------------------------:|------------------------:|----------------:|
| 2017   |                       1 |                        0 |                          0 |                         2 |                       2 |                         7 |                      13 |              25 |
| 2018   |                       2 |                        1 |                          0 |                         0 |                       8 |                         8 |                      14 |              33 |
| 2019   |                       1 |                        0 |                          1 |                         2 |                       3 |                         6 |                       9 |              22 |
| 2020   |                       1 |                        1 |                          3 |                         3 |                       1 |                         6 |                       2 |              17 |
| 2021   |                       0 |                        1 |                          0 |                         1 |                       0 |                         6 |                       7 |              15 |
| 2022   |                       1 |                        0 |                          0 |                         0 |                       2 |                         3 |                       5 |              11 |
| 2023   |                       0 |                        0 |                          1 |                         1 |                       3 |                         7 |                       8 |              20 |
| 2024   |                       3 |                        2 |                          1 |                         2 |                       1 |                         8 |                       8 |              25 |
| Total    |                       9 |                        5 |                          6 |                        10 |                      20 |                        50 |                      65 |             165 |




### Mangelperioden

* COVID-Verbot
* Kella-Winde Regelung kaputt ab ca. 08.10.2022 [Ladegerät](https://photos.app.goo.gl/jWHgNVxGqZ1k3UQU8) bis Frühling 2023
* ELOWIN im Betrieb ab 18.03.2023?

## Betreibs-Probleme

### Haben wir Tagen verpasst?

#### Wetter

Basiert auf DWD distorische Daten

Siehe Regression [notebook](./flight_days_checks.ipynb)

#### Flugbetrieb in der Umgebung

Siehe [notebook](./dhvxc/dhvxc_region.ipynb)

### Streckenflugpotential besser ausnutzen

TODO @Akos Wetterdaten & XC tracks

### Vereinsarbeit besser verteilen

Siehe [Punktsystem](#punktsystem-verein)

### Flugsicherheit 

* Wie viel Praxis (Schlepps, Schlepptage) braucht ein WF (pro Jahr), um die Piloten nicht zu gefährden?
* Wie viele Schlepps pro Tag pro WF sind noch sicher? Wie viele Stunden sind noch sicher an einem Hitzetag?


## Vergleich Dienstplanungen

### Fahrdienst HDGV

Nicht vergleichbar.

* Gleichbeteiligung: Alle Mitglieder sind eingeteilt (nicht nur eine Minderheit wie die WF)
* Vereinsarbeit: Kein Windenverein => Fahrdienst grundsätzlich einzige Möglichkeit in der Arbeit teilzunehmen
* Flugerwartungen am Diensttag: An guten Tagen kann man trotz Fahrdienst mit einem längeren Flug rechnen.
* Kalendarabdeckung: Viel mehr Mitglieder => Samstag, Sonntag + Feiertage können mit 2 Fahrer
* Shuttle fahren 4 Stunden vs Winde fahren 4 Stunden in der Hitze?

### Windenfahrerdienst Deisterflieger

* Weniger Gastflieger (mindestens keine öffentlichen Kalender)
* Streckenflugpotenzial deutchlich niedriger: Lufträume, Lee-Lage (absteigende Luftmasse)

### Windenfahrerdienst GSC Landesbergen

* 2 Schleppstrecken (Grundsätzlich alle Windrichtungen)
* Sie hatten WF-Plan, haben aber abgelöst


### Windenfahrerdienst beim Segelflugbetrieb

* Weniger Wetter-Abhängig
* Betrieb braucht mehr Personal
* Ortsgebunden

## Alternativen zum Windenfahrerdienstplan an 3 Ebenen

### WF-Anteil erhöhen `VEREIN`

* Stand 10.03.2024 : mehrere WiFA

### Punktsystem `VEREIN` 

* Am Jahresbeginn nimm Anzahl `N` von Schlepps als Durchschnitt aus dem letzten 3 (oder 5) Jahren

#### WF 

  * Ziehe `A` = 60 * Anzahl von WiFA (oder Pauschal 2) ab
  * Verteilen Zwischen `W` Windenfarher - ohne EWFs und WiFAs
  * Schlepps zu Leisten: `n = (N - A)/w`
  * Schlepps pro WF *veröffentlichen*
  * Nach `n` geschafften Schlepps weitere Vorteile an WF

#### Nicht-WF

  * `M` Anzahl von nicht-WF
  * Startleitertätigkeiten zu Leisten: `N/M`
  * Auch veröffentlichen


### Kalender-Regeln überdenken `VEREIN`

* Anmeldungsfrist 20:00 Vorabend 
  * auch technisch (im Kalender) 
  * persönliches Engagement von Piloten verstärken
* "gelb" streichen

### Fernbedienung `VEREIN`

* weniger Anwesenden gebraucht
  * hauptsätzlich in der Woche - in der Regel kein Mischflugbetrieb
  * Am Wochenende gibt's mehr Leute

### Kooperation mit den anderen Vereinen verstärken `REGIO`

* Gemeinsame Anmeldungstool
* Piloten &  WF(!) austausch

### Selbstschlepp `DHV`

* Nur langfristige Lösung










