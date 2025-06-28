# poly

This repository provides a simple script to query Polymarket data.

## fetch_markets.py

`fetch_markets.py` ruft ueber die Gamma API aktive Maerkte ab, deren Startdatum nach dem 26. Juni 2025 liegt. Die gefundenen Maerkte werden ausgegeben und das Programm fragt, ob Preise ueber den CLOB Endpunkt abgefragt werden sollen. Bei Bestaetigung werden die Token der Maerkte abgefragt und die aktuellen Preise ausgegeben.
Beim Abfragen der Token nutzt das Skript die jeweilige `condition_id` eines Marktes.
Diese ID wird an den CLOB-Endpunkt `/markets/<condition_id>` geschickt, um die
zugehörigen Token-IDs zu erhalten.

Beispielausgabe:

```text
Gefundene Märkte:
- 42: beispiel-market (Start: 2025-07-01T00:00:00Z)
Fortfahren und Preise abrufen? [j/N] j
Tokens für condition_id 42: ['0xabc...', '0xdef...']
```

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
