

"""
Created on Tue Oct 14 13:50:48 2025

@author: sharifhafzi
"""

# Study Plan Program

# Lists to store course info
emnekoder = []
semester = []      # "Høst" or "Vår"
studiepoeng = []

# Study plan: 6 semesters, each is a list of course codes
studieplan = [[], [], [], [], [], []]


def lag_nytt_emne():
    kode = input("Skriv emnekode (f.eks. INF100): ").strip().upper()
    if kode in emnekoder:
        print("Emnet finnes allerede!")
        return
    sem = input("Skriv semester (Høst/Vår): ").strip().capitalize()
    if sem not in ["Høst", "Vår"]:
        print("Ugyldig semester!")
        return
    try:
        poeng = int(input("Skriv antall studiepoeng: "))
    except ValueError:
        print("Må være et tall!")
        return

    emnekoder.append(kode)
    semester.append(sem)
    studiepoeng.append(poeng)
    print(f"Emnet {kode} lagt til!")


def legg_til_emne_i_studieplan():
    if not emnekoder:
        print("Ingen emner registrert!")
        return
    kode = input("Hvilket emne vil du legge til? ").strip().upper()
    if kode not in emnekoder:
        print("Emnet finnes ikke!")
        return

    # Sjekk om emnet allerede er lagt til
    for sem in studieplan:
        if kode in sem:
            print("Emnet er allerede i studieplanen!")
            return

    try:
        semnr = int(input("Hvilket semester (1-6)? "))
    except ValueError:
        print("Ugyldig semester!")
        return
    if semnr < 1 or semnr > 6:
        print("Semester må være mellom 1 og 6.")
        return

    # Sjekk semester type
    idx = emnekoder.index(kode)
    emne_sem = semester[idx]
    if (emne_sem == "Høst" and semnr not in [1, 3, 5]) or \
       (emne_sem == "Vår" and semnr not in [2, 4, 6]):
        print(f"Feil semester! {kode} kan kun legges i {emne_sem}-semester.")
        return

    # Sjekk studiepoeng i semesteret
    total = sum(studiepoeng[emnekoder.index(k)] for k in studieplan[semnr-1])
    if total + studiepoeng[idx] > 30:
        print("Ikke plass i semesteret (maks 30 sp).")
        return

    studieplan[semnr-1].append(kode)
    print(f"{kode} lagt til i semester {semnr}!")


def skriv_ut_alle_emner():
    if not emnekoder:
        print("Ingen emner registrert.")
        return
    print("\nAlle registrerte emner:")
    for i in range(len(emnekoder)):
        print(f"{emnekoder[i]} - {semester[i]} - {studiepoeng[i]} sp")


def skriv_ut_studieplan():
    print("\nStudieplan:")
    for i in range(6):
        sem_type = "Høst" if i+1 in [1,3,5] else "Vår"
        print(f"Semester {i+1} ({sem_type}): {studieplan[i]} - total sp: {sum(studiepoeng[emnekoder.index(k)] for k in studieplan[i])}")

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
