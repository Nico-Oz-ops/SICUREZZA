# Esempio didattico di scambio di chiave usando il protoccolo Diffie-Hellman
# che permette a due parti di generare una chiave condivisa su un canale insicuro

'''
Tema: Scambio di Key Exchange

Obiettivo:
Simulare il protocollo Diffie-Hellman tra due parti (Alice e Bob) e verificare che ottengono
la stessa chiave segreta condivisa.

Nome dell'esercizio: diffie_hellman_demo

Traccia:
Scrivere un programma che:
1. Definisce un numero primo "p" e una base "g" (pubblici).
2. Simula due utenti, Alice e Bob, che generano ciascuno una chiave privata e calcolano la propria chiave pubblica.
3. Scambiano le chiavi pubbliche
4. Ognuno calcola la chiave segreta condivisa
5. Verifica che le chiavi segrete coincidano
'''
import random

def diffie_hellman_demo():
    # Defino i parametri pubblici concordati

    p = 23 # numero primo
    g = 5 # generatore

    print(f"Parametri pubblici: p = {p}, g = {g}\n")

    # Alice sceglie una chiave privata casuale
    a = random.randint(2, p - 2) # chiave privata casuale tra 2 e p-2, non banale (né 0 né 1 né p-1), valida per l'aritmetica modulo p
    A = pow(g, a, p) # chiave pubblica di Alice

    # Bob sceglie una chiave privata casuale
    b = random.randint(2, p - 2) # scelta di una chiave privata casuale per Bob
    B = pow(g, b, p) # chiave pubblica di Bob

    print(f"Alice sceglie a = {a} e calcola A = {A}")
    print(f"Bob sceglie b = {b} e calcola B = {B}\n")


    # Scambio pubblico -> Alice invia A, Bob invia B

    segreto_alice = pow(B, a, p) # Alice calcola la chiave segreta

    segreto_bob = pow(A, b, p) # Bob calcola la chiave segreta

    print(f"Chiave segreta calcolata da Alice: {segreto_alice}")
    print(f"Chiave segreta calcolata da Bob: {segreto_bob}")

    # Verificare che le due chiavi coincidano
    if segreto_alice == segreto_bob:
        print(f"Scambio riuscito! Chiave condivisa: {segreto_alice}")
    else:
        print("Errore: le chiavi non coincidono")

# Test
diffie_hellman_demo()


'''
Perché tra 2 e p-2?
* se fosse 0, g^0 mod p = 1 -> chiave pubblica triviale e prevedibile;
* se fosse 1, g^1 = g -> anche troppo semplice, quindi insicuro.

Deve essere minore di p-1, perché:
* in aritmetica modulo p, gli esponenti si "ripetono" ogni p - 1 (teorema di Fermat)
* quindi non serve usare valori più grandi
* inoltre p - 1 darebbe g ^ p-1 mod p = 1 (di nuovo, valore banale)
'''