'''SISTEMA DE CADASTRO EM ARQUIVO CSV'''

import csv #Manipular os arquivos csv
import time #Tempo
import os # funcionalidades do terminal

print('-'*70)
nome_completo = input('Digite seu nome completo: ')
print('-'*70)
data_de_nascimento = input('Digite sua data de nascimento (DD/MM/AAAA): ')
print('-'*70)
cpf = input('Digite seu CPF (exemplo 111.222.333-44): ')

with open('ficha_cadastro.csv', 'a') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow([nome_completo, data_de_nascimento, cpf])
print()
print('***********************************')
print('* Cadastro realizado com sucesso! *')
print('***********************************')


os.system('cls')
from colorama import Fore

for i in range(0,10):
    print(f'Gerando o arquivo em: {i+1}' + Fore.GREEN)
    Fore.WHITE
    time.sleep(1)
    os.system('cls')

with open('ficha_cadastro.csv', 'r') as arquivo:
    dados = csv.reader(arquivo)
    for linha in dados:
        print(linha)
        print('-'*70)