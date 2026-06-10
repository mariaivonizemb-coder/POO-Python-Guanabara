# Desafio 20 - Perfil Gamer

## Sobre o Projeto

Este projeto foi desenvolvido como parte dos estudos de Programação Orientada a Objetos (POO) em Python.

O sistema representa o perfil de um jogador, armazenando informações pessoais e uma lista de jogos favoritos. Também permite adicionar novos jogos à coleção e exibir uma ficha organizada utilizando a biblioteca Rich.

---

## Conceitos Praticados

* Programação Orientada a Objetos (POO)
* Classes e Objetos
* Método construtor (`__init__`)
* Atributos de instância
* Listas em Python
* Métodos
* Ordenação de coleções
* Iteração com `for`
* Formatação de saída com Rich

---

## Estrutura da Classe

A classe `Gamer` representa um jogador e possui os seguintes atributos:

| Atributo     | Descrição                   |
| ------------ | --------------------------- |
| `nome`       | Nome real do jogador        |
| `nick`       | Apelido utilizado nos jogos |
| `lista_favs` | Lista de jogos favoritos    |

---

## Métodos Disponíveis

| Método       | Função                                     |
| ------------ | ------------------------------------------ |
| `add_favs()` | Adiciona um novo jogo à lista de favoritos |
| `ficha()`    | Exibe uma ficha completa do jogador        |

---

## Funcionalidades

* Cadastro de nome e nickname.
* Armazenamento de jogos favoritos.
* Ordenação automática dos jogos em ordem alfabética.
* Exibição organizada das informações utilizando painéis da biblioteca Rich.

---

## Exemplo de Uso

```python
j1 = Gamer('Maria', 'Mimi')

j1.add_favs('Mario')
j1.add_favs('Hoozy')
j1.add_favs('The Sims')

j1.ficha()
```

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

Este exercício foi desenvolvido para praticar o uso de listas como atributos de objetos, manipulação de coleções, ordenação de dados e criação de interfaces mais amigáveis para aplicações executadas no terminal.

---

## Autora

**Maria Ivonize**

Estudante de Tecnologia da Informação (T.I.) em formação, dedicada ao desenvolvimento de habilidades em programação e engenharia de software.

Atualmente aprofundando conhecimentos em Python, Programação Orientada a Objetos (POO), Git, GitHub e boas práticas de desenvolvimento através da construção de projetos e resolução de desafios práticos.
