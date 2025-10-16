'''
Tema: Scambio di Key Exchange

Obiettivo: Simulare il protocollo Diffie-Hellman tra due parti (Alice e Bob) e verificare che ottengono 
la stessa chiave segreta condivisa.

Nome dell’esercizio: diffie_hellman_demo

Traccia:
Scrivere un programma Python che:
*   Definisce un numero primo p e una base g (pubblici).
*   Simula due utenti, Alice e Bob, che generano ciascuno una chiave privata casuale e calcolano la 
    propria chiave pubblica usando la formula:
*   Scambiano le chiavi pubbliche tra loro.
*   Ognuno calcola la chiave segreta condivisa usando la chiave pubblica dell’altro:
*   Verifica che le chiavi segrete di Alice e Bob coincidano e stampale a video.

Suggerimento:
*   Puoi usare la funzione random.randint(a, b) per generare le chiavi private.
*   Usa numeri primi piccoli per testare, ma ricordati che in pratica servirebbero numeri molto grandi.
        - chiave_condivisa = (chiave_pub_altra_parte ** chiave_privata) % p
        - chiave_pubblica = (g ** chiave_privata) % p
'''
p = 71
g = 10
a = 6 # chiave privata di Alice
b = 8 # chiave privata di Bob

# Chiave pubblica Alice
A = pow(g, a, p)
print(A)

# Chiave pubblica Bob
B = pow(g, b, p)
print(B)

# Scambio chiavi pubbliche per calcolo di chiave segreta
chiave_segreta_alice = pow(B, a, p)
chiave_segreta_bob = pow(A, b, p)

# Verifico che le chiavi segrete coincidano

try:
    if chiave_segreta_alice == chiave_segreta_bob:
        print("Le chiavi segrete coincidono")
    
    else:
        print("Le chiavi segrete non coincido")

except ValueError as e:
    print(f"Errore: {e}")

