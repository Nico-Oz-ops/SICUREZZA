'''
Scrivere un programma PYTHON che a partire da una stringa la cifra con la tecnica XOR
Successivamente mostrare che la stringa cifrata, riapplicando lo stesso XOR, torna la stringa originale. 

Per fare lo XOR utilizzate un solo valore: 57
Quindi data la stringa di esempio “Nel mezzo del cammin di nostra vita”, dovete fare per ogni 
carattere della stringa lo xor con il valore 57
“N” xor 57, “e” xor 57, …
Ottenendo una lista di numeri es: 78 (che è il codice asciii  della lettera N) xor 
(si indica con il simbolo ^) => 78 ^ 57 = 119

E così via per tutta la stringa. Al termine stampare la lista di numeri ottenuti
In fondo a partire dalla lista di numeri, riapplicare lo xor sempre con 57 e 
quindi ottenere (ricostruendola) la stringa originale
NB: potreste utilizzare input(“…”) in modo da leggere sia la stringa da cifrare, sia il valore segreto da applicare come xor
'''
from functools import reduce

input_utente = input("Inserisci stringa: ")
key = int(input("Chiave: "))
lista_cifrata = []
for element in input_utente:
    numero_cifrato = ord(element) ^ key
    lista_cifrata.append(numero_cifrato)
print("Messaggio cifrato: ", lista_cifrata)


lista_decifrata = []
for elemento in lista_cifrata:
    lettera_decrifrata = chr(elemento ^ key)
    lista_decifrata.append(lettera_decrifrata)
print("Messaggio cifrato: ", lista_decifrata)



msg = input("Dammi il messaggio: ")
key = int(input("Dammi la chiave: "))

cifrato = [ord(carattere)^key for carattere in msg]
#oppure
cifrato=[]
for carattere in msg:
    cifrato.append(ord(carattere)^key)
print("Messaggio cifrato: ", cifrato)

decifrato = ''.join([chr(carattere^key) for carattere in cifrato])
# oppure
decifrato = []
for carattere in cifrato:
    decifrato.append(chr(carattere^key))
decifrato = ''.join(decifrato)
print("Messaggio decifrato: ", decifrato)
# Nota: join è un metodo delle stringhe, non una funzione globale
# Quindi non posso fare join(cifrato) ma devo fare ''.join(cifrato)
# oppure usare join(cifrato) se cifrato è una lista di stringhe
# oppure ''.join(cifrato) se cifrato è una lista di caratteri
# oppure ''.join(map(chr, cifrato)) se cifrato è una lista di interi

#In un altro modo, usando map e reduce
cifrato = list(map(lambda c: ord(c) ^ key, msg))
print("Messaggio cifrato: ", cifrato)

decifrato = reduce(lambda x,y: x+y, map(lambda x : chr(x ^ key), cifrato), "")
print("Messaggio decifrato: ", decifrato)

# la map trasforma una lista in un'altra lista consentendo di modificare gli elementi
l=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x: x*3, l)))
print(list(map(lambda x: x*x, l)))
# data la lista l intendo sommare tutti gli elementi tra loro
print(reduce(lambda x,y: x+y, l, 0))
