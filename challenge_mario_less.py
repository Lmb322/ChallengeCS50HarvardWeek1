bloco = '#'
espaco = ' '
while True:
    try:
        altura = int(input('Digite a altura de 1 a 8: '))
        if altura > 0 and altura < 9:
            for i in range (altura):
                qtde_espaco = altura - i - 1
                print(f'{espaco*qtde_espaco}{bloco*(i+1)}')
            break
        else:
            print('Numero invalido')
    except ValueError:
        print('Erro no caractere inserido digite apenas números inteiros!')
    continue