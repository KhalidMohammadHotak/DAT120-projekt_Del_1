#creating topic lag emne
emner = []
def lag_emne():
    print("\n Lager et nytt emne...")
    emnekode = input("Skriv emnekode (f.eks. MAT100): ").strip().upper()
    semester = input("Undervises i Høst (H) eller Vår (V): ").strip().upper()
    studiepoeng = int(input("Antall studiepoeng: "))
    
    emne = {
        "kode": emnekode,
        "semester": semester,
        "studiepoeng": studiepoeng
    }

    emner.append(emne)
    print(f" Emne '{emnekode}' ble lagret!")
    
    
#skrive ut emner
def skrive_ut_emner():
    if not emner:
        print("Ingen emner registrert ennå.")
        return

    print("\n--- Registrerte emner ---")
    for e in emner:
        sesong = "Høst" if e["semester"] == "H" else "Vår"
        print(f"{e['kode']} ({sesong}) - {e['studiepoeng']} studiepoeng")
    print()
    
 