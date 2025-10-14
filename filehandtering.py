# code/filhandtering.py
import json
from typing import Any, Dict
from emne import emner
from studieplan import plan

def lagre_til_fil(filnavn: str = "data.json"):
    data: Dict[str, Any] = {"emner": emner, "studieplan": plan}
    with open(filnavn, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f" Lagret til {filnavn}")

def les_fra_fil(filnavn: str = "data.json"):
    try:
        with open(filnavn, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Fant ikke fil. Lagre først (valg 6).")
        return
    except json.JSONDecodeError:
        print("Ugyldig filformat (JSON).")
        return

    # load back into globals
    emner.clear()
    for e in data.get("emner", []):
        emner.append(e)

    # plan keys can be strings in JSON – normalize to ints
    plan.clear()
    loaded_plan = data.get("studieplan", {})
    for k, v in loaded_plan.items():
        plan[int(k)] = list(v)
    print(f" Lest fra {filnavn}")
