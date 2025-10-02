'''
Sia dato il messaggio cifrato (convertito in numero intero in base 10):
204751668535

Il messaggio cifrato è stato ottenuto cifrando il messaggio originale con algoritmo 
RSA senza padding con n=514948966453 e esponente pubblico (e) pari a 3.

Provare a decifrare il messaggio cifrato.

NB: il messaggio originale è una parola di cinque lettere maiuscole e minuscole.
NB: Quando il problema sembra arduo, allora un approccio brutale potrebbe essere quello vincente.
messaggio_cifrato: int = 204751668535
modulo: int = 514948966453
'''
# Alternativa 1

messaggio_cifrato = 204751668535
modulo = 514948966453
e = 3
abc = "ABCDEFGHIJKLMNOPQRSTUVWXZabcdefghijklmnopqrstuvwxyz"

trovato = False
for car1 in abc:
    if trovato:
        break

    for car2 in abc:
        if trovato:
            break

        for car3 in abc:
            if trovato:
                break

            for car4 in abc:
                if trovato:
                    break

                for car5 in abc:
                    parola = car1 + car2 +  car3 + car4 + car5

                    # converto la parola in un intero
                    parola_int = int.from_bytes(parola.encode(), "big")
                    # alternativa: M = int(parola.encode().hex(), 16)

                    # cifrare con "e" e modulo
                    cifrato = pow(parola_int, e, modulo)

                    if cifrato == messaggio_cifrato:
                        print(f"Trovato! Il messaggio originale è: {parola}")
                        trovato = True
                        break

# Alternativa 2
import itertools

messaggio_cifrato = 204751668535
modulo = 514948966453
e = 3
abc = "ABCDEFGHIJKLMNOPQRSTUVWXZabcdefghijklmnopqrstuvwxyz"

for carattere in itertools.product(abc, repeat=5):
    parola = ''.join(carattere)
    try:
        M = int.from_bytes(parola.encode(), "big")
        C = pow(M, e, modulo)
        if C == messaggio_cifrato:
            print("Trovato:", parola)
            break
    except Exception as e:
        # log dell'errore e continua con la prossima parola
        print("Errore con", parola, ":", e)
        continue



                