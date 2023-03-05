import random
import csv

### Wörterbücher und Zähler für Richtig/Falsch ###
woerter = {}
woerter_1 = {}
woerter_2 = {}
woerter_3 = {}
woerter_4 = {}
richtig = {}
falsch = {}

### Funktion zum erstellen von neuen Vokabeln ###
def neu():

    while True:
        wort = input("Bitte gebe ein neues Wort ein (#fertig zum Abbrechen): ")
        if wort == "#fertig":
            break
        uebersetzung = input("Bitte gebe die Übersetzung ein: ")
        woerter[wort] = uebersetzung
        richtig[wort] = 0
        falsch[wort] = 0
        print("Wort wurde gespeichert!")

### Abfrage ob eine bestimmte Vokabel in den Wörterbüchern vorhanden ist und wo ###
def abfrage():

    def abfrage_dyn(dicti):
        print(wort + ": " + dicti[wort] + " befindet sich in Fach 0")
        print(wort + " wurde " + str(richtig[wort]) + " mal richtig und " + str(falsch[wort]) + " mal falsch eingeben.")

    while True:

        wort = input("Bitte gebe ein Wort ein (#fertig zum Abbrechen): ").lower()
        if wort == "#fertig":
            break

        elif wort in woerter:
            abfrage_dyn(woerter)
            
        elif wort in woerter_1:
            abfrage_dyn(woerter_1)

        elif wort in woerter_2:
            abfrage_dyn(woerter_2)

        elif wort in woerter_3:
            abfrage_dyn(woerter_3)

        elif wort in woerter_4:
            abfrage_dyn(woerter_4)

        else:
            print("Wort ist nicht in Wörterbuch, bitte eintragen mit 'neu'")

### Starte das Vokabelquiz ### 
def quiz():

    def quiz_dyn(dicti, dicti_next, dicti_prev, bool_next, bool_prev):

        while True:

            if dicti:

                print("Zum Abbrechen #fertig eingeben")
                w = list(dicti.keys()) # key - value
                print(w)
                zufall = random.randint(0, len(w) - 1) # zufälliger index in w
                abfrageWort = w[zufall]
                abfrage = input("Was ist die Übersetzung von " + abfrageWort + "? ").lower()
                if abfrage == "#fertig":
                    break
                elif abfrage == dicti[abfrageWort]:
                    print("Richtig!")
                    richtig[abfrageWort] = richtig[abfrageWort] + 1

                    if bool_next:
                        richtigesWort = {abfrageWort: abfrage}
                        dicti_next.update(richtigesWort)
                    
                    del dicti[abfrageWort]
                        
                else:
                    print("Falsch")
                    falsch[abfrageWort] = falsch[abfrageWort] + 1

                    if bool_prev:
                        falschesWort = {abfrageWort: dicti[abfrageWort]}
                        dicti_prev.update(falschesWort)
                        del dicti[abfrageWort]
            else:
                print("Glückwunsch! Es befinden sich keine Vokabeln mehr in diesem Fach!")
                break

    print("Aus welchem Fach sollen die Vokabeln kommen?")
    auswahl = input("Gebe das Fach an (0 bis 4): ")

    if auswahl == "0":
        quiz_dyn(woerter, woerter_1, woerter, True, False)

    elif auswahl == "1":
        quiz_dyn(woerter_1, woerter_2, woerter, True, True)

    elif auswahl == "2":
        quiz_dyn(woerter_2, woerter_3, woerter_1, True, True)
        
    elif auswahl == "3":
        quiz_dyn(woerter_3, woerter_4, woerter_2, True, True)

    elif auswahl == "4":
        quiz_dyn(woerter_4, woerter_4, woerter_3, False, True)

    else:
        print("Fehlerhafte Eingabe")

### Speichern der Wörterbücher und Zähler ###
def speichern():

    def speichern_dyn(dicti, file):

        with open (f"{file}", "w") as csv_file:
            writer = csv.writer(csv_file)
            for key, value in dicti.items():
                writer.writerow([key, value])

    speichern_dyn(woerter, "woerterbuch.csv")
    speichern_dyn(woerter_1, "woerterbuch_1.csv")
    speichern_dyn(woerter_2, "woerterbuch_2.csv")
    speichern_dyn(woerter_3, "woerterbuch_3.csv")
    speichern_dyn(woerter_4, "woerterbuch_4.csv")
    speichern_dyn(richtig, "richtig.csv")
    speichern_dyn(falsch, "falsch.csv")
    
    print("Gespeichert...")

### Laden der Wörterbücher und Zähler ###
def laden():

    def laden_dyn(dicti, file):

        if dicti:

            with open (f"{file}") as csv_file:
                reader = csv.reader(csv_file)
                dicti = dict(reader)
        
        else:
            print(f"Datei '{file}' wurde nicht gefunden oder existiert nicht.")

    laden_dyn(woerter, "woerterbuch.csv")
    laden_dyn(woerter_1, "woerterbuch_1.csv")
    laden_dyn(woerter_2, "woerterbuch_2.csv")
    laden_dyn(woerter_3, "woerterbuch_3.csv")
    laden_dyn(woerter_4, "woerterbuch_4.csv")
    laden_dyn(richtig, "richtig.csv")
    laden_dyn(falsch, "falsch.csv")

    print("Geladen...")

### Anzeigen der Wörter in den jeweiligen Fächern / oder komplette Anzeige + Anzahl an richtigen/falschen Antworten ### 
def anzeigen():

    ### Dynamische Funktion mit Parametern
    def anzeigen_dyn(dicti, i):

        if dicti:
            print(f"Fach {str(i)}: ")
            for key, value in dicti.items():
                print(f"Deutsch: {key} - Englisch: {value}")

        else:
            print(f"Fach {str(i)} ist leer")

    def anzeigen_dyn_count():
        
            print("Zähler - Richtig:")
            for key, value in richtig.items():
                print(f"Das Wort '{key}' wurde {value} mal richtig beantwortet.")
            print("Zähler - Falsch:")
            for key, value in falsch.items():
                print(f"Das Wort '{key}' wurde {value} mal falsch beantwortet.")

    print("Vorhandene Fächer: 0 - 4, komplett")
    auswahl = input("Welches Fach möchtest du anzeigen? ")

    if auswahl == "0":
        anzeigen_dyn(woerter, 0)
        anzeigen_dyn_count()

    elif auswahl == "1":
        anzeigen_dyn(woerter_1, 1)
        anzeigen_dyn_count()

    elif auswahl == "2":
       anzeigen_dyn(woerter_2, 2)
       anzeigen_dyn_count()

    elif auswahl == "3":
        anzeigen_dyn(woerter_3, 3)
        anzeigen_dyn_count()

    elif auswahl == "4":
        anzeigen_dyn(woerter_4, 4)
        anzeigen_dyn_count()

    elif auswahl == "komplett":
        anzeigen_dyn(woerter, 0)
        anzeigen_dyn(woerter_1, 1)
        anzeigen_dyn(woerter_2, 2)
        anzeigen_dyn(woerter_3, 3)
        anzeigen_dyn(woerter_4, 4)
        anzeigen_dyn_count()
        
    else:
        print("Fehlerhafte Ausgabe")

### Verschiedene Befehle / Menüsteuerung ### 
print("Starten des Vokabeltrainers.")
print("Folgende Befehle stehen zur Auswahl:")
print("-- neu\n-- abfrage\n-- quiz\n-- speichern\n-- laden\n-- anzeigen\n-- beenden")
command = (input("Befehl eingeben: ")).lower()

while command != "beenden":

    if command == "neu":
        neu()
    elif command == "abfrage":
        abfrage()
    elif command == "quiz":
        quiz()
    elif command == "speichern":
        speichern()
    elif command == "laden":
        laden()
    elif command == "anzeigen":
        anzeigen()
    else:
        print("Unbekannter Befehl. Dir stehen folgende Befehle zur Auswahl:")
        print("-- neu\n-- abfrage\n-- quiz\n-- speichern\n-- laden\n-- anzeigen\n-- beenden")
    
    command = (input("Befehl eingeben: ")).lower()

print("Beenden des Vokabeltrainers.")