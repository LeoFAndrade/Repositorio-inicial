fr = input('Digite uma frase:').lower().strip()
# Uma aplicação simples para analisar certas características sobre uma frase.
frase = fr.count('a')
letraA1 = fr.index('a')
letraA2 = fr.rindex('a')
print(f'A letra "A" aparece {frase} na frase')
print(f'A primeira letra "A" apareceu primeiro na posição {letraA1}')
print(f'E a ultima letra "A" aparece na posição {letraA2}')
