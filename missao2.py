"""
Missão 2: O Sistema Eleitoral Secreto 📝 
O grêmio estudantil da escola realiza votações
para decidir melhorias e inovações, mas o vírus
desativou a verificação de elegibilidade para votar!
Sua tarefa é criar um programa que pergunte a idade do
usuário e informe se ele pode votar (mínimo: 16 anos)."""

#Passos
#1 o input("Digite sua idade: ") vai ffazer uma solicitação ao usuário para inserir a idade.
#2 Já no int(...) vai converter a entrada para número inteiro.
#3 no if idade >= 16: aqui vai ser onde vai verificar se a idade é 16 ou mais.
#4 Vai imprimir a mensagem correspondente.

#no terminal utilize python missao2.py 

idade = int(input("Digite sua idade: "))

if idade >= 16:
    print("Você pode votar! 🗳️")
else:
    print("Você ainda não pode votar. ⛔")
