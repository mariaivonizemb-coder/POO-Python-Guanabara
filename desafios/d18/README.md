# Desafio 18 - Planejamento de Churrasco

## Sobre o Projeto

Este projeto foi desenvolvido como parte dos estudos de Programação Orientada a Objetos (POO) em Python.

O sistema simula o planejamento de um churrasco, calculando automaticamente a quantidade de carne necessária, o custo total do evento e o valor que cada participante deverá contribuir com base no número de convidados.

Para tornar a visualização mais agradável, os resultados são apresentados no terminal utilizando a biblioteca Rich.

---

## Conceitos Praticados

* Programação Orientada a Objetos (POO)
* Classes e Objetos
* Método construtor (`__init__`)
* Atributos de instância
* Atributos de classe
* Métodos
* Método especial `__str__`
* Cálculos matemáticos
* Formatação de strings
* Interface de terminal com Rich

---

## Estrutura da Classe

A classe `Churrasco` representa um evento e possui os seguintes atributos:

### Atributos de Classe

| Atributo         | Descrição                              |
| ---------------- | -------------------------------------- |
| `consumo_padrao` | Consumo médio de carne por pessoa (kg) |
| `preco_kg`       | Valor do quilograma da carne           |

### Atributos de Instância

| Atributo  | Descrição                   |
| --------- | --------------------------- |
| `pessoas` | Quantidade de participantes |
| `titulo`  | Nome do evento              |

---

## Métodos Disponíveis

| Método               | Função                                         |
| -------------------- | ---------------------------------------------- |
| `quant_carne()`      | Calcula a quantidade total de carne necessária |
| `gasto_total()`      | Calcula o custo total do churrasco             |
| `custo_individual()` | Calcula quanto cada participante deverá pagar  |
| `analisar()`         | Exibe um relatório completo do evento          |
| `__str__()`          | Retorna uma descrição textual do churrasco     |

---

## Exemplo de Uso

```python
c1 = Churrasco(15, 'Churras dos migos')
c1.analisar()
```

### Informações Geradas

* Quantidade recomendada de carne
* Custo total do churrasco
* Valor individual por participante
* Resumo completo do evento

---

## Tecnologias Utilizadas

* Python 3
* Rich

### Instalação da Biblioteca Rich

```bash
pip install rich
```

---

## Objetivo Educacional

Este exercício foi desenvolvido para reforçar conceitos fundamentais de Programação Orientada a Objetos, demonstrando a utilização de atributos compartilhados entre objetos, métodos para processamento de dados e geração de relatórios formatados em aplicações de terminal.

---

## Autora

**Maria Ivonize**

Estudante de Tecnologia da Informação (T.I.) em formação, dedicada ao desenvolvimento de habilidades em programação e engenharia de software.

Atualmente aprofundando conhecimentos em Python, Programação Orientada a Objetos (POO), Git, GitHub e boas práticas de desenvolvimento através da construção de projetos e resolução de desafios práticos.
