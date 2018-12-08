#   Bibliothek zum Einlesen der .csv Datei
import csv
#   Bibliothek für die Generierung der Zufallszahlen
import random

#   Einlesen der .csv Datei
with open('Wahlen_2018.csv') as csvfile:
    #   Erstellen eines Readers
    reader = csv.reader(csvfile)

    #   Initialisieren von Listen mit dem Namen der Spalten
    name = []
    vorname = []
    studienfach = []
    fachsemester = []
    wahltext = []
    zweitkandidatur = []
    kandierungsfaktor = []

    for row in reader:
        #   Abspeichern der einzelnen Elemente einer Spalte in die jeweilige Variable
        Name = row[0]
        Vorname = row[1]
        Studienfach = row[2]
        Fachsemester = row[3]
        Wahltext = row[4]
        Zweitkandidatur = row[5]
        Kandierungsfaktor = row[6]

        #   Hinzufügen der Variablen zu den oben erstellten Listen
        name.append(Name)
        vorname.append(Vorname)
        studienfach.append(Studienfach)
        fachsemester.append(Fachsemester)
        wahltext.append(Wahltext)
        zweitkandidatur.append(Zweitkandidatur)
        kandierungsfaktor.append(Kandierungsfaktor)


def zufall():
    #   Generieren von 3 random Zahlen zwischen 1 und der Anzahl der Kandidaten ohne Dopplungen
    RandomKandidat1 = random.randint(1, 19)
    RandomKandidat2 = random.randint(1, 19)
    RandomKandidat3 = random.randint(1, 19)
    while RandomKandidat2 == RandomKandidat1:
        RandomKandidat2 = random.randint(1, 19)
    while RandomKandidat3 == RandomKandidat1 or RandomKandidat3 == RandomKandidat2:
        RandomKandidat3 = random.randint(1, 19)

    #   Ausgabe der Informationen der 3 ausgewählten Kandidaten
    print(">> ", vorname[RandomKandidat1], " ", name[RandomKandidat1])
    print(studienfach[RandomKandidat1])
    print(fachsemester[RandomKandidat1], ". Fachsemester\n")
    print(wahltext[RandomKandidat1], "\n")
    if zweitkandidatur[RandomKandidat1] == "0":
        print("Zweitkandidatur: Nein")
    else:
        print("Zweitkandidatur: Ja")
    print(kandierungsfaktor[RandomKandidat1], "\n")

    print(">> ", vorname[RandomKandidat2], " ", name[RandomKandidat2])
    print(studienfach[RandomKandidat2])
    print(fachsemester[RandomKandidat2], ". Fachsemester\n")
    print(wahltext[RandomKandidat2], "\n")
    if zweitkandidatur[RandomKandidat2] == "0":
        print("Zweitkandidatur: Nein")
    else:
        print("Zweitkandidatur: Ja")
    print(kandierungsfaktor[RandomKandidat2], "\n")

    print(">> ", vorname[RandomKandidat3], " ", name[RandomKandidat3])
    print(studienfach[RandomKandidat3])
    print(fachsemester[RandomKandidat3], ". Fachsemester\n")
    print(wahltext[RandomKandidat3], "\n")
    if zweitkandidatur[RandomKandidat3] == "0":
        print("Zweitkandidatur: Nein")
    else:
        print("Zweitkandidatur: Ja")
    print(kandierungsfaktor[RandomKandidat3], "\n")


def spezifisch():

    #   initialisieren der Suchparameter falls der Nutzer seine Suche nicht spezifisieren möchte
    studiengang = "irrelevant"
    neuling = "irrelevant"
    #   die fachsemesteranzahl wird als Liste realisiert
    fachsemesteranzahl = []
    fachsemesteranzahl.append("irrelevant")
    #   Zählvariable für Schleifen
    count = -1

    #   Abfrage des Studienganges
    while True:
        try:
            auswahl = str(input("Ist dir der Studiengang wichtig? [Ja/Nein]\n"))
            if auswahl in {"ja", "Ja", "JA"}:

                #   spezifische Frage nach dem Studiengang
                while True:
                    try:
                        studiengang = str(input("> Studiengang [Ba Inf, Ba MInf, Di Inf, Ma Inf, Ma MInf]\n"))

                        #   bei gültiger Eingabe: Beenden der Schleife, bei ungültiger Eingabe: Erzeugen eines Fehlers
                        #   --> erneuter Durchlauf
                        if studiengang not in {"Ba Inf", "Ba MInf", "Di Inf", "Ma Inf", "Ma MInf"}:
                            studiengang = int("Fehler")
                        break
                    except ValueError:
                        print("Das war keine gültige Eingabe. Bitte versuche es erneut.\n")

            #   bei "nein": Beenden der Schleife, bei !"nein": Erzeugen eines Fehler --> erneuter Durchlauf
            elif auswahl not in {"nein", "Nein", "NEIN"}:
                auswahl = int("Fehler")
            break
        except ValueError:
                print("Das war keine gültige Eingabe. Bitte versuche es erneut.")

    #   Abfrage der Zweitkandidatur
    while True:
        try:
            auswahl = str(input("Ist dir wichtig, dass es ein Neuling ist? [Ja/Nein]\n"))
            if auswahl in {"ja", "Ja", "JA"}:
                neuling = "0"

            #   bei "nein": Beenden der Schleife, bei !"nein": Erzeugen eines Fehler --> erneuter Durchlauf
            elif auswahl not in {"nein", "Nein", "NEIN"}:
                auswahl = int("Fehler")
            else:
                neuling = "1"
            break
        except ValueError:
                print("Das war keine gültige Eingabe. Bitte versuche es erneut.")

    #   Abfrage des Fachsemesters
    while True:
        try:
            auswahl = str(input("Ist dir das Fachsemester wichtig? [Ja/Nein]\n"))
            if auswahl in {"ja", "Ja", "JA"}:
                fachsemesteranzahl.remove("irrelevant")

                #   Schleife für weitere Fachsemestereingaben
                while auswahl in {"ja", "Ja", "JA"}:
                    count += 1
                    fachsemesteranzahl.append(0)

                    #   spezifische Frage nach dem Fachsemester
                    while True:
                        try:

                            #   'eingabe' dient als Zwischenspeicher der Eingabe damit keine Fachsemester doppelt
                            #   eingegeben werden
                            eingabe = int(input("> Fachsemester\n"))

                            #   es wird geschaut, ob eingabe nicht zu groß oder klein ist oder ob dieses Fachsemester
                            #   schon bereits angegeben wurde.
                            if eingabe > 11 or eingabe < 1:
                                fachsemesteranzahl[count] = int("Fehler")

                            #   parsen auf String um mit dem Listenelement zu vergleichen
                            str(eingabe)
                            if eingabe in fachsemesteranzahl:
                                fachsemesteranzahl[count] = int("Fehler")
                            fachsemesteranzahl[count] = eingabe
                            break
                        except ValueError:
                            print("Du kannst nur Zwischen den Fachsemestern 1 - 11 wählen und keine Fachsemester"
                                  " doppelt angeben. Bitte versuche es erneut.")

                    while True:
                        try:

                            #   Abfrage, ob weitere Fachsemester eingegeben werden möchten, Abbruch,
                            #   falls keine weiteren Fachsemester zur Verfügung stehen
                            auswahl = str(input("Soll ein weiteres Fachsemester einbezogen werden? [Ja/Nein]\n"))

                            #   bei gültiger Eingabe: Beenden der Schleife, bei ungültiger Eingabe:
                            #   Erzeugen eines Fehlers --> erneuter Durchlauf
                            if auswahl not in {"ja", "Ja", "JA", "nein", "Nein", "NEIN"}:
                                auswahl = int("Fehler")
                            break
                        except ValueError:
                            print("Das war keine gültige Eingabe. Bitte versuche es erneut.")

                    #   es stehen nur 11 Semester zur Verfügung also können nicht mehr als 11 gewählt werden
                    if count >= 10:
                        print("du hast alle möglichen Fachsemester ausgewählt")
                        break

            #   bei "nein": Beenden der Schleife, bei !"nein": Erzeugen eines Fehler --> erneuter Durchlauf
            elif auswahl not in {"nein", "Nein", "NEIN"}:
                auswahl = int("Fehler")
            break
        except ValueError:
                print("Das war keine gültige Eingabe. Bitte versuche es erneut.")

    #   Erstellung einer Liste der möglichen Kandidaten
    moeglicherKandidat = []

    count = 1

    #   Vergleichen der Suchparameter mit den möglichen Kandidaten
    while count < 20:
        if studiengang == studienfach[count] or studiengang == "irrelevant":
            if neuling == zweitkandidatur[count] or neuling == "1":
                if fachsemester[count] in fachsemesteranzahl or fachsemesteranzahl[0] == "irrelevant":
                    moeglicherKandidat.append(count)
        count += 1
    count = 0

    #   Ausgabe aller möglichen Kandidaten
    while count < len(moeglicherKandidat):
        print(">> ", vorname[moeglicherKandidat[count]], " ", name[moeglicherKandidat[count]])
        print(studienfach[moeglicherKandidat[count]])
        print(fachsemester[moeglicherKandidat[count]], ". Fachsemester\n")
        print(wahltext[moeglicherKandidat[count]], "\n")
        print(kandierungsfaktor[moeglicherKandidat[count]], "\n")
        count += 1

    #   wird ausgegeben, falls die Kriterien zu keinen Kandidaten passen
    if len(moeglicherKandidat) == 0:
        print("Für dich konnte leider kein geeigneter Kandidat gefunden werden")


def main():
    print("[Wahl-o-Unimat]\n")

    #   Wahl des Modus mit Überprüfung auf korrekte Eingabe
    while True:
        try:
            i = int(input("Wähle einen Modus: (1) Zufall oder (2) Spezifisch\n"));
            if i == 1:
                print("\nZufall:\n")
                zufall()
            elif i == 2:
                print("\nSpezifisch:\n")
                spezifisch()
            else:
                i = int("Fehler")
            break
        except ValueError:
                print("Das war keine gültige Eingabe. Bitte versuche es erneut.\n")

main()
