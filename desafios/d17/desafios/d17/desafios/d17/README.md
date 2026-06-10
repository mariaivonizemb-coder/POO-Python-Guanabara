# Desafio 17 - Etiqueta de Produtos

## Sobre o Projeto

Este projeto foi desenvolvido como parte dos estudos de Programação Orientada a Objetos (POO) em Python.

O objetivo é representar produtos por meio de uma classe e exibir suas informações em uma etiqueta formatada no terminal utilizando a biblioteca Rich.

---

## Conceitos Praticados

* Programação Orientada a Objetos (POO)
* Classes e Objetos
* Método construtor (`__init__`)
* Atributos de instância
* Métodos
* Formatação de strings
* Exibição de informações com a biblioteca Rich

---

## Estrutura da Classe

A classe `Produto` possui os seguintes atributos:

* `nome` → Nome do produto
* `preço` → Valor do produto

### Método disponível

| Método       | Descrição                                                         |
| ------------ | ----------------------------------------------------------------- |
| `etiqueta()` | Exibe uma etiqueta formatada contendo o nome e o preço do produto |

---

## Exemplo de Uso

```python
p1 = Produto('Monster', 8)
p1.etiqueta()

p2 = Produto('Notebook gamer', 8000)
p2.etiqueta()
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

Este exercício foi desenvolvido para praticar conceitos fundamentais de Programação Orientada a Objetos e aprimorar a apresentação visual de informações em aplicações de terminal utilizando a biblioteca Rich.

---

## Autora

**Maria Ivonize**

Estudante de Nutrição, entusiasta de tecnologia e programação, atualmente aprofundando seus conhecimentos em Python e Programação Orientada a Objetos.
