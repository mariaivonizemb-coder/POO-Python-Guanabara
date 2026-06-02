#Declaração de classe
class Gafanhoto:
    def __init__(self, nome='vazio', idade=0): #método construtor
        #Atributos de instãncia
        '''
        Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade
        
        Para criar uma noca pessoa, use
        variavel=Gafanhoto(nome,idade)
        '''
        self.nome=nome
        self.idade=idade


    #Métodos de Instância
    def aniversário(self):
        self.idade+=1


    #def mensagem(self):
        #return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'
    
    def __str__(self): #Dunder Method
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'


    def __getstate__(self): #Pd ser personalizavel
        return f'Estado: nome {self.nome}, idade {self.idade}'

#Declração de objetos
g1=Gafanhoto("Maria", 22) #() é chamada ao método construtor; g1 é objeto
g1.aniversário()#é um método
#print(g1.mensagem())#graças ao def str n precisamos mais desse

#print(g1.__doc__)
#print(g1)
print(g1.__dict__) #Atributo
print(g1.__getstate__())#Método tem ()
print(g1.__class__) #Classe do objeto