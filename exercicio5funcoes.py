def main():
    p1nota = receptornota('P1')
    p2nota = receptornota('P2')

    mediasem = calculomedia(p1nota,p2nota)

    aprovacao(mediasem)
    return


def receptornota(prova):
   print('Digite a nota da sua' , prova)
   nota = float(input())
   if validadordenota(nota) == True:
      return float(nota)
   else:
      print('Apenas valores entre 0 e 10')
      print('----------------------------')
   return receptornota(prova)
   

def validadordenota(nota):
   if nota in range(-1,11):
      return True
   else:
      return False
   
      
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