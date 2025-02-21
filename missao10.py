"""
Missão 10: Contando Letras 🔄
O sistema precisa contar quantas letras há em um nome.
➡️ Crie uma função que receba um nome e diga quantas letras esse nome tem.
➡️ Exemplo: contar_letras("Ana")
➡️ Saída:" O nome Ana tem 3 letras"
"""

# A Função len vai contar quantos caracteres existe no nome
def contar_letras(nome):
    return len(nome)

# Vai pedir o nome e chamar a função
nome = input("Digite um nome: ")
print(f"O nome {nome} tem {contar_letras(nome)} letras.")
