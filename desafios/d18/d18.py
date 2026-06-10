from rich import print
from rich.panel import Panel

class Churrasco:

    consumo_padrao:float=0.400
    preco_kg:float=82.40

    def __init__(self, pessoas=0, título=''):
        self.pessoas=pessoas
        self.título=título

    def __str__(self):
        return f"Esse é o {self.título} com {self.pessoas} pessoas participando"

    def quant_carne(self) -> float:
        return self.pessoas *Churrasco.consumo_padrao
    
    def gasto_total(self) -> float:
        return self.quant_carne()*Churrasco.preco_kg
    
    def custo_individual(self):
        return self.gasto_total()/self.pessoas
        
    
    def analisar(self):
        conteudo=f"Analisando [green]{self.título}[/] com [blue]{self.pessoas}[/] convidados"
        conteudo+= f"\nCada participante comerá {Churrasco.consumo_padrao}Kg e cada Kg custa R${Churrasco.preco_kg:,.2f}"
        conteudo+=f"\nRecomendo [blue]comprar {self.quant_carne():.3f} Kg[/] de carne"
        conteudo+=f"\nO custo total será de [green]R${self.gasto_total():,.2f}[/]"
        conteudo+=f"\nCada pessoa pagará [yellow]R${self.custo_individual():,.2f}[/] para participar"
        painel=Panel(conteudo, title=self.título)
        print(painel)


c1=Churrasco(15, 'Churras dos migos')
c1.analisar()

