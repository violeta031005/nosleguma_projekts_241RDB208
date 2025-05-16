import json
import datetime
import time
import threading

class MajasDarbs:
    def __init__(self, nosaukums, diena, laiks):
        self.nosaukums = nosaukums
        self.diena = diena.capitalize()
        self.laiks = laiks  

    def to_dict(self):
        return {
            "nosaukums": self.nosaukums,
            "diena": self.diena,
            "laiks": self.laiks
        }

def saglaba_darbus(darbi, fails="darbi.json"):
    ar_open = [darb.to_dict() for darb in darbi]
    with open(fails, "w", encoding="utf-8") as f:
        json.dump(ar_open, f, indent=4, ensure_ascii=False)

def ielade_darbus(fails="darbi.json"):
    try:
        with open(fails, "r", encoding="utf-8") as f:
            dati = json.load(f)
            return [MajasDarbs(**d) for d in dati]
    except FileNotFoundError:
        return []

def atgadinajumu_cikls():
    while True:
        tagad = datetime.datetime.now()
        diena = tagad.strftime("%A")
        laiks = tagad.strftime("%H:%M")

        for darbs in darbi:
            if darbs.diena == diena and darbs.laiks == laiks:
                print(f"\n Atgādinājums: {darbs.nosaukums} ({darbs.diena} {darbs.laiks}) 🔔\n")
        time.sleep(60)

def pievieno_darbu():
    nos = input("Ievadi darba nosaukumu: ")
    diena = input("Kura diena? ")
    laiks = input("Laiks? ")
    darb = MajasDarbs(nos, diena, laiks)
    darbi.append(darb)
    saglaba_darbus(darbi)
    print("Darbs pievienots!")

darbi = ielade_darbus()

t = threading.Thread(target=atgadinajumu_cikls, daemon=True)
t.start()

while True:
    print("\n==== Mājas darbu atgādinātājs ====")
    print("1. Parādīt visus darbus")
    print("2. Pievienot jaunu darbu")
    print("3. Iziet")
    izvele = input("Tava izvēle: ")

    if izvele == "1":
        if darbi:
            print("\nIr jāizpilda:")
            for d in darbi:
                print(f"{d.nosaukums} – {d.diena} {d.laiks}")
        else:
            print("Nav neviena ierakstīta darba.")
    elif izvele == "2":
        pievieno_darbu()
    elif izvele == "3":
        print("Programma beidz darbu.")
        break
    else:
        print("Nepareiza izvēle.")
