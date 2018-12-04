def zufall():
    print("Hier muss die zufall() Methode ausgefüht werden")

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

print("Justinwarhier")