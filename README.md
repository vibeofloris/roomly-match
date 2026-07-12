# 🏠 Sistema di Matching Coinquilini

## Descrizione

Questo progetto implementa un sistema di **matching tra coinquilini** basato sulla compatibilità delle preferenze personali.

L'obiettivo è simulare un algoritmo che, attraverso un questionario iniziale, confronta le caratteristiche di un nuovo utente con diversi profili già presenti e restituisce una classifica dei candidati più compatibili.

Il progetto è stato sviluppato per esercitarsi con:
- programmazione ad oggetti (OOP)
- gestione di classi e oggetti
- strutture dati Python
- logica di confronto e scoring
- gestione degli input utente

---

## Funzionamento

Il programma raccoglie le preferenze dell'utente attraverso un questionario composto da 8 criteri:

- Ordine
- Rumore
- Animali domestici
- Feste
- Fumatore
- Orari
- Cucina
- Pulizia

Per ogni criterio l'utente può scegliere:

| Valore | Significato |
|---|---|
| F | Favorevole |
| S | Sfavorevole |
| I | Indifferente |

Dopo la compilazione, il sistema confronta il profilo dell'utente con gli altri coinquilini disponibili e calcola una percentuale di compatibilità.

---

## Logica di Matching

Il confronto tra due persone avviene criterio per criterio:

- ✅ **Pro**: preferenze uguali tra i due profili
- ❌ **Contro**: preferenze differenti
- ➖ **Neutri**: almeno una delle due persone è indifferente
