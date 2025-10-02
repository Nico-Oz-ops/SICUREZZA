'''Scrivere un programma che apra un file, lo legga in memoria, selezioni un byte, 
selezioni un bit casualmente e lo modifichi'''

# leggo la riga di comando
import sys 
import random


# print("Argomenti della riga di comando:", sys.argv) 
if len(sys.argv) != 2:
    print(f"Usage: python random_bit.py <nome file>")
    sys.exit(1)


# apro il file in lettura
content = None
with open(sys.argv[1], "rb") as f:
    # r = read e b = binary
    # leggio il contenuto del file
    content = f.read()

pos = random.randint(0, len(content) - 1)
byte = content[pos]

# estraggo il bit casuale 
bit = random.randint(0, 7) 
valore = 1 << bit 
# negazione 
byte = byte ^ valore 

# aggiorno il byte del file 
content = content[:pos] + bytes([byte]) + content[pos + 1:]

# salvo il file 
with open(sys.argv[1], "wb") as f:
    f.write(content)
print(f"Modificato il bit {bit} del byte alla posizione {pos} nel file {sys.argv[1]}") 
sys.exit(0)


# sys.argv = elenco di parametri che vengono presi dalla riga di comando (compreso il nome del file (il primo elemento))
