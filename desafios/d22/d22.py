from rich import print
from rich.panel import Panel

class Controle_Remoto:
    canal_min:int=1
    canal_max:int=6
    volume_min:int=1
    volume_max=5

    def __init__(self, canal=1, volume=2):
        self.canal_atual:int=canal
        self.volume_atual:int=volume
        self.ligado:bool= False

    def liga_desliga(self):
        self.ligado=not self.ligado

    def mostrar_tv(self):
        conteudo=''
        if not self.ligado:
            conteudo=f':prohibited: [red] A tv está desligada[/]'
        else:
            conteudo=f'CANAL ='
            for canal in range(Controle_Remoto.canal_min, Controle_Remoto.canal_max+1):
                if canal==self.canal_atual:
                    conteudo+=f'[yellow on yellow] {canal} [/]'
                else:
                    conteudo+=f" {canal} "
            conteudo+=f'\nVOLUME ='
            for volume in range (Controle_Remoto.volume_min, Controle_Remoto.volume_max+1):
                if volume <= self.volume_atual:
                    conteudo+=f'[black on cyan] [/]'
                else:
                    conteudo+='[black on white] [/]'

        tv=Panel(conteudo, title='[TV]', width=30)
        print(tv)

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == Controle_Remoto.canal_max:
                self.canal_atual = Controle_Remoto.canal_min
            else:
                self.canal_atual+=1

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual==Controle_Remoto.canal_min:
                self.canal_atual=Controle_Remoto.canal_max
            else:
                self.canal_atual-=1

    def volume_mais(self):
        if self.ligado:
            if self.volume_atual!=Controle_Remoto.volume_max:
                self.volume_atual+=1
    
    def volume_menos(self):
        if self.ligado:
            if self.volume_atual!=Controle_Remoto.volume_min:
                self.volume_atual-=1
                

c=Controle_Remoto(2,1)
while True:
    c.mostrar_tv()
    comando=str(input(f'< CH{c.canal_atual} >  - VOL{c.volume_atual} +'))
    match comando:
        case'0':
            break
        case '@':
            c.liga_desliga()
        case '>':
            c.canal_mais()
        case '<':
            c.canal_menos()
        case '-':
            c.volume_menos()
        case '+':
            c.volume_mais()
    print('\n'*10)

       
