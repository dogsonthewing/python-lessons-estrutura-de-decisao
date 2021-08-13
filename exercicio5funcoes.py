def receptornota(prova):
   print('Digite a nota da sua' , prova)
   nota = float(input())
   if nota > 10 or nota < 0:
      print('Apenas valores entre 0 e 10')
      receptornota(prova)
   elif nota >= 0 or nota <= 10:
      return float(nota)


def calculomedia(p1nota,p2nota):
    mediasem = (p1nota + p2nota) / 2
    return mediasem


def aprovacao(mediasem):
   if mediasem == 10:
      print('Aprovado com Distinção')
   elif mediasem >= 7:
      print('Aprovado')
   else:
      print('Reprovado')