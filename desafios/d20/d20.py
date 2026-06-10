from rich import print
from rich.panel import Panel

class Gamer:

    def __init__(self, nome='', nick='', lista_favs=None):
        self.nome=nome
        self.nick=nick
        self.lista_favs=lista_favs
        if lista_favs is None:
            self.lista_favs=[]
        

    def add_favs(self, jogo=''):
        self.lista_favs.append(jogo)
        self.lista_favs= sorted(self.lista_favs, key=str.lower)
        
    
    def ficha(self):
        conteudo=f'Nome real: [black on white] {self.nome} [/]'
        conteudo+=f'\nJogos favoritos:'
        for num, game in enumerate(self.lista_favs):
            conteudo+=f'\n:video_game: [black on blue]{game}[/]'
        painel=Panel(conteudo, title=f'Jogador <{self.nick}>')
        print(painel)

j1= Gamer('Maria', 'Mimi')
j1.add_favs('Mario')
j1.add_favs('Hoozy')
j1.add_favs('The sims')
j1.ficha()