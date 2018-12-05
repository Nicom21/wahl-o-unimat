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
    #   Generieren von 3 random Zahlen zwischen 1 und der Anzahl der Kandidaten
    RandomKandidat1 = random.randint(1, 19)
    RandomKandidat2 = random.randint(1, 19)
    RandomKandidat3 = random.randint(1, 19)

    #   Ausgabe der Informationen der 3 ausgewählten Kandidaten
    print(">> ", name[RandomKandidat1], " ", vorname[RandomKandidat1])
    print(studienfach[RandomKandidat1])
    print(fachsemester[RandomKandidat1], ". Fachsemester\n")
    print(wahltext[RandomKandidat1], "\n")
    print(kandierungsfaktor[RandomKandidat1], "\n")

    print(">> ", name[RandomKandidat2], " ", vorname[RandomKandidat2])
    print(studienfach[RandomKandidat2])
    print(fachsemester[RandomKandidat2], ". Fachsemester\n")
    print(wahltext[RandomKandidat2], "\n")
    print(kandierungsfaktor[RandomKandidat2], "\n")

    print(">> ", name[RandomKandidat3], " ", vorname[RandomKandidat3])
    print(studienfach[RandomKandidat3])
    print(fachsemester[RandomKandidat3], ". Fachsemester\n")
    print(wahltext[RandomKandidat3], "\n")
    print(kandierungsfaktor[RandomKandidat3], "\n")

def spezifisch():
    print("Hier muss die spezifisch() Methode ausgeführt werden")


def main():
    print("[Wahl-o-Unimat]\n")

    #   Wahl des Modus mit Überprüfung auf korrekte Eingabe
    while True:
        try:
            i = int(input("Wähle einen Modus: (1) Zufall oder (2) Spezifisch\n"));
            if i == 1:
                zufall()
            elif i == 2:
                spezifisch()
            else:
                i = int("falsche Eingabe")
            break
        except ValueError:
                print("Das war keine gültige Eingabe. Bitte versuche es erneut.")

main()
