# Criteri
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
    def __init__(self, criteri: dict[str, str]):
        self.criteri: dict[str, str] = criteri

# Modello candidati
class Persona:
    def __init__(self, nome: str, preferenze: Preferenze):
        self.nome: str = nome
        self.preferenze: Preferenze = preferenze


# Profili
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
francesca = Persona(
    "Francesca",
    preferenze_francesca
)

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
sibilla = Persona(
    "Sibilla",
    preferenze_sibilla
)

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
lorenzo = Persona(
    "Lorenzo",
    preferenze_lorenzo
)

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
luca = Persona(
    "Luca",
    preferenze_luca
)

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
giovanna = Persona(
    "Giovanna",
    preferenze_giovanna
)

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
loris = Persona(
    "Loris",
    preferenze_loris
)

# Lista candidati + input
coinquilini: list = [francesca, sibilla, lorenzo, luca, giovanna, loris]

# Domande match 
domande = {
    "Ordine": "Ordine in casa? [F/S/I]: ",
    "Rumore": "Rumore in casa? [F/S/I]: ",
    "Animali": "Animali domestici? [F/S/I]: ",
    "Feste": "Feste in casa? [F/S/I]: ",
    "Fumatore": "Convivere con fumatori? [F/S/I]: ",
    "Orari": "Rispettare gli orari? [F/S/I]: ",
    "Cucina": "Cucinare spesso? [F/S/I]: ",
    "Pulizie": "Pulizia frequente? [F/S/I]: "
}

# Valori ammessi
opzioni = {
    "F": "Favorevole",
    "S": "Sfavorevole",
    "I": "Indifferente"
}

# Schermata di benvenuto
def mostra_benvenuto():
    print("=" * 50)
    print("      SISTEMA DI MATCHING COINQUILINI    ")
    print("=" * 50)
    print("\nLinee guida per la compilazione del test:")
    print("Rispondi a ciascun quesito utilizzando i seguenti codici:")
    print("  [F] Favorevole  |  [S] Sfavorevole  |  [I] Indifferente")
    print("-" * 50)

# Raccolta preferenze 
def crea_persona() -> Persona:
    mostra_benvenuto()
    
    nome = input("Come ti chiami? ")

    risposte = {}
    for chiave, domanda in domande.items():
        while True:
            risposta = input(domanda).strip().upper()

            if risposta in opzioni:
                risposte[chiave] = risposta
                break
            else:
                print("Inserisci solo F, S oppure I.")

    print(f"\nLe risposte di {nome}:")
    for chiave, valore in risposte.items():
        print(f"{chiave}: {opzioni[valore]}") 

    while True:
        altro = input("Vuoi aggiungere un'altra persona? [S/N]: ").strip().upper()
        if altro != "S":
            coinquilini.append(crea_persona())
            break

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
    def calcola_match(self,
                      persona1: Persona,
                      persona2: Persona
    ) -> RisultatoMatch:
        
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
    
def mostra_classifica_match(utente_target: Persona, lista_candidati: list[Persona]):
    calcolatore = CalcoloMatch()
    risultati: list[RisultatoMatch] = []

    # Confronta l'utente target con tutti gli altri 
    for candidato in lista_candidati:
        if candidato.nome != utente_target.nome:
            match = calcolatore.calcola_match(utente_target, candidato)
            risultati.append(match)

    # Ordina i risultati dal punteggio più alto a quello più basso
    risultati.sort(key=lambda x: x.punteggio, reverse=True)

    # Print dei risultati a schermo
    print("\n" + "="*50)
    print(f"   RISULTATI MATCH PER: {utente_target.nome.upper()}   ")
    print("="*50)

    for risultato in risultati:
        print(f"\nCoinquilino: {r.persona2.nome}")
        print(f"  Compatibilità: {r.punteggio:.1f}%")
        print(f"  [+] Punti in comune ({len(r.pro)}): {', '.join(r.pro) if risultato.pro else 'Nessuno'}")
        print(f"  [-] Divergenze      ({len(r.contro)}): {', '.join(r.contro) if risultato.contro else 'Nessuna'}")
        print(f"  [/] Neutri/Indiff.  ({len(r.neutri)}): {', '.join(r.neutri) if risultato.neutri else 'Nessuno'}")
        print("-" * 40)


if __name__ == "__main__":

    # 1. Avvia l'inserimento dati 
    crea_persona()

    # 2. Recupera l'ultimo utente inserito
    utente_corrente = coinquilini[-1]
    
    # 3. Mostra la classifica rispetto a tutti gli altri profili
    mostra_classifica_match(utente_corrente, coinquilini)

