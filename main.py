from emne import lag_emne, skrive_ut_emner
from studieplan import legg_til_emner, skrive_ut_studieplan, sjekk_gyldighet
from filehandtering import lagre_til_fil, les_fra_fil


def main():
    while True:
        print("""
        1.lag et nytt emne
        2.legg til et emne i studieplannen
        3.Skrive ut liste over emner
        4.Skriv ut studieplan
        5.Sjekk om studieplanne er gylding
        6.Lagre til fil
        7.Les fra  file
        8.Avslutt      
              """)
        choice = input("Velg et nummer: ")
        if choice == "1":
            lag_emne()
        elif choice == "2":
            legg_til_emner()
        elif choice== "3":
            skrive_ut_emner()
        elif choice == "4":
            skrive_ut_studieplan()
        elif choice == "5":
            sjekk_gyldighet()
        elif choice == "6":
            lagre_til_fil()
        elif choice == "7":
            les_fra_fil()
        elif choice == "8":
            break
        else:
            print("Ugyldig valg")

if __name__ == "__main__":
        main()