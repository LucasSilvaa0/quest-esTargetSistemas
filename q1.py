entrada = int(input())

a = 0
b = 1

if entrada < a:
    print('Não pertence à sequência.')
elif entrada == a or entrada == b:
    print('Pertence à sequência.')
else:
    while entrada > b:
        k = b
        b += a
        a = k
        
    if entrada == b:
        print('Pertence à sequência.')
    elif a < entrada < b:
        print('Não pertence à sequência.')