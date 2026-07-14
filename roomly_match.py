# Criteri match
criteri = {
    "ORDINE": "Ordine",
    "RUMORE": "Rumore",
    "ANIMALI": "Animali",
    "FESTE": "Feste",
    "FUMATORE": "Fumatore",
    "ORARI": "Orari",
    "CUCINA": "Cucina",
    "PULIZIA": "Pulizia"
}

# Modello preferenze
class Preferenze:
    def __init__(self, criteri: dict):
        self.criteri: dict = criteri

# Modello candidati
class Persona:
    def __init__(self, nome: str, preferenze: Preferenze):
        self.nome: str = nome
        self.preferenze: Preferenze = preferenze


# Profili di test
preferenze_francesca = Preferenze({
    criteri["ORDINE"]: "F",
    criteri["RUMORE"]: "S",
    criteri["ANIMALI"]: "F",
    criteri["FESTE"]: "I",
    criteri["FUMATORE"]: "F",
    criteri["ORARI"]: "F",
    criteri["CUCINA"]: "F",
    criteri["PULIZIA"]: "F"
})
francesca = Persona("Francesca", preferenze_francesca)

preferenze_sibilla = Preferenze({
    criteri["ORDINE"]: "F",
    criteri["RUMORE"]: "I",
    criteri["ANIMALI"]: "I",
    criteri["FESTE"]: "S",
    criteri["FUMATORE"]: "I",
    criteri["ORARI"]: "F",
    criteri["CUCINA"]: "F",
    criteri["PULIZIA"]: "F"
})
sibilla = Persona("Sibilla", preferenze_sibilla)

preferenze_lorenzo = Preferenze({
    criteri["ORDINE"]: "F",
    criteri["RUMORE"]: "S",
    criteri["ANIMALI"]: "I",
    criteri["FESTE"]: "I",
    criteri["FUMATORE"]: "I",
    criteri["ORARI"]: "F",
    criteri["CUCINA"]: "F",
    criteri["PULIZIA"]: "F"
})
lorenzo = Persona("Lorenzo", preferenze_lorenzo)

preferenze_luca = Preferenze({
    criteri["ORDINE"]: "F",
    criteri["RUMORE"]: "I",
    criteri["ANIMALI"]: "I",
    criteri["FESTE"]: "I",
    criteri["FUMATORE"]: "I",
    criteri["ORARI"]: "F",
    criteri["CUCINA"]: "F",
    criteri["PULIZIA"]: "F"
})
luca = Persona("Luca", preferenze_luca)

preferenze_giovanna = Preferenze({
    criteri["ORDINE"]: "F",
    criteri["RUMORE"]: "S",
    criteri["ANIMALI"]: "S",
    criteri["FESTE"]: "F",
    criteri["FUMATORE"]: "S",
    criteri["ORARI"]: "F",
    criteri["CUCINA"]: "F",
    criteri["PULIZIA"]: "F"
})
giovanna = Persona("Giovanna", preferenze_giovanna)

preferenze_loris = Preferenze({
    criteri["ORDINE"]: "F",
    criteri["RUMORE"]: "S",
    criteri["ANIMALI"]: "I",
    criteri["FESTE"]: "I",
    criteri["FUMATORE"]: "I",
    criteri["ORARI"]: "F",
    criteri["CUCINA"]: "F",
    criteri["PULIZIA"]: "F"
})
loris = Persona("Loris", preferenze_loris)


coinquilini_test: list = [francesca, sibilla, lorenzo, luca, giovanna, loris]

# Domande match (chiavi allineate a "criteri")
domande = {
    "Ordine": "Ordine in casa? [F/S/I]: ",
    "Rumore": "Rumore in casa? [F/S/I]: ",
    "Animali": "Animali domestici? [F/S/I]: ",
    "Feste": "Feste in casa? [F/S/I]: ",
    "Fumatore": "Convivere con fumatori? [F/S/I]: ",
    "Orari": "Rispettare gli orari? [F/S/I]: ",
    "Cucina": "Cucinare spesso? [F/S/I]: ",
    "Pulizia": "Pulizia frequente? [F/S/I]: "
}

# Valori ammessi
opzioni = {
    "F": "Favorevole",
    "S": "Sfavorevole",
    "I": "Indifferente"
}


class RisultatoMatch:
    def __init__(self,
                 persona1: Persona,
                 persona2: Persona,
                 pro: list,
                 contro: list,
                 neutri: list,
                 punteggio: float
    ):
        self.persona1 = persona1
        self.persona2 = persona2
        self.pro = pro
        self.contro = contro
        self.neutri = neutri
        self.punteggio = punteggio


class CalcoloMatch:
    def calcola_match(self, persona1: Persona, persona2: Persona) -> RisultatoMatch:

        pro = []
        contro = []
        neutri = []

        for criterio, valore1 in persona1.preferenze.criteri.items():
            valore2 = persona2.preferenze.criteri.get(criterio)

            if valore1 == "I" or valore2 == "I":
                neutri.append(criterio)
            elif valore1 == valore2:
                pro.append(criterio)
            else:
                contro.append(criterio)

        totale_rilevante = len(pro) + len(contro)
        punteggio = (len(pro) / totale_rilevante * 100) if totale_rilevante > 0 else 100.0

        return RisultatoMatch(persona1, persona2, pro, contro, neutri, punteggio)


def mostra_match_singolo(risultato: RisultatoMatch):
    print("\n" + "=" * 50)
    print(f"   MATCH: {risultato.persona1.nome.upper()} vs {risultato.persona2.nome.upper()}   ")
    print("=" * 50)
    print(f"  Compatibilità: {risultato.punteggio:.1f}%")
    print(f"  [+] Punti in comune ({len(risultato.pro)}): {', '.join(risultato.pro) if risultato.pro else 'Nessuno'}")
    print(f"  [-] Divergenze      ({len(risultato.contro)}): {', '.join(risultato.contro) if risultato.contro else 'Nessuna'}")
    print(f"  [/] Neutri/Indiff.  ({len(risultato.neutri)}): {', '.join(risultato.neutri) if risultato.neutri else 'Nessuno'}")
    print("-" * 40)


def mostra_benvenuto():
    print("=" * 50)
    print("      SISTEMA DI MATCHING COINQUILINI    ")
    print("=" * 50)
    print("\nLinee guida per la compilazione del test:")
    print("Rispondi a ciascun quesito utilizzando i seguenti codici:")
    print("  [F] Favorevole  |  [S] Sfavorevole  |  [I] Indifferente")
    print("-" * 50)


def crea_persona() -> Persona:
    nome = input("Come ti chiami? ")
    risposte = {}

    for chiave, domanda in domande.items():
        valido = False
        while not valido:
            risposta = input(domanda).strip().upper()
            if risposta in opzioni:
                risposte[chiave] = risposta
                valido = True
            else:
                print("Inserisci solo F, S oppure I.")

    print(f"\nLe risposte di {nome}:")
    for chiave, valore in risposte.items():
        print(f"{chiave}: {opzioni[valore]}")

    preferenze_utente = Preferenze(risposte)
    return Persona(nome, preferenze_utente)


def mostra_elenco_persone(elenco: list):
    print("\nPersone registrate:")
    for i, persona in enumerate(elenco, start=1):
        print(f"  {i}. {persona.nome}")


def scegli_persona_da_elenco(elenco: list, escludi: Persona = None) -> Persona:
    """Chiede all'utente di scegliere una persona dall'elenco tramite indice numerico.
    Se 'escludi' è specificata, quella persona viene nascosta dalla scelta
    (usato per evitare che uno scontro 1vs1 avvenga contro se stessi)."""
    disponibili = [p for p in elenco if p is not escludi]

    while True:
        mostra_elenco_persone(disponibili)
        scelta = input("Seleziona il numero della persona: ").strip()
        if scelta.isdigit() and 1 <= int(scelta) <= len(disponibili):
            return disponibili[int(scelta) - 1]
        print("Numero non valido, riprova.")


def ottieni_persona(elenco: list, etichetta: str, escludi: Persona = None) -> Persona:
    """Menu di scelta per una singola persona: nuova creazione oppure selezione
    da elenco già registrato. Se creata da zero, viene aggiunta all'elenco."""
    print(f"\n--- {etichetta} ---")
    print("  1. Crea una nuova persona")
    print("  2. Scegli tra le persone già registrate")

    while True:
        scelta = input("Seleziona un'opzione [1/2]: ").strip()
        if scelta == "1":
            persona = crea_persona()
            elenco.append(persona)
            return persona
        elif scelta == "2":
            if not elenco:
                print("Nessuna persona registrata al momento. Devi crearne una nuova.")
                continue
            return scegli_persona_da_elenco(elenco, escludi=escludi)
        else:
            print("Opzione non valida, riprova.")


def esegui_scontro_1v1(elenco: list):
    """Flusso scontro 1vs1: per ciascuna delle due persone puoi scegliere
    se crearla nuova o prenderla dall'elenco dei già registrati."""
    persona1 = ottieni_persona(elenco, "Prima persona")
    persona2 = ottieni_persona(elenco, "Seconda persona", escludi=persona1)

    calcolatore = CalcoloMatch()
    risultato = calcolatore.calcola_match(persona1, persona2)
    mostra_match_singolo(risultato)


def menu_principale():
    mostra_benvenuto()

    while True:
        print("\n" + "=" * 50)
        print("MENU PRINCIPALE")
        print("  1. Scontro 1vs1 (crea nuove persone e/o scegli tra registrate)")
        print("  2. Esci")
        scelta = input("Seleziona un'opzione: ").strip()

        if scelta == "1":
            esegui_scontro_1v1(coinquilini_test)
        elif scelta == "2":
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida, riprova.")


if __name__ == "__main__":
    menu_principale()