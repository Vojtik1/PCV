import time

def uvitani():
    print("Vítejte v kvízu! Odpovídejte na otázky a získávejte body.")
    time.sleep(1)

def ziskej_jmeno():
    jmeno = input("Jak se jmenujete? ")
    return jmeno

def spust_kviz(otazky):
    body = 0
    for otazka in otazky:
        print(otazka['otazka'])
        odpoved = input("Vaše odpověď: ")
        if odpoved.lower() == otazka['odpoved'].lower():
            print("Správně!")
            body += 1
        else:
            print(f"Ty jsi ale trouba! Správná odpověď byla: {otazka['odpoved']}")
        time.sleep(1)

    return body

def ukonceni(jmeno, body, otazky):
    print(f"Děkujeme za účast, {jmeno}!")
    print(f"Získali jste {body} bodů z {len(otazky)} možných.")

def main():
    uvitani()
    jmeno = ziskej_jmeno()
    otazky = [
        {
            'otazka': 'Kdo byl první člověk na měsící (napiš jen příjmení)',
            'odpoved': 'Armstrong'
        },
        {
            'otazka': 'Který oceán je největší?',
            'odpoved': 'Tichý'
        },
        {
            'otazka': 'Kde se nachází Eiffelova věž?',
            'odpoved': 'Paříž'
        }
    ]
    body = spust_kviz(otazky)
    ukonceni(jmeno, body, otazky)

if __name__ == "__main__":
    main()
