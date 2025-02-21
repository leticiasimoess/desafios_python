"""
Missão 1: Restaurando as Regras Escolares 📝 
O vírus apagou os critérios de aprovação dos alunos!
 Para ajudar o Professor Byte a organizar o sistema,
sua tarefa é criar um programa que verifique se um
aluno foi aprovado (nota maior ou igual à 6) ou
reprovado (nota menor ou igual à 5).
"""

#Regras 
#se a nota for 6 ou > o aluno está aprovado
#se a nota for 8 ou >  Parabéns! Você foi APROVADO com nota alta
#se a nota for 5 ou < o aluno está reprovado


#Passos
#1 primeiro vamos pedir a nota do aluno 
#2 em seguida verificar
#3por im mostrar o resultado onde o programinha irá dizer se passou ou não


nota = float(input("Digite a nota do aluno(a): ")) 

if nota >= 6:
    if nota > 8:
        
        print("🎉 Parabéns! Você foi APROVADO com nota alta!")
        print("✅ O aluno(a) foi APROVADO!")    
    
else:

    print("😅 Foi por pouco! Estude um pouco mais na próxima vez! Você foi REPROVADO.")
