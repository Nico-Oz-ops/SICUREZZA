p = 23
g = 11
a = 6
b = 9

A = pow(g, a, p) # chiave pubblica di A

B = pow(g, b, p) # chiave pubblica di B

# Scambio

segreto_a = pow(B, a, p) # chiave segreta A
segreto_b = pow(A, b, p) # chiave segreta B

# controllo delle chiave segrete
if segreto_a == segreto_b:
    print("Le chiave segrete coincidono")

else:
    print("Le chiave segrete non coincidono")