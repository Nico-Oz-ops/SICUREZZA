'''
Tema: Crittografia RSA — rappresentazione numerica, cifratura e decifratura di messaggi.

Obiettivo: Imparare a:
    * Estrarre e convertire chiavi RSA da formato testuale (simile a PEM) in numeri interi.
    * Convertire un messaggio testuale in numero intero.
    * Applicare la formula di cifratura e decifratura RSA manualmente usando pow(M, e, n) e pow(C, d, n).
    * Riconvertire il numero decifrato in stringa.

Nome dell’esercizio: Cifratura e decifratura RSA manuale in Python

Traccia: Scrivi un programma che:

1. Simuli una chiave RSA fornendo i seguenti valori: 
n_hex =
a4:16:1b:5e:2d:88:36:cf:d1:a7:9a:42:91:bb:a1:73:
91:6c:39:4a:73:29:a8:53:d2:ff:2e:0d:35:cf:9d:01

e_hex = 010001
d_hex =
6f:af:1e:94:3d:76:0a:a3:2b:97:68:7e:3d:54:a2:44:
1a:b0:31:57:0f:b9:dc:92:a7:4f:a3:ed:21:3b:92:2d

2. Converta ciascuna stringa esadecimale in un intero

3. Scelga un messaggio (ad esempio "HELLO") e:
    * Converti ogni carattere in byte e poi in intero
    * Cifra
    * Decifra

4. Riconvertire in stringa

5. Verificare che messaggio decifrato sia uguale al messaggio originale.
'''
n_hex = '''00:9f:f6:96:1f:f2:c4:7f:7c:a5:b2:95:a0:9f:11:
    90:bc:4b:fc:6b:be:72:e4:a7:a1:9f:ea:56:06:2d:
    41:66:8f:3b:8c:79:e4:03:bb:e2:7d:8c:ee:89:57:
    08:1e:ef:82:b2:b3:6b:60:b9:6e:d7:08:d9:94:99:
    62:77:e5:9e:18:77:c0:0c:51:63:08:0a:28:cc:b8:
    d9:af:32:bf:61:88:33:fe:8c:0c:70:73:6b:99:13:
    36:55:8d:46:99:c2:dd:f4:75:4a:47:3f:4b:5c:83:
    ac:3e:af:c7:0c:f2:0d:74:86:41:74:c9:ed:50:8c:
    5c:f4:b7:dd:1e:79:70:de:be:69:bd:24:cb:ab:cd:
    25:42:c0:6d:ac:c1:07:cf:90:31:d7:69:35:14:53:
    cb:93:b4:dc:6d:2a:5b:0c:77:13:ce:2b:61:8b:f5:
    16:ed:2a:0f:ec:96:8c:51:4a:11:1c:25:4f:3e:6a:
    2d:1b:be:ce:e2:88:6d:22:64:52:e5:1f:a2:47:6d:
    2c:29:24:c9:7b:70:02:31:ab:a3:ec:78:bb:90:a2:
    a4:30:cf:e4:95:16:5d:04:0d:9f:69:20:ee:d8:84:
    be:e3:13:e6:c5:81:a8:1a:27:11:d4:f1:e6:d7:59:
    2d:d9:0b:0a:f9:3d:82:45:37:1f:24:c2:84:29:66:
    fd:25
'''

e = 3
d_hex = '''1a:a9:19:05:53:20:bf:ea:1b:9d:c3:9a:c5:2d:98:
    1f:61:ff:67:4a:68:7b:71:45:9a:a7:0e:56:5c:e0:
    3b:c2:89:ec:be:fb:55:f4:a5:bf:97:7d:16:e3:d6:
    af:d2:95:c8:73:3c:90:1e:e7:ce:81:79:98:c4:3b:
    13:fb:9a:59:69:4a:ac:b8:3b:2c:01:b1:77:74:24:
    47:dd:ca:90:41:5d:ff:c2:02:12:bd:e7:44:2d:de:
    63:97:8b:c4:4b:24:fe:13:8c:61:35:37:3a:15:f2:
    0a:72:a1:2c:d3:02:3e:16:60:3e:21:a7:8d:6c:ba:
    28:c9:4f:85:14:3d:7a:74:cd:d3:f4:f5:85:83:6b:
    1d:c7:a2:62:58:09:6b:91:c6:fb:d0:55:fc:41:cb:
    23:99:83:5e:e1:ce:91:43:20:a7:db:f7:d9:fc:68:
    91:cf:fe:c4:83:b5:89:72:68:23:09:70:10:4e:ee:
    f8:08:ae:93:a3:9a:cd:af:0c:eb:6e:0f:79:bc:20:
    4c:29:62:6a:fd:2a:00:a9:eb:19:61:e4:1c:c6:cf:
    63:c5:aa:0e:0e:00:a6:46:71:ce:00:8d:0d:e1:03:
    20:7a:19:61:23:7a:ac:d7:07:78:e7:4e:d7:70:76:
    4e:87:b9:f5:16:03:d0:27:31:e0:54:5e:a9:b3:c5:
    6b'''

# Pulizie dei valori di n, e e d

n_pulito = n_hex.replace(":", "").replace(" ", "").replace("\n", "")
n = int(n_pulito, 16)
print(n)

d_pulito = d_hex.replace(":", "").replace(" ", "").replace("\n", "")
d = int(d_pulito, 16)
print(d)


msg = "HELLO"

# Convertire ogni caratttere in byte e poi interi
def str_to_num(stringa: str):
    totale = 0
    esponente = 0

    for car in stringa[::-1]:
        totale = totale + 256 ** esponente * ord(car)
        esponente += 1

    return totale 

'''
La ragione per cui si usa 256 è legata al fatto che ogni carattere di una stringa in Python 
(e in generale in ASCII/UTF-8) può essere rappresentato da un byte.

Perché 256 e non 128 o 100?

 * 256 è il numero naturale di valori per un byte (8 bit).
 * Se usassi 128, funzionerebbe solo per ASCII a 7 bit.
 * Se usassi 100, la conversione non sarebbe coerente con la codifica dei byte.
'''

M = str_to_num(msg)

# Cifrare
cifra = pow(M, e, n)

# Decifrare
decifra = pow(cifra, d, n)

# Riconvertire in stringa
def num_to_str(num: int):
    caratteri = []

    while num > 0:
        caratteri.append(chr(num % 256))
        num = num // 256
    
    return ''.join(caratteri[::-1])

decifra_msg = num_to_str(decifra)

# Verificare che il messaggio decifrato sia uguale al messaggio originale

try:
    if decifra_msg == msg:
        print("Enhorabuena los mensajes son iguales")
        print(f"Messaggio originale: {msg}")
        print(f"Messaggio decifrato: {decifra_msg}")
    
    else:
        print("I messaggi non coincidono")

except ValueError as e:
    print(f"Errore di conversione: {e}")



# Alternativa 2
n_pulito = n_hex.replace(":", "").replace(" ", "").replace("\n", "")
n = int(n_pulito, 16)
print(n)

d_pulito = d_hex.replace(":", "").replace(" ", "").replace("\n", "")
d = int(d_pulito, 16)
print(d)

messaggio = "HELLO"

msg_int = int.from_bytes(messaggio.encode(), "big") # equivalente alla funzione str_to_num

cifra = pow(msg_int, e, n)
decifra = pow(cifra, d, n)

decifra_str = decifra.to_bytes((decifra.bit_length() + 7) // 8, "big").decode() # equivalente alla funzione num_to_str

try:
    if decifra_str == messaggio:
        print("Enhorabuena los mensajes son iguales")
        print(f"Messaggio originale: {messaggio}")
        print(f"Messaggio decifrato: {decifra_str}")
    
    else:
        print("I messaggi non coincidono")

except ValueError as e:
    print(f"Errore di conversione: {e}")


