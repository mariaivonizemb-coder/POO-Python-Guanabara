# Desafio 19 - Controle de Leitura de Livros

## Sobre o Projeto

Este projeto foi desenvolvido como parte dos estudos de Programação Orientada a Objetos (POO) em Python.

O sistema simula a leitura de um livro, permitindo acompanhar a página atual, avançar páginas e retornar páginas já lidas, respeitando os limites do livro.

A aplicação utiliza a biblioteca Rich para tornar as mensagens exibidas no terminal mais organizadas e visualmente agradáveis.

---

## Conceitos Praticados

* Programação Orientada a Objetos (POO)
* Classes e Objetos
* Método construtor (`__init__`)
* Atributos de instância
* Métodos
* Validação de dados
* Estruturas condicionais
* Formatação de saída com Rich

---

## Estrutura da Classe

A classe `Livro` representa um livro em leitura e possui os seguintes atributos:

| Atributo       | Descrição                          |
| -------------- | ---------------------------------- |
| `titulo`       | Nome do livro                      |
| `paginas`      | Quantidade total de páginas        |
| `pagina_atual` | Página em que o leitor se encontra |

---

## Métodos Disponíveis

| Método             | Função                               |
| ------------------ | ------------------------------------ |
| `avançar_pagina()` | Avança uma ou mais páginas do livro  |
| `voltar_paginas()` | Retorna uma ou mais páginas já lidas |

---

## Regras Implementadas

* Não é possível avançar além da última página do livro.
* Não é possível voltar para uma página anterior à página 1.
* O sistema informa ao usuário quando uma operação não pode ser realizada.

---

## Exemplo de Uso

```python
l1 = Livro('Bridgerton', 250)

l1.avançar_pagina(210)
l1.voltar_paginas(500)
```

### Funcionalidades Demonstradas

* Inicialização do livro
* Controle da página atual
* Avanço de páginas
* Retorno de páginas
* Validação dos limites de leitura

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

Este exercício foi desenvolvido para praticar a manipulação de estados de objetos, validação de regras de negócio e implementação de métodos responsáveis por controlar o comportamento de uma classe.

---

## Autora

**Maria Ivonize**

Estudante de Tecnologia da Informação (T.I.) em formação, dedicada ao desenvolvimento de habilidades em programação e engenharia de software.

Atualmente aprofundando conhecimentos em Python, Programação Orientada a Objetos (POO), Git, GitHub e boas práticas de desenvolvimento através da construção de projetos e resolução de desafios práticos.
