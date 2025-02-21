"""
Missão 9: Calculando Dobro de um Número 🛠️
Os alunos precisam de um programa que ajude em cálculos rápidos. 
Sua tarefa é criar uma função que receba um número e retorne o dobro do seu valor.
➡️ Exemplo: dobro(5)
➡️ Saída: "O dobro de 5 é 10"

"""

# Função que calcula o dobro
def dobro(num):
    return num * 2

# Pedindo um número e chamando a função
numero = int(input("Digite um número: "))
print(f"O dobro de {numero} é {dobro(numero)}")
