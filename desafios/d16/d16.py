from rich import print


class Funcionario:

    empresa='Curso em Vídeo'

    def __init__(self, nome='', setor='', cargo=''):
        self.nome= nome
        self.setor=setor
        self.cargo=cargo

    def apresentar(self):
       return (
            f':handshake: Olá, sou [violet]{self.nome}[/violet], '
            f'e sou {self.cargo} do setor {self.setor} '
            f'da empresa {Funcionario.empresa}.'
        )
    

c1=Funcionario('Maria', 'TI', 'Head')
print(c1.apresentar())

c2= Funcionario ('Pedro', 'Marketing', 'Estagiário')
print(c2.apresentar())