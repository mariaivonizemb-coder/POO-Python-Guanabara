#Declaração de classe
class Gafanhoto:
    def __init__(self): #método construtor
        #Atributos de instãncia
        self.nome=""
        self.idade=0


    #Métodos de Instância
    def aniversário(self):
        self.idade+=1


    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'


#Declração de objetos
g1=Gafanhoto() #() é chamada ao método construtor; g1 é objeto
g1.nome="Maria" #é atributo pq nao tem ()
g1.idade=22 
g1.aniversário()#é um método
print(g1.mensagem())

g2=Gafanhoto()
g2.nome="Mauro"
g2.idade=53
print(g2.mensagem())

g3=Gafanhoto()
print(g3.mensagem())