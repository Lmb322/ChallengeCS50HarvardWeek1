altura = int(input('Digite a altura: '))
bloco = '#'
espaco = ' ' 
for i in range (altura):
    qtde_espaco = altura - i - 1
    print(f'{espaco*qtde_espaco}{bloco*(i+1)} {bloco*(i+1)}')
