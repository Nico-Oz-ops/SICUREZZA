'''
Esercizio per casa
* Estrarre n (modulus), e (public exponent), d (private exponent) dal file PEM (chiave pubblica)

* In python per convertire una stringa in numero si usa
    • sn=«172312683»
    • Int(sn, 10) => intero
    • Sn=«edf45638» # esadecimale
    • Int(sn, 16)

*Convertire n, e, d in numeri interi
    • Esempio: n: togliere i «:», togliere «\n», togliere « « e poi con la funzione int(s, 16) => numero intero
    • Prendete il messaggio e convertitelo in numero intero
    • Poi eseguite
    • Cifra: pow(M, e, n) => C (messaggio cifrato)
    • Decifra: pow(C, d, n) => M
    • Riconvertire M in stringa e verificare se avete decifrato correttamente
'''

modulus = """
    00:b0:17:96:e2:cb:30:18:93:dd:60:69:92:d5:87:
    01:99:b1:fc:70:50:55:9e:78:12:c8:0e:6b:45:c4:
    e1:60:18:97:81:c6:11:73:71:b2:40:50:ad:68:d7:
    dd:d1:9d:01:f7:56:fe:7a:dd:76:d9:ac:b7:1f:59:
    74:bb:e5:74:0d:08:ef:a7:dc:48:12:a6:25:2f:c2:
    d6:55:9e:33:68:26:b9:76:af:21:7c:3c:a1:8c:83:
    c1:77:cb:05:9b:30:dd:7b:a2:87:7d:f6:d2:58:f6:
    58:90:18:6e:d3:be:97:4f:e2:f9:22:6b:bf:34:9c:
    c3:51:7f:04:bf:f1:5b:ca:10:94:92:58:0a:39:7e:
    3e:1e:d0:b3:85:20:5e:70:54:38:51:68:46:ac:af:
    db:20:50:93:e2:c6:6f:03:b2:09:ef:40:4c:24:9d:
    f5:93:22:cc:2e:39:fe:fd:97:c3:8f:cb:c4:a5:af:
    17:b1:79:14:19:64:aa:38:92:fa:95:5d:38:49:d5:
    2b:cb:d5:da:90:c6:4e:2c:09:74:44:a3:95:7d:38:
    b6:c3:03:68:a2:6a:c4:43:33:d0:e3:77:84:19:9a:
    3b:db:5b:cd:74:d3:46:e8:cd:b7:a7:43:3e:be:e0:
    0f:30:c7:30:6a:87:71:19:ac:c4:ac:90:c7:42:0a:
    19:7f
"""
# pulizia della stringa, tolgo due punti, a capo e spazi
modulus_str_pulita = modulus.replace(":", "").replace("\n", "").replace(" ", "") 

n = int(modulus_str_pulita, 16) # stringa esadecimale convertita in intero decimale
e = 3 # esponente pubblico 

private_exponent = '''
1d:59:43:d0:77:32:ae:c3:4f:90:11:98:78:eb:d5:
    99:9d:aa:12:b8:0e:45:14:03:21:57:bc:8b:a0:d0:
    3a:ae:c3:ea:f6:58:3d:e8:48:60:0d:72:3c:23:fa:
    4d:9a:2a:fe:8e:7f:bf:24:e9:24:47:73:da:8e:e8:
    c9:fb:93:57:81:7d:46:a4:b6:ad:c6:5b:87:f5:ce:
    63:9a:5d:e6:b1:1e:e9:1d:30:3f:5f:70:42:15:f5:
    93:f7:2b:99:dd:7a:3f:45:c1:3f:a9:23:0e:d3:b9:
    6d:59:67:cd:f5:19:37:fb:29:85:bc:9f:de:1a:20:
    8d:95:2b:75:52:e4:a1:ad:27:41:bb:4c:42:62:ad:
    1b:3e:be:ee:48:d1:e2:47:ac:25:a3:7d:58:0c:18:
    39:11:d5:bd:52:ff:ef:7a:56:a3:e9:65:59:98:1a:
    09:9c:4b:5f:1a:53:79:bf:20:ef:2d:13:42:8d:ab:
    c0:80:11:d4:87:01:77:ad:cc:c0:33:9a:fa:82:3b:
    e2:6b:ef:ee:ab:65:4f:a5:94:a9:24:3a:3a:22:4d:
    83:42:10:b9:22:d3:af:e0:be:ae:43:86:1b:b1:4f:
    3a:36:56:c2:6e:5f:01:9c:04:db:e2:8f:13:31:9b:
    9e:7f:89:a4:72:4f:50:5e:06:2c:15:02:e5:08:94:
    ff
'''
private_exponent_str_pulita = private_exponent.replace(":", "").replace("\n", "").replace(" ", "")
d = int(private_exponent_str_pulita, 16) # esponente privato convertito in un intero decimale
print(f"d = {d}")
print("-" * 100)

msg = "Nel mezzo del cammin di nostra vita mi ritrovai per una selva oscura, ché la diritta via era smarrita."
msg_int = int.from_bytes(msg.encode(), "big")
# con msg.encode() ottengo i byte della stringa
# "big" il byte più significativo viene per primo
# int.from_bytes(...) prende una sequenza di byte e la interpreta come un numero intero
print(msg_int)

# Messaggio Cifrato
cifra = pow(msg_int, e, n)
print(cifra)

# Messaggio Decifrato
decifra = pow(cifra, d, n) # messaggio decifrato come numero intero
print(decifra)

decifra_str = decifra.to_bytes((decifra.bit_length() + 7) // 8, "big").decode()
# decifra.bit_length(), restitusice quanti bit servono per rappresentare il numero
# aggiungo 7 prima di fare la divisione intera (//8....1 byte = 8 bit), per arrotondare verso l'alto
# .decode() converto i byte in una stringa leggibile usando la codifica predefinita (utf-8)
print(decifra_str)


xd = int("10100101", 5)
print(xd)
print(ord("a"))


# esempio usando "little"
# op1
def S2N(s: str):
    tot = 0
    esp = 0

    for c in s:
        tot = tot + 256 ** esp * ord(c)
        esp = esp + 1
    
    return tot

print(f"{s} in decimale è: {S2N(s)}")


#op2

def S2Ne(s):
    tot = 0
    for c in s[::-1]:
        tot = (tot << 8) | ord(c)
    return tot
print(f"{s} in decimale è: {S2N(s)}")

