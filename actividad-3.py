import hashlib
import random

g = 2
print(f'Base: {g}')
primeNumber = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919
print(f'Numero primo: {primeNumber}')

alice = random.getrandbits(256)
print(f'\nLlave privada de Alice: {alice}')
bob = random.getrandbits(256)
print(f'Llave privada de Bob: {bob}')
eve = random.getrandbits(256)
print(f'Llave privada de Bob: {eve}')

print('\nIntecambio de mensajes')
Alice = pow(g, alice, primeNumber)
Bob = pow(g, bob, primeNumber)
Eve = pow(g, eve, primeNumber)
print(f'Mensaje de alice: {Alice}')
print(f'Mensaje de bob: {Bob}')
print(f'Mensaje de eve: {Eve}')

print('\nModular Inverso')
s1 = pow(Alice, eve, primeNumber)
s2 = pow(Eve, alice, primeNumber)
print(s1)
print(s2)

if s1 == s2:
    s = hashlib.sha256(str(s1).encode()).hexdigest()
    print(f'\nLlave SHA256: {s}')
else:
    print('LLaves incorrectas')


print('\nModular Inversion')
s3 = pow(Bob, eve, primeNumber)
s4 = pow(Eve, bob, primeNumber)
print(s3)
print(s4)

if s3 == s4:
    s = hashlib.sha256(str(s3).encode()).hexdigest()
    print(f'\nLlave SHA256: {s}')
else:
    print('LLaves incorrectas')


print('\nComunicacion de Alice con Bob:')
if s1 == s3:
    s = hashlib.sha256(str(s1).encode()).hexdigest()
    print(f'\nLlave SHA256: {s}')
else:
    print('LLaves incorrectas')
