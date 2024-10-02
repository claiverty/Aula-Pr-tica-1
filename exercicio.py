#Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de
#desconto a ser aplicado a ele. Calcule e exiba o valor do desconto e o preço final do produto.
preco = float(input('Digite o preço do produto: '))
percentual = float(input('Digite o percentual de desconto (0-100%): '))

desconto = preco * (percentual / 100)
final = preco - percentual

print(f'O preço do produto é {preco}. O Desconto de {percentual}%')
print(f'Valor calculado de desconto: {desconto}. Valor final do produto: {final}')

#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado 
#pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
kmrodado = int(input('Quantos km foram rodados?: '))
dias = int(input('Por quantos dias o carro foi alugado?: '))

diaria = 60 * dias
valorkm = 0.15 * kmrodado

final = diaria + valorkm
print(f'O carro foi alugado por {dias} dias e percorreu {kmrodado} quilómetros.')
print(f'O valor total do aluguel do carro é de R${final}. Obrigado pela preferência!')

#Crie uma variável de string que receba uma frase qualquer. Crie uma segunda variável,
#agora contendo a metade da string digitada. Imprima na tela somente os dois últimos
#caracteres da segunda variável do tipo string.
frase = input('Digite uma frase: ')
tam = len(frase)

frase2 = frase[:int(tam/2)]

print(frase2[-2:])