def media(lista):
   nota = sum(lista) / len(lista)
   if nota < 4:
      return "Reprovado", nota
   elif nota < 6:
      return "Recuperação", nota
   else:
      return "Aprovado", nota
   
   

# Exemplo de lista de notas
lista = [7.5, 8.0, 9.2, 6.8, 10.0]



media_notas = media(lista)
print("A média das notas é:", media_notas)


#Crie um teste para a função media, se o aluno tirar menos do que 4 está reprovado, se tirar entre 4 e 6 está de recuperação e se tirar mais do que 6 está aprovado.
def teste_media(nota):
   if nota < 4:
      return "Reprovado"
   elif nota < 6:
      return "Recuperação"
   else:
      return "Aprovado"