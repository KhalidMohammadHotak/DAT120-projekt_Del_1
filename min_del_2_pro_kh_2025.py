def sjekk_studieplan_gyldighet():
    gyldig = True
    for i in range(6):
        total = sum(studiepoeng[emnekoder.index(k)] for k in studieplan[i])
        if total != 30:
            gyldig = False
            print(f"Semester {i+1} har {total} sp - ikke gyldig!")
    if gyldig:
        print("Studieplanen er gyldig!")


def lagre_til_fil():
    with open("data.txt", "w") as f:
        f.write(";".join(emnekoder) + "\n")
        f.write(";".join(semester) + "\n")
        f.write(";".join(str(sp) for sp in studiepoeng) + "\n")
        for sem in studieplan:
            f.write(";".join(sem) + "\n")
    print("Data lagret til data.txt!")


def les_fra_fil():
    global emnekoder, semester, studiepoeng, studieplan
    try:
        with open("data.txt", "r") as f:
            lines = f.read().splitlines()
            emnekoder = lines[0].split(";") if lines[0] else []
            semester = lines[1].split(";") if lines[1] else []
            studiepoeng = [int(x) for x in lines[2].split(";")] if lines[2] else []
            studieplan = [line.split(";") if line else [] for line in lines[3:9]]
        print("Data lest fra data.txt!")
    except FileNotFoundError:
        print("Filen finnes ikke!")


def hovedmeny():
    while True:
        print("\n--- MENY ---")
        print("1. Lag et nytt emne")
        print("2. Legg til et emne i studieplanen")
        print("3. Skriv ut alle registrerte emner")
        print("4. Skriv ut studieplanen")
        print("5. Sjekk om studieplanen er gyldig")
        print("6. Lagre til fil")
        print("7. Les fra fil")
        print("8. Avslutt")
        valg = input("Velg et tall (1-8): ")
        if valg == "1":
            lag_nytt_emne()
        elif valg == "2":
            legg_til_emne_i_studieplan()
        elif valg == "3":
            skriv_ut_alle_emner()
        elif valg == "4":
            skriv_ut_studieplan()
        elif valg == "5":
            sjekk_studieplan_gyldighet()
        elif valg == "6":
            lagre_til_fil()
        elif valg == "7":
            les_fra_fil()
        elif valg == "8":
            print("Avslutter programmet.")
            break
        else:
            print("Ugyldig valg!")


if __name__ == "__main__":
    hovedmeny()

