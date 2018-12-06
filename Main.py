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
    print(kandierungsfaktor[RandomKandidat1], "\n")

    print(">> ", vorname[RandomKandidat2], " ", name[RandomKandidat2])
    print(studienfach[RandomKandidat2])
    print(fachsemester[RandomKandidat2], ". Fachsemester\n")
    print(wahltext[RandomKandidat2], "\n")
    print(kandierungsfaktor[RandomKandidat2], "\n")

    print(">> ", vorname[RandomKandidat3], " ", name[RandomKandidat3])
    print(studienfach[RandomKandidat3])
    print(fachsemester[RandomKandidat3], ". Fachsemester\n")
    print(wahltext[RandomKandidat3], "\n")
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
            auswahl = str(input("Ist dir der Studiengang wichtig?\n"));
            if auswahl == "ja":

                #   spezifische Frage nach dem Studiengang
                while True:
                    try:
                        studiengang = str(input("Studiengang [Inf, MInf, Dipl, MaInf, MaMInf]\n"))

                        #   bei gültiger Eingabe: Beenden der Schleife, bei ungültiger Eingabe: Erzeugen eines Fehlers
                        #   --> erneuter Durchlauf
                        if studiengang not in {"Inf", "MInf", "Dipl", "MaInf", "MaMInf"}:
                            studiengang = int("Fehler")
                        break
                    except ValueError:
                        print("Das war keine gültige Eingabe. Bitte versuche es erneut.\n")

            #   bei "nein": Beenden der Schleife, bei !"nein": Erzeugen eines Fehler --> erneuter Durchlauf
            elif auswahl != "nein":
                auswahl = int("Fehler")
            break
        except ValueError:
                print("Das war keine gültige Eingabe. Bitte versuche es erneut.")

    #   Abfrage der Zweitkandidatur
    while True:
        try:
            auswahl = str(input("Ist dir wichtig, dass es ein Neuling ist?\n"));
            if auswahl == "ja":
                neuling = auswahl

            #   bei "nein": Beenden der Schleife, bei !"nein": Erzeugen eines Fehler --> erneuter Durchlauf
            elif auswahl != "nein":
                auswahl = int("Fehler")
            break
        except ValueError:
                print("Das war keine gültige Eingabe. Bitte versuche es erneut.")

    #   Abfrage des Fachsemesters
    while True:
        try:
            auswahl = str(input("Ist dir das Fachsemester wichtig?\n"));
            if auswahl == "ja":
                fachsemesteranzahl.remove("irrelevant")

                #   Schleife für weitere Fachsemestereingaben
                while auswahl == "ja":
                    count += 1
                    fachsemesteranzahl.append(0)

                    #   spezifische Frage nach dem Fachsemester
                    while True:
                        try:

                            #   'eingabe' dient als Zwischenspeicher der Eingabe damit keine Fachsemester doppelt
                            #   eingegeben werden
                            eingabe = int(input("Fachsemester\n"))

                            #   es wird geschaut, ob eingabe nicht zu groß oder klein ist oder ob dieses Fachsemester
                            #   schon bereits angegeben wurde.
                            if eingabe > 11 or eingabe < 1:
                                fachsemesteranzahl[count] = int("Fehler")
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
                            auswahl = str(input("Möchtest du weitere Fachsemester angeben?\n"))

                            #   bei gültiger Eingabe: Beenden der Schleife, bei ungültiger Eingabe:
                            #   Erzeugen eines Fehlers --> erneuter Durchlauf
                            if auswahl not in {"ja", "nein"}:
                                auswahl = int("Fehler")
                            break
                        except ValueError:
                            print("Das war keine gültige Eingabe. Bitte versuche es erneut.")

                    #   es stehen nur 11 Semester zur Verfügung also können nicht mehr als 11 gewählt werden
                    if count >= 10:
                        print("du hast alle möglichen Fachsemester ausgewählt")
                        break

            #   bei "nein": Beenden der Schleife, bei !"nein": Erzeugen eines Fehler --> erneuter Durchlauf
            elif auswahl != "nein":
                auswahl = int("Fehler")
            break
        except ValueError:
                print("Das war keine gültige Eingabe. Bitte versuche es erneut.")

    #   hier werden die Suchkriterien ausgegeben. Später muss hier der Vergleich mit den Kandidaten folgen
    print("\nSuchparameter:")
    print("Studiengang: ", studiengang)
    print("Zweitkandidatur: ", neuling)
    print("Fachsemester: ", fachsemesteranzahl, "\n")


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
