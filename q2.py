entrada = str(input())

if 'a' not in entrada.lower():
    print("A letra 'a' ou 'A' não está na string enviada.")
else:
    print("A letra 'a' ou 'A' está na string enviada.")
    print(f"A letra 'a'(minúscula) aparece {entrada.count('a')} vezes na string enviada.")
    print(f"A letra 'A'(maiúscula) aparece {entrada.count('A')} vezes na string enviada.")