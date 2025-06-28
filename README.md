# poly

This repository provides a simple script to query Polymarket data.

## fetch_markets.py

`fetch_markets.py` ruft ueber die Gamma API aktive Maerkte ab, deren Startdatum nach dem 26. Juni 2025 liegt. Die gefundenen Maerkte werden ausgegeben und das Programm fragt, ob Preise ueber den CLOB Endpunkt abgefragt werden sollen. Bei Bestaetigung werden die Token der Maerkte abgefragt und die aktuellen Preise ausgegeben.

Fehlschläge bei Netzwerkzugriffen werden nun abgefangen und als klare Meldungen ausgegeben.

### Nutzung

1. Abhaengigkeit installieren:
   ```bash
   pip install requests
   ```
2. Script starten:
   ```bash
   python fetch_markets.py
   ```
