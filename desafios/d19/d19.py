from rich import print

class Livro:

    def __init__(self, titulo='', paginas=0, pagina_atual=1):
        self.titulo=titulo
        self.paginas=paginas
        self.pagina_atual=pagina_atual

        print(f':open_book: Você acabou de abrir o livro {self.titulo} que tem  {self.paginas} páginas, você está na página {self.pagina_atual}')

       
    def avançar_pagina(self, quantidade=1):
        if  self.pagina_atual + quantidade <= self.paginas:
            self.pagina_atual+=quantidade
            print(f'Página avançada para [violet]{self.pagina_atual}[/] do livro [blue]{self.titulo}[/]')
        else:
            print(f'Não é possível avançar [violet] {quantidade}[/] páginas, pois o livro acaba em [white] {self.paginas}[/] páginas')

    def voltar_paginas(self, quantidade=1):
        if self.pagina_atual - quantidade >=1:
            self.pagina_atual-=quantidade
            print(f'Página voltada para [red] {self.pagina_atual}[/] do livro [blue] {self.titulo}[/]')
        else:
            print(f'Não é possível voltar [red] {quantidade}[/] páginas, pois o livro começa na página [white] 1[/]')
    
l1= Livro('Bridgerton', 250)
l1.avançar_pagina(210)
l1.voltar_paginas(500)