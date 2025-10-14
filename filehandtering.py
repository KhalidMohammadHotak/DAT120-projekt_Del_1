from emne import emner  # list of dicts: {"kode","semester","studiepoeng"}

# sem → list of emnekoder
plan = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}

HOEST_SEM = {1, 3, 5}
VAAR_SEM  = {2, 4, 6}
MAKS_SP = 30

def _find_emne(kode: str):
    kode = kode.strip().upper()
    for e in emner:
        if e["kode"] == kode:
            return e
    return None

def _alle_emner_i_planen():
    return [kode for sem in plan.values() for kode in sem]

def _semester_sp(semnr: int):
    total = 0
    for kode in plan[semnr]:
        e = _find_emne(kode)
        if e:
            total += int(e["studiepoeng"])
    return total

def legg_til_emner():
    """Menu 2: Interaktivt – velg emnekode + semester og legg til med regler."""
    if not emner:
        print("Ingen emner registrert. Lag et emne først (valg 1).")
        return

    kode = input("Emnekode å legge til: ").strip().upper()
    e = _find_emne(kode)
    if not e:
        print("Fant ikke emnet. Lag det først i meny 1.")
        return

    try:
        semnr = int(input("Semester (1–6): ").strip())
    except ValueError:
        print("Ugyldig verdi. Skriv et tall 1–6.")
        return
    if semnr not in plan:
        print("Ugyldig semester. Må være 1–6.")
        return

    # 1) ikke duplikat i hele planen
    if kode in _alle_emner_i_planen():
        print("Dette emnet er allerede i studieplanen.")
        return

    # 2) riktig sesong
    if e["semester"] == "H" and semnr not in HOEST_SEM:
        print("Høst-emne kan kun legges i semester 1, 3 eller 5.")
        return
    if e["semester"] == "V" and semnr not in VAAR_SEM:
        print("Vår-emne kan kun legges i semester 2, 4 eller 6.")
        return

    # 3) maks 30 SP
    sp_na = _semester_sp(semnr)
    sp_emne = int(e["studiepoeng"])
    if sp_na + sp_emne > MAKS_SP:
        print(f"Ikke plass: Semester {semnr} har {sp_na} SP. "
              f"{kode} ({sp_emne} SP) vil overstige {MAKS_SP} SP.")
        return

    plan[semnr].append(kode)
    print(f" La til {kode} i semester {semnr}.")

def skrive_ut_studieplan():
    print("\n--- Studieplan ---")
    for s in range(1, 7):
        koder = plan[s]
        sp = _semester_sp(s)
        if koder:
            print(f"Semester {s} (sum {sp} SP): " + ", ".join(koder))
        else:
            print(f"Semester {s} (sum {sp} SP): (ingen emner)")
    print()

def sjekk_gyldighet():
    """Gyldig hvis alle 6 sem har nøyaktig 30 SP."""
    ikke_ok = []
    for s in range(1, 7):
        sp = _semester_sp(s)
        if sp != MAKS_SP:
            ikke_ok.append((s, sp))
    if not ikke_ok:
        print(" Studieplanen er gyldig (alle semestre har 30 studiepoeng).")
    else:
        print(" Studieplanen er IKKE gyldig. Mangler/avvik:")
        for s, sp in ikke_ok:
            print(f"  Semester {s}: {sp} studiepoeng")
