from rich import print

class Caneta:

    def __init__(self, cor='', tampada=True):
        self.cor=cor
        self.tampada=tampada

    def destampar(self,):
        if self.tampada==True:
            self.tampada=False
       
        
    def escrever(self, texto=''):
        if self.tampada==False:
            self.texto=texto
            print(f'[{self.cor}] {texto} [/{self.cor}]')
        else:
            print('Você precisa destampar a sua caneta para escrever!')
       
        

c1=Caneta('red')



c1.escrever('Olá td bem?')